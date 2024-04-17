import json

from mongoengine import Document
from omni.pro.airflow.airflow_client_base import AirflowClientBase
from omni_pro_base.logger import configure_logger
from omni_pro_base.util import eval_condition
from omni_pro_grpc.grpc_function import EventRPCFucntion, WebhookRPCFucntion
from omni_pro_grpc.util import MessageToDict
from sqlalchemy.inspection import inspect

logger = configure_logger(__name__)


class ActionToAirflow(object):

    @classmethod
    def send_to_airflow(cls, cls_name, instance, action: str, context: dict, **kwargs):
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
            model_code = cls_name._collection.name if isinstance(instance, Document) else cls_name.mapped_table.name
            action_code = f"{model_code}_{str(action).lower()}"

            rpc_event = EventRPCFucntion(context=context)
            response, success, _e = rpc_event.read_event(
                {
                    "filter": {
                        "filter": f"['and',('code','=','{action_code}'), ('model__is_replic', '=',{instance.__is_replic_table__})]"
                    }
                }
            )
            if success and len((events := response.events)):
                event = events[0]

                rpc_webhook = WebhookRPCFucntion(context=context)
                response, success, _e = rpc_webhook.read_webhook({"filter": {"filter": f"['events','{event.id}']"}})
                if success and len((webhooks := response.webhooks)):
                    modified_fields = set()
                    if event.operation == "update":
                        if isinstance(instance, Document):
                            # modified_fields = instance._get_changed_fields()
                            modified_fields = set([f"{model_code}-{key}" for key in kwargs.keys()])
                        else:
                            state = inspect(instance)
                            modified_fields = set(
                                [f"{model_code}-{attr.key}" for attr in state.attrs if attr.history.has_changes()]
                            )
                    instance_pj = (
                        instance.generate_dict() if isinstance(instance, Document) else instance.model_to_dict()
                    )
                    for webhook in webhooks:

                        if event.operation == "update" and not modified_fields & set(webhook.trigger_fields):
                            continue

                        if eval_condition(instance_pj, webhook.python_code):
                            params = {
                                "instance": instance_pj,
                                "action_code": action_code,
                                "context": context,
                                "webhook": MessageToDict(webhook),
                            }
                            AirflowClientBase(context["tenant"]).run_dag(
                                dag_id=webhook.dag_id or "Signal_Event",
                                params=params,
                            )
        except Exception as e:
            logger.error(f"Error sending to Airflow: {e}")
