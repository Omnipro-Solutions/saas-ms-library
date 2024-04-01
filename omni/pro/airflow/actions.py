import json

from mongoengine import Document
from omni.pro.airflow.airflow_client_base import AirflowClientBase
from omni_pro_base.logger import configure_logger
from omni_pro_base.util import eval_condition
from omni_pro_grpc.grpc_function import EventRPCFucntion, WebhookRPCFucntion
from omni_pro_grpc.util import MessageToDict

logger = configure_logger(__name__)


class ActionToAirflow(object):

    @classmethod
    def send_to_airflow(cls, cls_name, instance, action: str, context: dict):
        """
        Send a request to Airflow to run a DAG
        :param cls_name: Name of the class or mapper
        :param instance: Model instance
        :param action: Action to be performed
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        try:
            action_code = (
                f"{cls_name._collection.name}_{str(action).lower()}"
                if isinstance(instance, Document)
                else f"{cls_name.mapped_table.name}_{str(action).lower()}"
            )
            try:
                instance = MessageToDict(instance.to_proto())
            except Exception as e:
                instance = (
                    json.loads(instance.to_json()) if isinstance(instance, Document) else instance.model_to_dict()
                )

            rpc_event = EventRPCFucntion(context=context)
            response, success, _e = rpc_event.read_event({"filter": {"filter": f"[('code','=','{action_code}')]"}})
            if success and len((events := response.events)):
                event = events[0]
                rpc_webhook = WebhookRPCFucntion(context=context)
                response, success, _e = rpc_webhook.read_webhook({"filter": {"filter": f"['events','{event.id}']"}})
                if success and len((webhooks := response.webhooks)):
                    for webhook in webhooks:
                        if eval_condition(instance, webhook.python_code):
                            params = {
                                "instance": instance,
                                "action_code": action_code,
                                "context": context,
                                "webhook": MessageToDict(webhook),
                            }
                            AirflowClientBase(context["tenant"]).run_dag(
                                dag_id="Signal_Event",
                                params=params,
                            )
                        # else:
                        #     logger.error(f"No webhook {webhook.id} condition met {webhook.python_code}")
                # else:
                #     logger.error("No webhooks found")
        except Exception as e:
            logger.error(f"Error sending to Airflow: {e}")
