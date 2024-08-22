import threading
from typing import Dict, List, Set, Type, Any
import time
from datetime import datetime
from omni_pro_base.util import nested
from google.protobuf import json_format
from google.protobuf.timestamp_pb2 import Timestamp
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

_logger = configure_logger(name=__name__)


class WebhookHandler:
    def __init__(self, crud_attrs: dict, context: dict) -> None:
        self.type_db = context.pop("type_db")
        self.context = context
        self.tenant = context.get("tenant")
        self.user = context.get("user")
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
        self.event_by_code: Dict[str, str] = {}
        self.webhooks_by_event_id: Dict[str, list] = {}
        self.instances_by_model_name_and_id: Dict[str, Dict[Any, object]] = {}
        self.session = None
        self.stack = None
        self.models_mirror_by_code: Dict[str, object] = {}
        self.paginated_limit = 50000
        self.internal_webhooks: list[dict] = []
        self.external_webhooks: list[dict] = []

    @classmethod
    def start_thread(cls, crud_attrs: dict, context: dict):
        if crud_attrs.get("created_attrs") or crud_attrs.get("updated_attrs") or crud_attrs.get("deleted_attrs"):
            if context.get("tenant") and context.get("type_db"):
                webhook_handler = WebhookHandler(crud_attrs, context)
                thread = threading.Thread(target=webhook_handler.resolve_interface)
                thread.start()
            else:
                _logger.error(f"Tenant or type db is not defined")

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
                _logger.error(f"resolve_interface sql: {str(e)}")
        elif self.type_db == "document":
            try:
                from omni.pro.database import DatabaseManager
                from omni.pro.stack import ExitStackDocument

                db_params = self.redis_manager.get_mongodb_config(Config.SERVICE_ID, self.tenant)
                db_alias = f"{self.tenant}_{db_params.get('name')}"
                db_params["db"] = db_params.pop("name")
                db_manager = DatabaseManager(**db_params)

                with ExitStackDocument(
                    document_classes=list(self.class_by_name.values()),
                    db_alias=db_alias,
                ) as stack:
                    self.stack = stack
                    self.execute_events()

            except Exception as e:
                _logger.error(f"resolve_interface sql: {str(e)}")

    @measure_time
    def execute_events(self):
        time.sleep(0.2)
        self._set_event_by_code()
        if not self.event_by_code:
            return
        self._set_webhooks_by_event_id()
        if not self.webhooks_by_event_id:
            return

        if self.created_attrs:
            self._set_internal_external_webhooks_by_operation(self.created_attrs, "create")
        if self.updated_attrs:
            self._set_internal_external_webhooks_by_operation(self.updated_attrs, "update")
        if self.deleted_attrs:
            self._set_internal_external_webhooks_by_operation(self.deleted_attrs, "delete")
        self._send_webhooks()

    def _send_webhooks(self):
        self.internal_webhooks.sort(key=lambda item: item.get("webhook").priority_level)
        for item in self.internal_webhooks:
            event = item.get("event")
            webhook = item.get("webhook")
            records = item.get("records")
            print(f"event: {event.name} - webhook: {webhook.name} - priority: {webhook.priority_level}")
            if event.operation == "delete":
                # TODO: No estan creados los servicios para eliminar en el mirro_model.py
                continue
            self._send_internal_webhook(event, webhook, records)

    @measure_time
    def _set_internal_external_webhooks_by_operation(self, operation_attrs: dict, operation: str):
        for model_name, data_attrs in operation_attrs.items():
            code = f"{model_name}_{operation}"
            event: dict = self.event_by_code.get(code)
            if event:
                event_operation: str = event.operation
                webhooks: List[dict] = self.webhooks_by_event_id.get(event.id, [])
                if webhooks:
                    # TODO: Aqui organizar los webhooks por priority
                    if not self.instances_by_model_name_and_id:
                        self._set_instances_by_model_name_and_id()
                    instances_in_model_name = self.instances_by_model_name_and_id.get(model_name, {})
                    model_ids_set = set(data_attrs)
                    instances: List[object] = [
                        instance for id, instance in instances_in_model_name.items() if id in model_ids_set
                    ]

                    if instances:
                        instances_attrs: List[dict] = [
                            instance.generate_dict() if isinstance(instance, Document) else instance.model_to_dict()
                            for instance in instances
                        ]
                        for webhook in webhooks:
                            if webhook.type_webhook == "internal":
                                records = []
                                if event_operation == "create":
                                    records: list[dict] = [
                                        item
                                        for item in instances_attrs
                                        if not webhook.python_code or eval_condition(item, webhook.python_code)
                                    ]
                                elif event_operation == "update":
                                    trigger_fields = set([attr.split("-", 1)[-1] for attr in webhook.trigger_fields])
                                    for record in instances_attrs:
                                        record_id = record.get("id")
                                        modified_fields = data_attrs.get(record_id, set())
                                        if modified_fields & trigger_fields:
                                            records.append(record)

                                if records:
                                    self.internal_webhooks.append(
                                        {"event": event, "webhook": webhook, "records": records}
                                    )

                            else:
                                instance_ids = [
                                    item.get("id")
                                    for item in instances_attrs
                                    if not webhook.python_code or eval_condition(item, webhook.python_code)
                                ]
                                if instance_ids:
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

    def _send_internal_webhook(self, event: object, webhook: object, records: list[dict]):
        if webhook.method_grpc.class_name == "MirrorModelServiceStub":
            self._set_models_mirror_by_code()
            self._send_data_to_mirror_models(event, records)

    def _send_data_to_mirror_models(self, event: object, records: list[dict]):
        log_send = ""
        len_records = len(records)
        try:
            model_code = event.model.code
            models_mirror: list[object] = self.models_mirror_by_code.get(model_code, [])
            if models_mirror:
                paginated_records = [
                    records[i : i + self.paginated_limit] for i in range(0, len(records), self.paginated_limit)
                ]
                for model_mirror in models_mirror:

                    count_items_send = 0
                    for sub_records in paginated_records:
                        items = self._get_model_mirror_items(model_mirror, sub_records)
                        pull_result: bool = self._pull_mirror_model(model_mirror, items)
                        if pull_result:
                            count_items_send += len(items)

                    log_send += f"\nMirror microservice: {model_mirror.microservice} - mirror model: {model_mirror.name}- count records = {len_records} - count items pull: {count_items_send}"

            else:
                _logger.warning(f"Model mirror with code = {model_code} does not exist")

        except Exception as ex:
            _logger.error(f"_send_data_to_mirror_models:\n{str(ex)}")
        print(f"\nlog =====> {log_send}")

    def _pull_mirror_model(self, model_mirror, items: list[dict], retries=3) -> bool:
        rpc_mirror = MirrorModelRPCFucntion(self.context, model_mirror.microservice)
        try:
            response = rpc_mirror.multi_update_model(
                {
                    "model_path": model_mirror.class_name,
                    "data": items,
                    "context": self.context,
                }
            )
            if response.get("response_standard", {}).get("success"):
                return True
            else:
                error_message = response.get("response_standard", {}).get("message")

        except Exception as e:
            error_message = str(e)
        if error_message:
            _logger.error(
                f"\nMicroservice = {model_mirror.microservice} - model mirror = {model_mirror.name}, Max retries reached. Could not pull to mirror model.\n message = {error_message}"
            )
            # Generar aqui la logica para guardar un logger de excepciones
        return False

    def _get_model_mirror_items_with_retry(self, model_mirror, sub_records, retries=3):
        attempt = 0
        while attempt < retries:
            try:
                model_mirror_items = self._get_model_mirror_items(model_mirror, sub_records)
                return model_mirror_items
            except Exception as e:
                attempt += 1
                _logger.warning(f"Error encountered: {e}. Retrying {attempt}/{retries}...")
                if attempt >= retries:
                    _logger.error(
                        f"\nMicroservice = {model_mirror.microservice} - model mirror = {model_mirror.name}, Max retries reached. Could not get model mirror items."
                    )
                    # Generar aqui la logica para guardar un logger de excepciones
        return []

    @measure_time
    def _get_model_mirror_items(self, model_mirror: object, original_records: list[dict]) -> list[dict]:

        field_aliasing_in_mirror: object = self._get_field_aliasing_in_mirror_model(model_mirror)

        if field_aliasing_in_mirror:
            filter_field_in_mirror_record: str = field_aliasing_in_mirror.code
            main_field_in_original_record: str = field_aliasing_in_mirror.field_aliasing
            return self._build_mirror_model_items(
                filter_field_in_mirror_record, main_field_in_original_record, model_mirror, original_records
            )

        return []

    def _build_mirror_model_items(
        self,
        filter_field_in_mirror_record: str,
        main_field_in_original_record: str,
        model_mirror: object,
        original_records: list[dict],
    ):
        mirror_records_by_filter_field: Dict[Any, dict] = {}

        fields = self._get_fields_in_mirror_model(model_mirror)
        items = []
        for originalRecord in original_records:
            id_original_record = originalRecord.get(main_field_in_original_record)
            # mirror_record: dict = mirror_records_by_filter_field.get(id_original_record)

            item = {
                field.code: nested(originalRecord, field.field_aliasing) for field in fields if field.field_aliasing
            }

            id_mirror_record = None

            persistence_type = model_mirror.persistence_type
            user = self.user or "admin"
            if persistence_type == "NO_SQL":
                item.update({"context": self.context})
            elif persistence_type == "SQL":
                item.update(
                    {
                        "tenant": self.tenant,
                        "updated_by": user,
                        "created_by": user,
                    }
                )

            items.append(item)

        # if items:
        #     # Se añade el nombre del campo por el cual se va a hacer la busqueda de los documentos
        #     # en la insercicio o el update del microservicio espejo
        #     items.insert(0, {
        #         'field_filter':filter_field_in_mirror_record
        #     })

        return items

    def _get_fields_in_mirror_model(self, mirror_model):
        return [field for field in mirror_model.fields if hasattr(field, "field_aliasing") and not ("." in field.code)]

    def _get_field_aliasing_in_mirror_model(self, model_mirror):
        fields = self._get_fields_in_mirror_model(model_mirror)
        field = next((field for field in fields if field.field_aliasing == "id"), None)
        if not field:
            field = next((field for field in fields if field.field_aliasing == "code"), None)
        return field

    def _set_instances_by_model_name_and_id(self):

        instances_by_model_name_and_id: Dict[str, Dict[Any, object]] = {}

        def set_data(data_attrs: dict):
            for model_name, model_attrs in data_attrs.items():
                class_model: Type[object] = self.class_by_name.get(model_name)
                if model_attrs and class_model:
                    instances: list[class_model] = []
                    model_ids = list(model_attrs.keys()) if isinstance(model_attrs, dict) else model_attrs
                    if self.session:
                        instances = (
                            self.session.query(class_model)
                            .filter(class_model.id.in_(model_ids), class_model.tenant == self.tenant)
                            .all()
                        )
                    elif self.type_db == "document":
                        instances = class_model.objects(id__in=model_ids, context__tenant=self.tenant)

                    if instances:
                        if not model_name in instances_by_model_name_and_id:
                            instances_by_model_name_and_id[model_name] = {}

                        for instance in instances:
                            instance_id = instance.id
                            if self.type_db == "document":
                                instance_id = str(instance_id)
                            if not instance_id in instances_by_model_name_and_id[model_name]:
                                instances_by_model_name_and_id[model_name][instance_id] = instance

        set_data(self.created_attrs)
        set_data(self.updated_attrs)
        set_data(self.deleted_attrs)
        self.instances_by_model_name_and_id = instances_by_model_name_and_id

    @measure_time
    def _set_webhooks_by_event_id(
        self,
    ) -> Dict[str, list]:
        webhooks_by_event_id: Dict[str, list] = {}

        try:
            filter = {
                "filter": {"filter": f"[('active','=',True)]"},
                "paginated": {"offset": 1, "limit": self.paginated_limit},
            }
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
            _logger.error(f"_set_webhooks_by_event_id: {str(ex)}")

        self.webhooks_by_event_id = webhooks_by_event_id

    @measure_time
    def _set_event_by_code(
        self,
    ) -> Dict[str, object]:
        try:
            filter_event = {
                "filter": {"filter": f"[('active','=',True)]"},
                "paginated": {"offset": 1, "limit": self.paginated_limit},
            }
            response, success, _e = self.rpc_event.read_event(filter_event)
            if success:
                events = response.events
                self.event_by_code = {event.code: event for event in events}
        except Exception as ex:
            _logger.error(f"_set_event_by_code: {str(ex)}")

    def _set_models_mirror_by_code(
        self,
    ) -> Dict[str, object]:
        if not self.models_mirror_by_code:
            try:
                params = {
                    "filter": {"filter": f"[('is_replic','=', true)]"},
                    "paginated": {"offset": 1, "limit": self.paginated_limit},
                }
                response, success, _e = self.rpc_model.read_model(params)

                if success:
                    for model in response.models:
                        model_code = model.code
                        if not model_code in self.models_mirror_by_code:
                            self.models_mirror_by_code[model_code] = []
                        self.models_mirror_by_code[model_code].append(model)
            except Exception as ex:
                _logger.error(f"_set_models_mirror_by_code: {str(ex)}")

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
