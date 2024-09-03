"""
Celery configuration and task definition.

This module configures a Celery instance using Redis as both the broker and backend. It defines two specific task queues and a task with retry policies for handling webhook resending.

Celery Configuration:
- **Broker**: Redis, at `redis://localhost:6379/5`
- **Backend**: Redis, at `redis://localhost:6379/5`
- **Task Queues**:
  - `webhook_internal`: Queue for handling internal webhooks.
  - `webhook_external`: Queue for handling external webhooks.

Defined Task:
- **retry_send_webhook**:
  - **Description**: Task that attempts to resend a webhook. If it fails, the task will retry with an exponentially increasing delay up to a maximum of 3 retries.
  - **Parameters**:
    - `self`: Reference to the Celery task instance.
    - `webhook_entry` (dict): Data of the webhook to be resent.
    - `context` (dict): Context associated with the webhook.
    - `**kwargs`: Optional additional parameters.
  - **Exceptions**:
    - `Exception`: Captures any exception during webhook resending. The task will retry if the maximum retries have not been exceeded.
    - `MaxRetriesExceededError`: Exception raised if the maximum number of retries is exceeded. The task is marked as failed.

Broker and Backend Configuration:
- `CELERY_BROKER` and `CELERY_BACKEND` are configured using environment variables to define the Redis connection.

Queue Configuration:
- Tasks are routed to specific queues (`webhook_internal` and `webhook_external`) based on the type of webhook they are handling.

Example Usage:
- To send a webhook, self.celery_app.send_task(name = name, args=[webhook_entry, self.context], kwargs=kwargs, queue=queue) to enqueue it in the appropriate queue.

Starting the Worker:
- To start the Celery worker, use the following command:
    celery -A celery_worker.app worker --loglevel=info
"""

import os
import time
from celery import Celery
from kombu import Queue
from omni.pro.webhook.webhook_handler import WebhookHandler
from celery.exceptions import MaxRetriesExceededError

os.environ["CELERY_BROKER"] = "redis://localhost:6379/5"
os.environ["CELERY_BACKEND"] = "redis://localhost:6379/5"
app = Celery(__name__, broker=os.environ.get("CELERY_BROKER"), backend=os.environ.get("CELERY_BACKEND"))

app.conf.task_queues = (
    Queue("critical"),
    Queue("high"),
    Queue("medium"),
    Queue("low"),
    Queue("very_low"),
)


@app.task(bind=True, max_retries=3, default_retry_delay=10)
def retry_send_webhook(self, webhook_entry: dict, context: dict, **kwargs):
    try:
        webhook_handler = WebhookHandler(context=context)
        webhook_handler.resend_webhook_entry(webhook_entry, timeout=30)
        return "Successful"
    except Exception as e:
        retry_count = self.request.retries or 0
        retry_delay = (2**retry_count) * 30  # example: 10s, 60s, 120s.
        try:
            raise self.retry(exc=e, countdown=retry_delay)
        except MaxRetriesExceededError:
            print("Max retries exceeded. Task failed.")
            raise e
