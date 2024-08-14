import threading
from typing import Dict, List, Set, Type, Any
import time

from google.protobuf import json_format
from omni.pro.logger import configure_logger
from omni_pro_grpc.grpc_function import EventRPCFucntion, WebhookRPCFucntion
from omni_pro_grpc.grpc_function import MirrorModelRPCFucntion, ModelRPCFucntion
from omni_pro_grpc.grpc_connector import Event, GRPClient
from omni.pro.util import measure_time
from omni.pro.config import Config
from omni.pro.airflow.airflow_client_base import AirflowClientBase
from omni.pro.redis import RedisManager
from mongoengine import Document
from omni_pro_grpc.util import MessageToDict
from omni_pro_base.util import eval_condition

logger = configure_logger(name=__name__)


class WebhookHandler:
    def __init__(self, crud_attrs: dict, context: dict) -> None:
        self.type_db = context.pop("type_db")
        self.context = context
        self.tenant = context.get("tenant")
        self.rpc_event = EventRPCFucntion(context=context, cache=True)
        self.rpc_webhook = WebhookRPCFucntion(context=context, cache=True)
        self.rpc_model = ModelRPCFucntion(context=context, cache=True)
        self.created_attrs: Dict[str, List[int]] = crud_attrs.get("created_attrs", {})
        self.updated_attrs: Dict[str, Dict[str, Set[str]]] = crud_attrs.get("updated_attrs", {})
        self.deleted_attrs: Dict[str, List[int]] = crud_attrs.get("deleted_attrs", {})
        self.class_by_name: Dict[str, Type[object]] = self._get_class_by_name()
        self.redis_manager = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        self.session = None
        self.model_mirror_by_code: Dict[str, object] = {}

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
        print(f"\n===>>>>> ****** \n{self.created_attrs}\n{self.updated_attrs}\n{self.deleted_attrs}")
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
                event_operation: str = event.operation
                webhooks: List[dict] = webhooks_by_event_id.get(event.id, [])
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
                            if webhook.type_webhook == "internal":
                                filter_instances_attrs: list[dict] = [
                                    item
                                    for item in instances_attrs
                                    if not webhook.python_code or eval_condition(item, webhook.python_code)
                                ]
                                self._send_to_internal_ms(event, webhook, filter_instances_attrs)
                            else:
                                instance_ids = [
                                    item.get("id")
                                    for item in instances_attrs
                                    if not webhook.python_code or eval_condition(item, webhook.python_code)
                                ]
                                params = {
                                    "instance_ids": instance_ids,
                                    "action_code": code,
                                    "context": self.context,
                                    "webhook": MessageToDict(webhook),
                                }
                                AirflowClientBase(self.tenant).run_dag(
                                    dag_id=webhook.get("dag_id") or "Signal_Event",
                                    params=params,
                                )

    def _send_to_internal_ms(self, event, webhook, instances_attrs: list[dict]):
        self._set_model_mirror_by_code()
        if webhook.method_grpc.class_name == "MirrorModelServiceStub":
            # params = {"filter": {"filter": f"['and', ('code','=','{event.model.code}'), ('is_replic','=', true)]"}}
            # response, success, _e = self.rpc_model.read_model(params)
            # response_attrs = json_format.MessageToDict(
            #     response, preserving_proto_field_name=True, including_default_value_fields=True
            # )
            # replic_models = []
            model_mirror = self.model_mirror_by_code.get(event.model.code)
            if model_mirror:

                self._read_instance_in_model_mirror(model_mirror, instances_attrs[0])
                client: GRPClient = GRPClient(model.microservice)
                response, success = client.call_rpc_fuction(event)
                l = 0

            else:
                logger.warning(f"Read mirror models resutl: {str(response.response_standard)}")

        self.event.update(
            dict(
                rpc_method="UpdateMirrorModel",
                request_class="CreateOrUpdateMirrorModelRequest",
                params={"context": self.context} | params,
            )
        )
        response, success, event = self.client.call_rpc_fuction(self.event) + (self.event,)
        return json_format.MessageToDict(
            response, preserving_proto_field_name=True, including_default_value_fields=True
        )

    def _read_instance_in_model_mirror(self, model_mirror, record):

        field_relational_in_mirror = self._get_field_aliasing_in_mirror_model(model_mirror)

        if field_relational_in_mirror:
            frm = json_format.MessageToDict(field_relational_in_mirror)

            # if isinstance(record.get(field_relational_in_mirror.field_aliasing), int):
            #     filter = {"filter": "[('{0}','=',{1})]".format(field_relational_in_mirror.code, record.get(field_relational_in_mirror.field_aliasing))}
            # else:
            filter = {
                "filter": "[('{0}','=','{1}')]".format(
                    field_relational_in_mirror.code, record.get(field_relational_in_mirror.field_aliasing)
                )
            }

            new_filter = {
                "model_path": model_mirror.class_name,
                "filter": filter,
                "context": self.context,
            }
            rpc_func = MirrorModelRPCFucntion(self.context, model_mirror.microservice)
            response = rpc_func.read_mirror_model(new_filter)
            model = response["mirror_models"][0] if response["mirror_models"] and "mirror_models" in response else {}

    def _get_fields_in_mirror_model(self, mirror_model):
        return [field for field in mirror_model.fields if hasattr(field, "field_aliasing") and not ("." in field.code)]

    def _get_field_aliasing_in_mirror_model(self, model_mirror):
        fields = self._get_fields_in_mirror_model(model_mirror)
        field = next((field for field in fields if field.field_aliasing == "id"), None)
        if not field:
            field = next((field for field in fields if field.field_aliasing == "code"), None)
        return field

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

    # @measure_time
    def _get_webhooks_by_event_id(
        self,
    ) -> Dict[str, list]:
        webhooks_by_event_id: Dict[str, list] = {}

        try:
            filter = {"filter": {"filter": f"[('active','=',True)]"}, "paginated": {"offset": 1, "limit": 10000}}
            response, success, _e = self.rpc_webhook.read_webhook(filter)

            if success:
                webhooks = response.webhooks
                for webhook in webhooks:
                    for event in webhook.events:
                        event_id = event.id
                        if not event_id in webhooks_by_event_id:
                            webhooks_by_event_id[event_id] = []
                        webhooks_by_event_id[event_id].append(webhook)
        except Exception as ex:
            logger.error(f"_get_webhooks_by_event_id: {str(ex)}")

        return webhooks_by_event_id

    # @measure_time
    def _get_event_by_code(
        self,
    ) -> Dict[str, object]:
        try:
            filter_event = {"filter": {"filter": f"[('active','=',True)]"}, "paginated": {"offset": 1, "limit": 10000}}
            response, success, _e = self.rpc_event.read_event(filter_event)
            if success:
                events = response.events
                return {event.code: event for event in events}
        except Exception as ex:
            logger.error(f"_get_event_by_code: {str(ex)}")
        return {}

    def _set_model_mirror_by_code(
        self,
    ) -> Dict[str, object]:
        if not self.model_mirror_by_code:
            try:
                params = {
                    "filter": {"filter": f"[('is_replic','=', true)]"},
                    "paginated": {"offset": 1, "limit": 10000},
                }
                response, success, _e = self.rpc_model.read_model(params)
                # response_attrs = json_format.MessageToDict(
                #     response, preserving_proto_field_name=True, including_default_value_fields=True
                # )
                if success:
                    self.model_mirror_by_code = {model.code: model for model in response.models}
            except Exception as ex:
                logger.error(f"_set_model_mirror_by_code: {str(ex)}")

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
