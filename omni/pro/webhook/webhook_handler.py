import json
import threading
import time
from copy import copy, deepcopy
from datetime import datetime
from typing import Any, Dict, List, Set, Type

from celery import Celery
from google.protobuf import json_format
from mongoengine import Document
from omni.pro.airflow.airflow_client_base import AirflowClientBase
from omni.pro.celery.celery_redis import CeleryRedis
from omni.pro.config import Config
from omni.pro.logger import configure_logger
from omni.pro.redis import RedisManager
from omni.pro.user.access import INTERNAL_USER
from omni.pro.util import measure_time
from omni_pro_base.http_request import OmniRequest
from omni_pro_base.util import eval_condition, nested
from omni_pro_grpc.grpc_connector import Event, GRPClient
from omni_pro_grpc.grpc_function import (
    EventRPCFucntion,
    MirrorModelRPCFucntion,
    ModelRPCFucntion,
    TemplateNotificationRPCFucntion,
    WebhookRPCFucntion,
)
from omni_pro_grpc.util import MessageToDict, format_datetime_to_iso

_logger = configure_logger(name=__name__)


class WebhookHandler:
    def __init__(self, crud_attrs: dict = {}, context: dict = {}) -> None:
        context.update({"user": INTERNAL_USER})
        self.type_db = context.pop("type_db") if "type_db" in context else None
        self.context = context
        self.tenant = context.get("tenant")
        self.user = INTERNAL_USER  ##context.get("user", "internal")
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
            return CeleryRedis(self.tenant).app
        except Exception as e:
            _logger.error(f"{str(e)}")

    @classmethod
    def start_thread(cls, crud_attrs: dict, context: dict):
        """
        Starts a new thread to handle webhook processing if certain CRUD attributes are present.

        This method checks for the presence of "created_attrs", "updated_attrs", or "deleted_attrs"
        within the provided CRUD attributes dictionary. If any of these attributes exist, and both
        the "tenant" and "type_db" are defined in the context, a new thread is created to process
        the webhook via the `WebhookHandler` class. If either "tenant" or "type_db" are missing, an
        error is logged.

        Args:
            crud_attrs (dict): A dictionary containing the CRUD attributes ("created_attrs",
                "updated_attrs", or "deleted_attrs") to be checked.
            context (dict): A dictionary containing the "tenant" and "type_db" keys for context
                verification.

        Returns:
            None
        """
        if crud_attrs.get("created_attrs") or crud_attrs.get("updated_attrs") or crud_attrs.get("deleted_attrs"):
            tenant = cls._get_tenant_in_crud_attrs(crud_attrs)
            if tenant and not context.get("tenant"):
                context["tenant"] = tenant
            if context.get("tenant") and context.get("type_db"):
                webhook_handler = WebhookHandler(crud_attrs, context)
                thread = threading.Thread(target=webhook_handler.resolve_interface)
                thread.start()
            else:
                _logger.error(f"Tenant or type db is not defined")

    @classmethod
    def _get_tenant_in_crud_attrs(cls, crud_attrs: dict) -> str:
        created_attrs = crud_attrs.get("created_attrs")
        updated_attrs = crud_attrs.get("updated_attrs")
        deleted_attrs = crud_attrs.get("deleted_attrs")
        tenant = None
        if created_attrs and created_attrs.get("tenant"):
            tenant = created_attrs.pop("tenant")
        if updated_attrs and updated_attrs.get("tenant"):
            tenant = updated_attrs.pop("tenant")
        if deleted_attrs and deleted_attrs.get("tenant"):
            tenant = deleted_attrs.pop("tenant")
        return tenant

    def resolve_interface(self):
        """
        Resolves the appropriate interface for handling events based on the database type.

        This method determines which type of database to interact with ("sql" or "document") based
        on the value of `self.type_db`. For an SQL database, it initializes a connection using
        `PostgresDatabaseManager` and executes events within a session context. For a document-based
        database, it uses `DatabaseManager` and `ExitStackDocument` to handle events within a document
        management stack context. Any exceptions during this process are logged as errors.

        Returns:
            None
        """
        if self.type_db == "sql":
            try:
                from omni.pro.database import PostgresDatabaseManager

                db_params = self.redis_manager.get_postgres_config(Config.SERVICE_ID, self.context.get("tenant"))
                pg_manager = PostgresDatabaseManager(**db_params)
                with pg_manager as session:
                    self.session = session
                    self.process_and_dispatch_webhooks()

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
                    self.process_and_dispatch_webhooks()

            except Exception as e:
                _logger.error(f"resolve_interface sql: {str(e)}")

    @measure_time
    def process_and_dispatch_webhooks(self):
        """
        Processes and dispatches webhooks based on CRUD operations and event data.

        This method initiates a short delay to allow for any asynchronous operations to settle.
        It then sets the internal state for events and associated webhooks using the provided
        CRUD attributes ("created_attrs", "updated_attrs", and "deleted_attrs"). If the required
        event or webhook data is not found, the process is halted. Once the internal and external
        webhook records are established, the method triggers the dispatch of the webhooks.

        Returns:
            None
        """
        time.sleep(0.2)
        self._set_event_by_code()
        if not self.event_by_code:
            return
        self._set_webhooks_by_event_id()
        if not self.webhooks_by_event_id:
            return

        self._configure_webhook_records_by_operation(self.created_attrs, "create")
        self._configure_webhook_records_by_operation(self.updated_attrs, "update")
        self._configure_webhook_records_by_operation(self.deleted_attrs, "delete")
        self._send_webhooks()

    def _send_webhooks(self):
        """
        Sends internal, external, and notification webhooks based on sorted priority levels.

        This method first sorts the webhooks by their priority level. It then iterates over different
        sets of webhook records (internal, external, and notification) and dispatches them accordingly.
        For internal webhooks, if the gRPC method class name is "MirrorModelServiceStub", the records
        are built and sent to mirror models. External and notification webhook records are processed
        and sent using their respective methods.

        Returns:
            None
        """
        self._sort_webhooks_by_priority_level()
        self.send_to_queue = True
        for webhook_entry in self.internal_webhook_records:
            webhook: dict = webhook_entry.get("webhook")
            if webhook.get("method_grpc", {}).get("class_name") == "MirrorModelServiceStub":
                self._build_and_send_records_to_mirror_models(webhook_entry)
            elif webhook.get("url") == "click_house":
                self._create_click_house_task(webhook_entry)

        for webhook_entry in self.external_webhook_records:
            self._send_external_webhook_records(webhook_entry)

        for webhook_entry in self.notification_webhook_records:
            self._send_notification_webhook_records(webhook_entry)

    def _create_click_house_task(self, webhook_entry: dict):
        order_ids = self._extract_order_ids_from_webhook_entry(webhook_entry)
        if self.celery_app and order_ids:
            webhook: dict = webhook_entry.get("webhook", {})
            records = webhook_entry.get("records", [])
            kwargs = {"name": webhook.get("name"), "order_ids_count": len(order_ids)}
            queue = "click_house"
            name = "tasks.sale.order.order_to_facts_file_object_storage"
            try:
                task = self.celery_app.send_task(name=name, args=[order_ids, self.context], kwargs=kwargs, queue=queue)
                _logger.debug(f"task ID: {task.id}")
            except Exception as e:
                _logger.error(str(e))

    def _extract_order_ids_from_webhook_entry(self, webhook_entry: dict) -> list:
        model = webhook_entry.get("event", {}).get("model", {})
        order_ids = []
        microservice = model.get("microservice")
        model_code = model.get("code")
        records = webhook_entry.get("records", [])
        if microservice == "saas-ms-sale":
            if model_code == "order":
                order_ids = [r.get("id") for r in records]
            elif model_code == "sale":
                order_ids = [order.get("id") for sale in records for order in sale.get("orders", [])]
            elif model_code == "order_line":
                order_ids = [r.get("order_id") for r in records]

        elif microservice == "saas-ms-stock":
            order_ids = [
                r.get("order", {}).get("order_sql_id") for r in records if r.get("order", {}).get("order_sql_id")
            ]
        if order_ids:
            order_ids = list(set(order_ids))
        return order_ids

    def _create_celery_task(self, webhook_entry: dict):
        """
        Creates a Celery task to asynchronously process a webhook entry.

        This method checks if a Celery application is available (`self.celery_app`). If so, it
        prepares the task parameters based on the provided `webhook_entry`, including the webhook
        name, number of records, and associated microservice (if applicable). The method determines
        the appropriate priority queue for the task using a predefined priority mapping. It then
        sends the task to the Celery worker for processing and prints the task ID.

        Args:
            webhook_entry (dict): A dictionary containing information about the webhook, including
                its name, records, model mirror, and priority level.

        Returns:
            None
        """
        if self.celery_app:
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

            name = "retry_send_webhook"
            try:
                task = self.celery_app.send_task(
                    name=name, args=[webhook_entry, self.context], kwargs=kwargs, queue=queue
                )
                _logger.debug(f"task ID: {task.id}")
            except Exception as e:
                _logger.error(str(e))

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
        """
        Sends notification webhook records using RPC and handles errors or retries via a queue.

        This method processes notification webhook records by dividing them into paginated sublists
        and rendering each group using a template. The rendered records are then sent as external
        webhooks. If rendering fails or an exception occurs, it logs the error and, depending on the
        configuration, either raises an exception or creates a Celery task to handle the retry.

        Args:
            webhook_entry (dict): A dictionary containing the webhook data, including records and
                the template notification details.
            timeout (float, optional): The timeout duration for the RPC call. Defaults to 0.

        Returns:
            bool: True if all notification webhook records are processed successfully.

        Raises:
            Exception: If the process fails and `send_to_queue` is not enabled.
        """
        records = webhook_entry.get("records")
        webhook = webhook_entry.get("webhook")
        rpc_template = TemplateNotificationRPCFucntion(self.context, timeout=timeout)

        paginated_records = [
            records[i : i + self.paginated_limit_notification_records]
            for i in range(0, len(records), self.paginated_limit_notification_records)
        ]
        for sub_records in paginated_records:
            try:
                template_notification = webhook.get("template_notification")
                if not template_notification:
                    raise Exception(f"Webhook without template_notification")

                model_ids = [str(record.get("id")) for record in sub_records]
                template_id = template_notification.get("id")

                response = rpc_template.template_notification_render(
                    {
                        "id": template_id,
                        "model_ids": model_ids,
                        "context": self.context,
                    }
                )
                if response.get("response_standard", {}).get("success"):
                    webhook_entry_render = copy(webhook_entry)
                    render_records = list(response.get("render", {}).values())
                    webhook_entry_render["records"] = render_records
                    self._send_external_webhook_records(webhook_entry_render, timeout=timeout)
                else:
                    raise Exception(response.get("response_standard", {}).get("message"))

            except Exception as e:
                message = str(e)
                _logger.error(f"send notification webhook: {str(e)}")
                if self.send_to_queue:
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
        """
        Sends external webhook records to a specified URL with pagination and handles errors or retries.

        This method divides the external webhook records into paginated sublists and sends each group
        to the specified URL using the `OmniRequest.make_request` method. If an error occurs during the
        request, it logs the error and, depending on the configuration, either raises an exception or
        creates a Celery task to handle the retry.

        Args:
            webhook_entry (dict): A dictionary containing the webhook data, including the URL, method,
                authentication details, and records to be sent.
            timeout (float, optional): The timeout duration for the request. Defaults to 0.

        Returns:
            bool: True if the external webhook records are successfully sent.

        Raises:
            Exception: If the process fails and `send_to_queue` is not enabled.
        """
        webhook = webhook_entry.get("webhook")
        records = webhook_entry.get("records")
        paginated_records = [
            records[i : i + self.paginated_limit_records] for i in range(0, len(records), self.paginated_limit_records)
        ]
        for sub_records in paginated_records:
            try:
                url = webhook.get("url")
                auth = webhook.get("auth")
                response = OmniRequest.make_request(
                    url,
                    webhook.get("method"),
                    json=sub_records,
                    tipo_auth=webhook.get("auth_type"),
                    auth_params=auth,
                    timeout=timeout or self.timeout_external,
                )
                response.raise_for_status()
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
        """
        Builds and sends records to mirror models based on the webhook entry data.

        This method retrieves mirror models associated with a specific event model code and sends
        paginated records to each mirror model. It logs details about the number of records sent
        and any issues encountered during the process. If no mirror models are found for the event
        model code, a warning is logged.

        Args:
            webhook_entry (dict): A dictionary containing event and record data to be sent to mirror models.

        Returns:
            None
        """
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
                        mirror_records = self._transforms_model_mirror_records(model_mirror, sub_records)
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
        _logger.debug(f"Send details:\n{log_send}")

    @measure_time
    def _send_records_to_mirror_model(self, webhook_entry: dict, timeout=0) -> bool:
        """
        Sends records to a mirror model using RPC and handles errors or retries.

        This method checks the operation type specified in the event and sends records to the mirror model
        via an RPC call. If the operation is "delete", it currently does nothing but is marked for future
        implementation. For other operations, it performs a multi-update on the mirror model. If the RPC
        call is successful, it returns True. If an error occurs or the response indicates failure, it logs
        the error and, depending on the configuration, either retries the operation by creating a Celery task
        or raises an exception.

        Args:
            webhook_entry (dict): A dictionary containing event data, model mirror details, and records to be sent.
            timeout (int, optional): The timeout duration for the RPC call. Defaults to 0.

        Returns:
            bool: True if the records are successfully sent to the mirror model, False otherwise.

        Raises:
            Exception: If the process fails and `send_to_queue` is not enabled.
        """
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
    def _configure_webhook_records_by_operation(self, operation_attrs: dict, operation: str):
        """
        Configures webhook records based on the operation type and attributes.

        This method processes records according to the specified operation (create, update, or delete)
        and the associated attributes. It sets up webhook entries for internal, external, and notification
        webhooks based on the event data, operation, and conditions specified in the webhooks. Records are
        filtered and grouped by the type of webhook and then stored in the respective lists.

        Args:
            operation_attrs (dict): A dictionary containing the attributes for each model associated with the operation.
            operation (str): The type of operation ("create", "update", or "delete").

        Returns:
            None
        """
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
                            webhook_url = webhook.get("url")
                            records: list[dict] = [
                                item
                                for item in instances_attrs
                                if not webhook.get("python_code") or eval_condition(item, webhook.get("python_code"))
                            ]
                            if event_operation == "update" and webhook_url != "click_house":
                                if webhook.get("trigger_fields"):
                                    trigger_fields = set(
                                        [attr.split("-", 1)[-1] for attr in webhook.get("trigger_fields")]
                                    )
                                    if not "active" in trigger_fields:
                                        trigger_fields.add("active")
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
    def _transforms_model_mirror_records(self, model_mirror: object, records: list[dict]) -> list[dict]:
        """
        Transforms records into the format required by the mirror model.

        This method maps the fields of each record to the mirror model's field aliases and applies necessary
        transformations such as converting datetime values to ISO format. It also adds metadata based on the
        persistence type of the mirror model (e.g., "NO_SQL" or "SQL").

        Args:
            model_mirror (object): The mirror model object containing field aliasing and persistence type information.
            records (list[dict]): A list of records to be transformed.

        Returns:
            list[dict]: A list of transformed records formatted according to the mirror model's requirements.
        """

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
                    if not field_aliasing and field_code == "active":
                        field_aliasing = field_code
                    if field_aliasing:
                        field_value = nested(record, field_aliasing)
                        if isinstance(field_value, datetime):
                            field_value = field_value.isoformat()
                        item[field_code] = field_value
                persistence_type = model_mirror.get("persistence_type")
                user = self.user or INTERNAL_USER
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
            if ("field_aliasing" in field or field.get("code") == "active") and not ("." in field.get("code"))
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
                        webhook_dict = json_format.MessageToDict(webhook, preserving_proto_field_name=True)
                        priority_map = {"critical": 1, "high": 2, "medium": 3, "low": 4, "very_low": 5}
                        priority_code = webhook_dict.get("priority_level", {}).get("code", "medium")
                        webhook_dict["priority_level"] = priority_map.get(priority_code)
                        webhooks_by_event_id[event_id].append(webhook_dict)
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
        """
        Retrieves a dictionary mapping collection or table names to their respective class types.

        Depending on the database type, this method returns a dictionary where the keys are the names of the
        collections or tables and the values are the corresponding class types. For document databases, it
        uses `BaseDocument` subclasses, and for SQL databases, it uses classes from the SQLAlchemy registry.

        Returns:
            Dict[str, Type[object]]: A dictionary mapping collection or table names to their class types.
        """
        from omni.pro.models.base import BaseDocument, BaseModel

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
