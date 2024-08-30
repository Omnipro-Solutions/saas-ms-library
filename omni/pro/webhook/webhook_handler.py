import threading
from typing import Dict, List, Set, Type, Any
import time
from datetime import datetime
from omni_pro_base.util import nested
from google.protobuf import json_format
from omni_pro_base.http_request import OmniRequest
from omni.pro.logger import configure_logger
from omni_pro_grpc.util import format_datetime_to_iso
from omni_pro_grpc.grpc_function import EventRPCFucntion, WebhookRPCFucntion
from omni_pro_grpc.grpc_function import MirrorModelRPCFucntion, ModelRPCFucntion
from omni_pro_grpc.grpc_connector import Event, GRPClient
from omni.pro.util import measure_time
from omni.pro.config import Config
from omni.pro.airflow.airflow_client_base import AirflowClientBase
from omni.pro.redis import RedisManager
from omni.pro.celery.celery_redis import CeleryRedis
from mongoengine import Document
from omni_pro_grpc.util import MessageToDict
from omni_pro_base.util import eval_condition
import json
from copy import deepcopy
from celery import Celery

_logger = configure_logger(name=__name__)


class WebhookHandler:
    def __init__(self, crud_attrs: dict = {}, context: dict = {}) -> None:
        self.type_db = context.pop("type_db") if "type_db" in context else None
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
        self.paginated_limit_records = 5000
        self.paginated_limit_notification_records = 100
        self.timeout_pull_mirror_model = 10
        self.timeout_external = 10
        self.timeout_notification = 10
        self.paginated_limit = 30000
        self.internal_webhook_records: list[dict] = []
        self.external_webhook_records: list[dict] = []
        self.notification_webhook_records: list[dict] = []
        self.send_to_queue: bool = False
        self.celery_app: Celery = self._get_celery_app()

    def _get_celery_app(self):
        try:
            return CeleryRedis.get_celery_app_by_tenant(self.tenant)
        except Exception as e:
            _logger.error(f"{str(e)}")

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

        self._set_internal_external_webhook_records_by_operation(self.created_attrs, "create")
        self._set_internal_external_webhook_records_by_operation(self.updated_attrs, "update")
        self._set_internal_external_webhook_records_by_operation(self.deleted_attrs, "delete")
        self._send_webhooks()

    def _send_webhooks(self):
        self._sort_webhooks_by_priority_level()
        self.send_to_queue = True
        for webhook_entry in self.internal_webhook_records:
            webhook: dict = webhook_entry.get("webhook")
            if webhook.get("method_grpc", {}).get("class_name") == "MirrorModelServiceStub":
                self._build_and_send_records_to_mirror_models(webhook_entry)

        for webhook_entry in self.external_webhook_records:
            self._send_external_webhook_records(webhook_entry)

        for webhook_entry in self.notification_webhook_records:
            self._send_notification_webhook_records(webhook_entry)

    def _create_celery_task(self, webhook_entry: dict):
        webhook: dict = webhook_entry.get("webhook", {})
        kwargs = {"name": webhook.get("name"), "records_count": len(webhook_entry.get("records", []))}
        model_mirror = webhook_entry.get("model_mirror")
        if model_mirror:
            kwargs["microservice"] = model_mirror.get("microservice")

        priority_queue = {
            1: "critical",
            2: "high",
            3: "medium",
            4: "low",
            5: "very_low",
        }

        priority_level: int = webhook.get("priority_level", 3)
        queue = priority_queue.get(priority_level)

        name = "celery_worker.retry_send_webhook"
        task = self.celery_app.send_task(name=name, args=[webhook_entry, self.context], kwargs=kwargs, queue=queue)
        print(f"task ID: {task.id}")

    def resend_webhook_entry(self, webhook_entry: dict, timeout: float = 0) -> bool:
        if self.context:
            model_mirror = webhook_entry.get("model_mirror")
            if model_mirror:
                self._send_records_to_mirror_model(webhook_entry, timeout=timeout)
            else:
                webhook: dict = webhook_entry.get("webhook")
                type_webhook = webhook.get("type_webhook")

                if type_webhook == "external":
                    self._send_external_webhook_records(webhook_entry, timeout=timeout)
                elif type_webhook == "notification":
                    self._send_notification_webhook_records(webhook_entry, timeout=timeout)
        else:
            raise Exception("Undefined context")

    def _send_notification_webhook_records(self, webhook_entry: dict, timeout: float = 0) -> bool:
        # Se debe consultar el renderizado enviando los ids
        # Luego enviar ese dict que devuelve el metodo a la app
        records = webhook_entry.get("records")
        webhook = webhook_entry.get("webhook")

        paginated_records = [
            records[i : i + self.paginated_limit_notification_records]
            for i in range(0, len(records), self.paginated_limit_notification_records)
        ]
        for sub_records in paginated_records:
            try:
                if not webhook.get("template_notification"):
                    raise Exception(f"Webhook without template_notification")

            except Exception as e:
                message = str(e)
                _logger.error(f"send notification webhook: {str(e)}")
                if self.send_to_queue:
                    # TODO: Logica aqui para enviarlo a cola
                    webhook_entry["message"] = message
                    self._create_celery_task(webhook_entry)
                else:
                    raise Exception(message)
        return True

    def _sort_webhooks_by_priority_level(self):
        self.internal_webhook_records.sort(key=lambda item: item.get("webhook", {}).get("priority_level"))
        self.external_webhook_records.sort(key=lambda item: item.get("webhook").get("priority_level"))
        self.notification_webhook_records.sort(key=lambda item: item.get("webhook").get("priority_level"))

    def _send_external_webhook_records(self, webhook_entry: dict, timeout: float = 0):
        webhook = webhook_entry.get("webhook")
        records = webhook_entry.get("records")
        paginated_records = [
            records[i : i + self.paginated_limit_records] for i in range(0, len(records), self.paginated_limit_records)
        ]
        for sub_records in paginated_records:
            try:
                url = webhook.get("url")
                response = OmniRequest.make_request(
                    url,
                    webhook.get("method"),
                    json=sub_records,
                    tipo_auth=webhook.get("auth_type"),
                    auth_params=webhook.get("auth"),
                    timeout=timeout or self.timeout_external,
                )
                print("GET RESPONSE APP...")
                response.raise_for_status()
                response_object = OmniRequest.get_response(response)
                print(json.dumps(response_object, indent=4))
                return True
            except Exception as e:
                message = str(e)
                _logger.error(f"send external webhook: {str(e)}")
                if self.send_to_queue:
                    webhook_entry["message"] = message
                    self._create_celery_task(webhook_entry)
                else:
                    raise Exception(message)

    def _build_and_send_records_to_mirror_models(self, webhook_entry: dict):
        event: dict = webhook_entry.get("event")
        records: list[dict] = webhook_entry.get("records")
        log_send = ""
        len_records = len(records)
        self._set_models_mirror_by_code()
        try:
            model_code = event.get("model", {}).get("code")
            models_mirror: list[dict] = self.models_mirror_by_code.get(model_code, [])
            if models_mirror:
                paginated_records = [
                    records[i : i + self.paginated_limit_records]
                    for i in range(0, len(records), self.paginated_limit_records)
                ]
                for model_mirror in models_mirror:
                    webhook_entry_mirror = deepcopy(webhook_entry)
                    webhook_entry_mirror["model_mirror"] = model_mirror
                    count_records_send = 0
                    for sub_records in paginated_records:
                        mirror_records = self._get_model_mirror_records(model_mirror, sub_records)
                        webhook_entry_mirror["records"] = mirror_records
                        pull_result: bool = self._send_records_to_mirror_model(
                            webhook_entry_mirror, timeout=self.timeout_pull_mirror_model
                        )
                        if pull_result:
                            count_records_send += len(mirror_records)

                    log_send += f"\nMirror microservice: {model_mirror.get('microservice')} - mirror model: {model_mirror.get('name')}- count records = {len_records} - count items pull: {count_records_send}"

            else:
                _logger.warning(f"Model mirror with code = {model_code} does not exist")

        except Exception as ex:
            _logger.error(f"_send_records_to_mirror_models:\n{str(ex)}")
        _logger.info(f"Send details:\n{log_send}")

    @measure_time
    def _send_records_to_mirror_model(self, webhook_entry: dict, timeout=0) -> bool:
        event = webhook_entry.get("event")
        model_mirror = webhook_entry.get("model_mirror")
        microservice = model_mirror.get("microservice")
        class_name = model_mirror.get("class_name")
        rpc_mirror = MirrorModelRPCFucntion(self.context, microservice, timeout=timeout)
        try:
            if event.get("operation") == "delete":
                # TODO: Falta añadir logica de eliminacion
                return True
            else:
                response = rpc_mirror.multi_update_model(
                    {
                        "model_path": class_name,
                        "data": webhook_entry.get("records", []),
                        "context": self.context,
                    }
                )
                if response.get("response_standard", {}).get("success"):
                    return True
                else:
                    raise Exception(response.get("response_standard", {}).get("message"))

        except Exception as e:
            message = str(e)
            _logger.error(
                f"\nMicroservice = {microservice} - model mirror = {model_mirror.get('name')}, Max retries reached. Could not pull to mirror model.\n message = {str(e)}"
            )
            if self.send_to_queue:
                webhook_entry["message"] = message
                self._create_celery_task(webhook_entry)
            else:
                raise Exception(message)
        return False

    @measure_time
    def _set_internal_external_webhook_records_by_operation(self, operation_attrs: dict, operation: str):
        for model_name, data_attrs in operation_attrs.items():
            code = f"{model_name}_{operation}"
            event: dict = self.event_by_code.get(code)
            if event:
                event_operation: str = event.get("operation")
                webhooks: List[dict] = self.webhooks_by_event_id.get(event.get("id"), [])
                if webhooks:
                    if not self.instances_by_model_name_and_id:
                        self._set_instances_by_model_name_and_id()
                    instances_in_model_name = self.instances_by_model_name_and_id.get(model_name, {})
                    model_ids_set = set(data_attrs)
                    instances: List[object] = [
                        instance for id, instance in instances_in_model_name.items() if id in model_ids_set
                    ]

                    if instances:
                        instances_by_id = {
                            str(instan.id) if self.type_db == "document" else instan.id: instan for instan in instances
                        }
                        instances_attrs: List[dict] = [
                            instance.generate_dict() if isinstance(instance, Document) else instance.model_to_dict()
                            for instance in instances
                        ]
                        for webhook in webhooks:
                            records: list[dict] = [
                                item
                                for item in instances_attrs
                                if not webhook.get("python_code") or eval_condition(item, webhook.get("python_code"))
                            ]
                            if event_operation == "update":
                                if webhook.get("trigger_fields"):
                                    trigger_fields = set(
                                        [attr.split("-", 1)[-1] for attr in webhook.get("trigger_fields")]
                                    )
                                    filter_records = []
                                    for record in records:
                                        record_id = record.get("id")
                                        modified_fields = data_attrs.get(record_id, set())
                                        if modified_fields & trigger_fields:
                                            filter_records.append(record)
                                    records = filter_records
                            if records:
                                type_webhook = webhook.get("type_webhook")
                                webhook_entry = {"event": event, "webhook": webhook, "records": records, "message": ""}
                                if type_webhook == "internal":
                                    self.internal_webhook_records.append(webhook_entry)
                                elif type_webhook == "external":
                                    webhook_entry["records"] = self._get_records_from_proto(records, instances_by_id)
                                    self.external_webhook_records.append(webhook_entry)
                                elif type_webhook == "notification":
                                    self.notification_webhook_records.append(webhook_entry)

    @measure_time
    def _get_records_from_proto(self, records: list[dict], instances_by_id: Dict[Any, object]) -> list[dict]:
        records_from_proto = []
        for record in records:
            id = record.get("id")
            instance = instances_by_id.get(id)
            if instance:
                try:
                    instance_proto = instance.to_proto()
                    records_from_proto.append(
                        json_format.MessageToDict(instance_proto, preserving_proto_field_name=True)
                    )
                except Exception as e:
                    _logger.error(f"Error converting instance to proto: {e}")
        return records_from_proto

    @measure_time
    def _get_model_mirror_records(self, model_mirror: object, records: list[dict]) -> list[dict]:

        field_aliasing_in_mirror: object = self._get_field_aliasing_in_mirror_model(model_mirror)
        items = []
        if field_aliasing_in_mirror:
            fields = self._get_fields_in_mirror_model(model_mirror)
            items = []
            for record in records:
                item = {}
                for field in fields:
                    field_aliasing = field.get("field_aliasing")
                    field_code = field.get("code")
                    if field_aliasing:
                        field_value = nested(record, field_aliasing)
                        if isinstance(field_value, datetime):
                            field_value = field_value.isoformat()
                        item[field_code] = field_value
                persistence_type = model_mirror.get("persistence_type")
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

        return items

    def _get_fields_in_mirror_model(self, mirror_model):
        return [
            field
            for field in mirror_model.get("fields")
            if "field_aliasing" in field and not ("." in field.get("code"))
        ]

    def _get_field_aliasing_in_mirror_model(self, model_mirror):
        fields = self._get_fields_in_mirror_model(model_mirror)
        field = next((field for field in fields if field.get("field_aliasing") == "id"), None)
        if not field:
            field = next((field for field in fields if field.get("field_aliasing") == "code"), None)
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

    def _instances_convert_datetime_fields_to_iso(self, instances: list[dict]) -> list[dict]:
        converted_instances = [
            {key: value.isoformat() if isinstance(value, datetime) else value for key, value in item.items()}
            for item in instances
        ]
        return converted_instances

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
                for webhook in response.webhooks:
                    for event in webhook.events:
                        event_id = event.id
                        if not event_id in webhooks_by_event_id:
                            webhooks_by_event_id[event_id] = []
                        webhooks_by_event_id[event_id].append(
                            json_format.MessageToDict(webhook, preserving_proto_field_name=True)
                        )
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
                self.event_by_code = {
                    event.code: json_format.MessageToDict(event, preserving_proto_field_name=True)
                    for event in response.events
                }
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
                        self.models_mirror_by_code[model_code].append(
                            json_format.MessageToDict(model, preserving_proto_field_name=True)
                        )
            except Exception as ex:
                _logger.error(f"_set_models_mirror_by_code: {str(ex)}")

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
