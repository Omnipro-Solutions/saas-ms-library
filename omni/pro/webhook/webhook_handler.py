import threading
from typing import Dict, List, Set, Type, Any
import time

from google.protobuf import json_format
from omni.pro.logger import configure_logger
from omni_pro_grpc.grpc_function import EventRPCFucntion, WebhookRPCFucntion
from omni.pro.util import measure_time
from omni.pro.config import Config

from sqlalchemy.orm import Session
from omni.pro.redis import RedisManager
from mongoengine import Document
from omni_pro_base.util import eval_condition

logger = configure_logger(name=__name__)


class WebhookHandler:
    def __init__(self, crud_attrs: dict, context: dict) -> None:
        self.type_db = context.pop("type_db")
        self.context = context
        self.tenant = context.get("tenant")
        self.rpc_event = EventRPCFucntion(context=context, cache=True)
        self.rpc_webhook = WebhookRPCFucntion(context=context, cache=True)
        self.created_attrs: Dict[str, List[int]] = crud_attrs.get("created_attrs", {})
        self.updated_attrs: Dict[str, Dict[str, Set[str]]] = crud_attrs.get("updated_attrs", {})
        self.deleted_attrs: Dict[str, List[int]] = crud_attrs.get("deleted_attrs", {})
        self.class_by_name: Dict[str, Type[object]] = self._get_class_by_name()
        self.redis_manager = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        self.session = None

    @classmethod
    def start_thread(cls, crud_attrs: dict, context: dict):
        if crud_attrs.get("created_attrs") or crud_attrs.get("updated_attrs") or crud_attrs.get("deleted_attrs"):
            webhook_handler = WebhookHandler(crud_attrs, context)
            thread = threading.Thread(target=webhook_handler.resolve_interface)
            thread.start()

    def resolve_interface(self):
        if self.type_db == "sql":
            try:
                from omni.pro.database import PostgresDatabaseManager

                db_params = self.redis_manager.get_postgres_config(Config.SERVICE_ID, self.context.get("tenant"))
                pg_manager = PostgresDatabaseManager(**db_params)
                with pg_manager as session:
                    self.session = session
                    self.execute_events()

            except Exception as e:
                logger.error(f"resolve_interface sql: {str(e)}")

    @measure_time
    def execute_events(self):

        # Lógica para filtrar eventos y webhooks
        # Aquí enviarías los eventos filtrados a microservicios internos y Airflow
        time.sleep(0.2)
        event_by_code: Dict[str, str] = self._get_event_by_code()
        if not event_by_code:
            print("sin eventos")
            return
        webhooks_by_event_id: Dict[str, list] = self._get_webhooks_by_event_id()
        if not webhooks_by_event_id:
            print("sin webhooks")
            return

        instances_by_model_name_and_id = self._get_instances_by_model_name_and_id()
        for model_name, model_ids in self.created_attrs.items():
            code = f"{model_name}_create"
            event: dict = event_by_code.get(code)
            if event:
                event_id: str = event.get("id")
                event_operation: str = event.get("operation")
                webhooks: List[dict] = webhooks_by_event_id.get(event_id, [])
                if webhooks:
                    instances_in_model_name = instances_by_model_name_and_id.get(model_name, {})
                    model_ids_set = set(model_ids)
                    instances: List[object] = [
                        instance for id, instance in instances_in_model_name.items() if id in model_ids_set
                    ]

                    if instances:
                        instances_attrs: List[dict] = [
                            instance.generate_dict() if isinstance(instance, Document) else instance.model_to_dict()
                            for instance in instances
                        ]
                        for webhook in webhooks:
                            # if event_operation == "update" and not modified_fields & set(webhook.trigger_fields):
                            #     continue

                            for attrs_instance in instances_attrs:
                                if eval_condition(attrs_instance, webhook.get("python_code")):
                                    # if webhook.type_webhook != "internal":
                                    #     try:
                                    #         instance_proto = instance.to_proto()
                                    #     except Exception as e:
                                    #         logger.error(f"Error converting instance to proto: {e}")
                                    # params = {
                                    #     "instance": MessageToDict(instance_proto) if instance_proto else instance_pj,
                                    #     "action_code": action_code,
                                    #     "context": context,
                                    #     "webhook": MessageToDict(webhook),
                                    # }
                                    # AirflowClientBase(context["tenant"]).run_dag(
                                    #     dag_id=webhook.dag_id or "Signal_Event",
                                    #     params=params,
                                    # )
                                    # instance_proto = None
                                    print(f"\n==> paso condicion")

    def _get_instances_by_model_name_and_id(self) -> Dict[str, Dict[Any, object]]:
        instances_by_model_name_and_id: Dict[str, Dict[Any, object]] = {}

        def set_data(data_attrs: dict):
            for model_name, model_ids in data_attrs.items():
                class_model: Type[object] = self.class_by_name.get(model_name)
                if model_ids and class_model:
                    instances: list[class_model] = []
                    if self.session:

                        instances = (
                            self.session.query(class_model)
                            .filter(class_model.id.in_(model_ids), class_model.tenant == self.tenant)
                            .all()
                        )

                        if instances:
                            if not model_name in instances_by_model_name_and_id:
                                instances_by_model_name_and_id[model_name] = {}

                            for instance in instances:
                                instance_id = instance.id
                                if not instance_id in instances_by_model_name_and_id[model_name]:
                                    instances_by_model_name_and_id[model_name][instance_id] = instance

        set_data(self.created_attrs)
        set_data(self.updated_attrs)
        set_data(self.deleted_attrs)
        return instances_by_model_name_and_id

    @measure_time
    def _get_webhooks_by_event_id(
        self,
    ) -> Dict[str, list]:
        webhooks_by_event_id: Dict[str, list] = {}

        try:
            filter = {"filter": {"filter": f"[('active','=',True)]"}, "paginated": {"offset": 1, "limit": 10000}}
            response, success, _e = self.rpc_webhook.read_webhook(filter)

            if success:
                response_data = json_format.MessageToDict(response, preserving_proto_field_name=True)
                webhooks: list[dict] = response_data.get("webhooks")

                for webhook in webhooks:
                    for event in webhook.get("events", []):
                        event_id = event.get("id")
                        if not event_id in webhooks_by_event_id:
                            webhooks_by_event_id[event_id] = []
                        webhooks_by_event_id[event_id].append(webhook)
        except Exception as ex:
            logger.error(f"_get_webhooks_by_event_id: {str(ex)}")

        return webhooks_by_event_id

    @measure_time
    def _get_event_by_code(
        self,
    ) -> Dict[str, str]:
        try:
            filter_event = {"filter": {"filter": f"[('active','=',True)]"}, "paginated": {"offset": 1, "limit": 10000}}
            response, success, _e = self.rpc_event.read_event(filter_event)
            if success:
                response_data = json_format.MessageToDict(response, preserving_proto_field_name=True)
                events: list[dict] = response_data.get("events")
                return {event.get("code"): event for event in events}
        except Exception as ex:
            logger.error(f"_get_event_by_code: {str(ex)}")
        return {}

    def _get_event_codes(self) -> list[str]:
        event_codes: list = []

        for model_name in self.created_attrs.keys():
            event_codes.append(f"{model_name}_create")
        for model_name in self.updated_attrs.keys():
            event_codes.append(f"{model_name}_update")
        for model_name in self.deleted_attrs.keys():
            event_codes.append(f"{model_name}_delete")
        return event_codes

    def _get_class_by_name(self) -> Dict[str, Type[object]]:
        from omni.pro.models.base import BaseDocument
        from omni.pro.models.base import BaseModel

        class_by_name = {}
        if self.type_db == "document":
            class_by_name = {cls._get_collection_name(): cls for cls in BaseDocument.__subclasses__()}
        elif self.type_db == "sql":
            class_by_name = {
                cls.__tablename__: cls
                for cls in BaseModel.registry._class_registry.values()
                if hasattr(cls, "__tablename__")
            }
        return class_by_name
