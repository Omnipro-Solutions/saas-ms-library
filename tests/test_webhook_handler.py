import unittest
from datetime import datetime
from unittest.mock import MagicMock, patch

import requests
from omni.pro.redis import RedisManager
from omni.pro.webhook.webhook_handler import WebhookHandler


class TestWebhookHandler(unittest.TestCase):

    def setUp(self):
        self.crud_attrs = {
            "created_attrs": {"test_model": [1, 2]},
            "updated_attrs": {"test_model": {"1": {"field1"}}},
            "deleted_attrs": {"test_model": [3]},
        }
        self.context = {"tenant": "test_tenant", "user": "test_user", "type_db": "sql"}

        # Mocks para RedisManager, Config y Celery
        self.mock_redis_manager = MagicMock()
        self.mock_celery_app = MagicMock()

        with patch("omni.pro.webhook.webhook_handler.RedisManager", return_value=self.mock_redis_manager), patch(
            "omni.pro.webhook.webhook_handler.CeleryRedis.get_celery_app_by_tenant", return_value=self.mock_celery_app
        ), patch("omni.pro.webhook.webhook_handler.Config") as MockConfig:

            # Configurar Mock para el objeto Config
            MockConfig.REDIS_HOST = "localhost"
            MockConfig.REDIS_PORT = 6379
            MockConfig.REDIS_DB = 0
            MockConfig.REDIS_SSL = False

            # Inicializar WebhookHandler
            self.handler = WebhookHandler(self.crud_attrs, self.context)
            self.handler.tenant = "test_tenant"
            self.handler.user = "test_user"
            self.handler.session = MagicMock()
            self.handler.class_by_name = {"TestModel": MagicMock()}
            self.handler.paginated_limit = 100
            self.handler.rpc_webhook = MagicMock()
            self.handler.rpc_event = MagicMock()
            self.handler.rpc_model = MagicMock()

    @patch("omni.pro.webhook.webhook_handler.RedisManager")
    @patch("omni.pro.webhook.webhook_handler.CeleryRedis.get_celery_app_by_tenant")
    def test_init_with_valid_data(self, mock_get_celery_app, mock_redis_manager):
        mock_get_celery_app.return_value = MagicMock()
        mock_redis_manager.return_value = MagicMock()

        handler = WebhookHandler(self.crud_attrs, self.context)

        self.assertEqual(handler.tenant, "test_tenant")
        self.assertEqual(handler.user, "test_user")
        self.assertEqual(handler.created_attrs, {"test_model": [1, 2]})
        self.assertEqual(handler.updated_attrs, {"test_model": {"1": {"field1"}}})
        self.assertEqual(handler.deleted_attrs, {"test_model": [3]})
        mock_get_celery_app.assert_called_once_with("test_tenant")
        mock_redis_manager.assert_called_once()

    @patch("omni.pro.webhook.webhook_handler._logger")
    @patch(
        "omni.pro.webhook.webhook_handler.CeleryRedis.get_celery_app_by_tenant", side_effect=Exception("Celery error")
    )
    def test_init_celery_app_error(self, mock_get_celery_app, mock_logger):
        handler = WebhookHandler(self.crud_attrs, self.context)
        self.assertIsNone(handler.celery_app)
        mock_logger.error.assert_called_with("Celery error")

    @patch("omni.pro.webhook.webhook_handler.threading.Thread.start")
    @patch("omni.pro.webhook.webhook_handler.WebhookHandler.resolve_interface")
    def test_start_thread(self, mock_resolve_interface, mock_thread_start):
        WebhookHandler.start_thread(self.crud_attrs, self.context)

        mock_thread_start.assert_called_once()

    @patch("omni.pro.webhook.webhook_handler._logger")
    def test_start_thread_no_tenant_or_type_db(self, mock_logger):
        invalid_context = {"user": "test_user"}
        WebhookHandler.start_thread(self.crud_attrs, invalid_context)

        mock_logger.error.assert_called_with("Tenant or type db is not defined")

    def test_resolve_interface_document(self):
        self.handler.redis_manager = RedisManager(host="localhost", port=27017, db=0, redis_ssl=False)

        self.handler.context = {"tenant": "test_tenant"}
        self.handler.tenant = "test_tenant"
        self.handler.type_db = "document"

        try:
            self.handler.resolve_interface()
        except Exception as e:
            self.fail(f"resolve_interface raised an exception: {e}")

    @patch("threading.Thread.start")
    @patch("omni.pro.webhook.webhook_handler.WebhookHandler.resolve_interface")
    def test_start_thread(self, mock_resolve_interface, mock_thread_start):
        crud_attrs = {
            "created_attrs": {"some_key": [1, 2, 3]},
        }
        context = {
            "tenant": "test_tenant",
            "type_db": "sql",
        }

        WebhookHandler.start_thread(crud_attrs, context)

        mock_thread_start.assert_called_once()

    @patch("omni.pro.webhook.webhook_handler.WebhookHandler._set_webhooks_by_event_id")
    @patch("omni.pro.webhook.webhook_handler.WebhookHandler._set_event_by_code")
    @patch("omni.pro.webhook.webhook_handler.WebhookHandler._send_webhooks")
    @patch("time.sleep", return_value=None)
    def test_process_and_dispatch_webhooks(self, mock_sleep, mock_send_webhooks, mock_set_event, mock_set_webhooks):
        mock_set_event.return_value = True
        mock_set_webhooks.return_value = True

        self.handler.event_by_code = {"event_1": "code_1"}

        self.handler.webhooks_by_event_id = {"event_1": ["webhook_1"]}

        self.handler.process_and_dispatch_webhooks()

        mock_sleep.assert_called_once()
        mock_set_event.assert_called_once()
        mock_set_webhooks.assert_called_once()
        mock_send_webhooks.assert_called_once()

    @patch("omni.pro.webhook.webhook_handler.WebhookHandler._send_notification_webhook_records")
    @patch("omni.pro.webhook.webhook_handler.WebhookHandler._send_external_webhook_records")
    def test_resend_webhook_entry(self, mock_send_external, mock_send_notification):
        webhook_entry = {"webhook": {"type_webhook": "notification"}}
        self.handler.resend_webhook_entry(webhook_entry)

        mock_send_notification.assert_called_once()

        webhook_entry["webhook"]["type_webhook"] = "external"
        self.handler.resend_webhook_entry(webhook_entry)

        mock_send_external.assert_called_once()

    def test_create_celery_task(self):
        webhook_entry = {"webhook": {"name": "test_webhook", "priority_level": 2}, "records": [1, 2, 3]}

        self.handler._create_celery_task(webhook_entry)

        self.handler.celery_app.send_task.assert_called_once_with(
            name="retry_send_webhook",
            args=[webhook_entry, self.handler.context],
            kwargs={"name": "test_webhook", "records_count": 3},
            queue="high",
        )

    def test_resolve_interface_sql(self):
        self.context = {"tenant": "test_tenant", "type_db": "sql"}

        handler = WebhookHandler(self.crud_attrs, self.context)

        try:
            handler.resolve_interface()
        except Exception as e:
            self.fail(f"resolve_interface raised an exception: {e}")

    @patch.object(WebhookHandler, "_send_records_to_mirror_model")
    @patch.object(WebhookHandler, "_send_external_webhook_records")
    @patch.object(WebhookHandler, "_send_notification_webhook_records")
    def test_resend_webhook_entry(self, mock_send_notification, mock_send_external, mock_send_mirror):
        handler = WebhookHandler({}, {"tenant": "test_tenant", "user": "test_user"})

        webhook_entry = {"model_mirror": {"some_key": "some_value"}}
        handler.resend_webhook_entry(webhook_entry)
        mock_send_mirror.assert_called_once_with(webhook_entry, timeout=0)

        webhook_entry = {"webhook": {"type_webhook": "external"}}
        handler.resend_webhook_entry(webhook_entry)
        mock_send_external.assert_called_once_with(webhook_entry, timeout=0)

        webhook_entry["webhook"]["type_webhook"] = "notification"
        handler.resend_webhook_entry(webhook_entry)
        mock_send_notification.assert_called_once_with(webhook_entry, timeout=0)

    def test_resend_webhook_entry_undefined_context(self):
        handler = WebhookHandler({}, {})
        webhook_entry = {}

        with self.assertRaises(Exception) as context:
            handler.resend_webhook_entry(webhook_entry)

        self.assertEqual(str(context.exception), "Undefined context")

    @patch("omni_pro_grpc.grpc_function.TemplateNotificationRPCFucntion.template_notification_render")
    @patch.object(WebhookHandler, "_send_external_webhook_records")
    @patch.object(WebhookHandler, "_create_celery_task")
    def test_send_notification_webhook_records(self, mock_create_task, mock_send_external, mock_rpc_template):
        handler = WebhookHandler({}, {"tenant": "test_tenant"})
        webhook_entry = {
            "webhook": {"template_notification": {"id": "test_template"}},
            "records": [{"id": 1}, {"id": 2}],
        }

        mock_rpc_template.return_value = {
            "response_standard": {"success": True},
            "render": {1: "rendered_data_1", 2: "rendered_data_2"},
        }
        handler._send_notification_webhook_records(webhook_entry)
        mock_send_external.assert_called_once()

        mock_rpc_template.return_value = {"response_standard": {"success": False, "message": "Some error"}}
        handler.send_to_queue = True
        handler._send_notification_webhook_records(webhook_entry)
        mock_create_task.assert_called_once()

    def test_send_notification_webhook_no_template(self):
        handler = WebhookHandler({}, {"tenant": "test_tenant"})
        webhook_entry = {"webhook": {}, "records": [{"id": 1}, {"id": 2}]}

        with self.assertRaises(Exception) as context:
            handler._send_notification_webhook_records(webhook_entry)

        self.assertEqual(str(context.exception), "Webhook without template_notification")

    def test_sort_webhooks_by_priority_level(self):
        handler = WebhookHandler({}, {"tenant": "test_tenant"})

        handler.internal_webhook_records = [
            {"webhook": {"priority_level": 2}},
            {"webhook": {"priority_level": 1}},
        ]
        handler.external_webhook_records = [
            {"webhook": {"priority_level": 3}},
            {"webhook": {"priority_level": 2}},
        ]
        handler.notification_webhook_records = [
            {"webhook": {"priority_level": 4}},
            {"webhook": {"priority_level": 1}},
        ]

        handler._sort_webhooks_by_priority_level()

        self.assertEqual(handler.internal_webhook_records[0]["webhook"]["priority_level"], 1)
        self.assertEqual(handler.external_webhook_records[0]["webhook"]["priority_level"], 2)
        self.assertEqual(handler.notification_webhook_records[0]["webhook"]["priority_level"], 1)

    @patch("omni_pro_base.http_request.OmniRequest.make_request")
    @patch.object(WebhookHandler, "_create_celery_task")
    def test_send_external_webhook_records(self, mock_create_task, mock_make_request):
        handler = WebhookHandler({}, {"tenant": "test_tenant"})
        webhook_entry = {
            "webhook": {"url": "http://example.com", "method": "POST", "auth_type": "Bearer", "auth": "token"},
            "records": [{"id": 1}, {"id": 2}],
        }

        mock_make_request.return_value = MagicMock(status_code=200)
        handler._send_external_webhook_records(webhook_entry)
        mock_make_request.assert_called_once()

        mock_make_request.side_effect = requests.exceptions.RequestException("Error")
        handler.send_to_queue = True
        handler._send_external_webhook_records(webhook_entry)
        mock_create_task.assert_called_once()

    def test_send_external_webhook_no_queue(self):
        handler = WebhookHandler({}, {"tenant": "test_tenant"})
        webhook_entry = {"webhook": {"url": "http://example.com", "method": "POST"}, "records": [{"id": 1}, {"id": 2}]}

        with self.assertRaises(Exception) as context:
            handler._send_external_webhook_records(webhook_entry)

        self.assertIn("Tipo de autenticación no soportado", str(context.exception))

    @patch("omni.pro.webhook.webhook_handler.MirrorModelRPCFucntion.multi_update_model")
    def test_send_records_to_mirror_model(self, mock_multi_update_model):
        handler = WebhookHandler({}, {"tenant": "test_tenant"})

        webhook_entry = {
            "event": {"operation": "update"},
            "model_mirror": {"microservice": "test_service", "class_name": "test_class"},
            "records": [{"id": 1}, {"id": 2}],
        }

        mock_multi_update_model.return_value = {"response_standard": {"success": True}}

        result = handler._send_records_to_mirror_model(webhook_entry)

        mock_multi_update_model.assert_called_once()
        self.assertTrue(result)

        mock_multi_update_model.return_value = {"response_standard": {"success": False, "message": "Error"}}
        with self.assertRaises(Exception):
            handler._send_records_to_mirror_model(webhook_entry)

    @patch("omni.pro.webhook.webhook_handler.WebhookHandler._set_instances_by_model_name_and_id")
    def test_configure_webhook_records_by_operation(self, mock_set_instances):
        handler = WebhookHandler({}, {"tenant": "test_tenant"})

        handler.event_by_code = {"test_model_create": {"operation": "create", "id": 1}}
        handler.webhooks_by_event_id = {1: [{"type_webhook": "internal", "trigger_fields": None}]}
        handler.instances_by_model_name_and_id = {"test_model": {1: MagicMock(id=1)}}

        operation_attrs = {"test_model": {1: {"field1"}}}

        handler._configure_webhook_records_by_operation(operation_attrs, "create")

        self.assertEqual(len(handler.internal_webhook_records), 1)

    @patch("omni.pro.webhook.webhook_handler.OmniRequest.make_request")
    def test_send_external_webhook_records(self, mock_make_request):
        handler = WebhookHandler({}, {"tenant": "test_tenant"})

        webhook_entry = {
            "webhook": {"url": "http://example.com", "method": "POST", "auth_type": None, "auth": None},
            "records": [{"id": 1}, {"id": 2}],
        }

        mock_make_request.return_value.status_code = 200

        result = handler._send_external_webhook_records(webhook_entry)

        mock_make_request.assert_called_once_with(
            "http://example.com",
            "POST",
            json=[{"id": 1}, {"id": 2}],
            tipo_auth=None,
            auth_params=None,
            timeout=handler.timeout_external,
        )
        self.assertTrue(result)

        mock_make_request.side_effect = Exception("Request Error")
        with self.assertRaises(Exception):
            handler._send_external_webhook_records(webhook_entry)

    @patch("omni.pro.webhook.webhook_handler.json_format.MessageToDict")
    def test_get_records_from_proto(self, mock_message_to_dict):
        instance_mock = MagicMock()
        instance_mock.to_proto.return_value = "proto_instance"
        mock_message_to_dict.return_value = {"converted_record": "value"}

        instances_by_id = {"1": instance_mock}
        records = [{"id": "1"}]

        result = self.handler._get_records_from_proto(records, instances_by_id)

        self.assertEqual(result, [{"converted_record": "value"}])
        instance_mock.to_proto.assert_called_once()
        mock_message_to_dict.assert_called_once_with("proto_instance", preserving_proto_field_name=True)

    def test_transforms_model_mirror_records(self):
        model_mirror = {
            "persistence_type": "SQL",
            "fields": [
                {"code": "field1", "field_aliasing": "alias1"},
                {"code": "field2", "field_aliasing": "alias2"},
                {"code": "field3", "field_aliasing": "alias3"},
            ],
        }

        records = [
            {"alias1": "value1", "alias2": "value2", "alias3": "value3"},
            {"alias1": "value4", "alias2": "value5", "alias3": "value6"},
        ]

        with patch.object(self.handler, "_get_field_aliasing_in_mirror_model", return_value=True), patch.object(
            self.handler, "_get_fields_in_mirror_model", return_value=model_mirror["fields"]
        ):
            result = self.handler._transforms_model_mirror_records(model_mirror, records)

        expected = [
            {
                "field1": "value1",
                "field2": "value2",
                "field3": "value3",
                "tenant": "test_tenant",
                "updated_by": "test_user",
                "created_by": "test_user",
            },
            {
                "field1": "value4",
                "field2": "value5",
                "field3": "value6",
                "tenant": "test_tenant",
                "updated_by": "test_user",
                "created_by": "test_user",
            },
        ]

        self.assertEqual(result, expected)

    def test_get_fields_in_mirror_model(self):
        model_mirror = {
            "fields": [
                {"code": "field1", "field_aliasing": "alias1"},
                {"code": "field2", "field_aliasing": "alias2"},
                {"code": "field3.with_dot", "field_aliasing": "alias3"},
            ]
        }

        result = self.handler._get_fields_in_mirror_model(model_mirror)
        expected = [{"code": "field1", "field_aliasing": "alias1"}, {"code": "field2", "field_aliasing": "alias2"}]

        self.assertEqual(result, expected)

    def test_get_field_aliasing_in_mirror_model(self):
        model_mirror = {
            "fields": [
                {"code": "field1", "field_aliasing": "alias1"},
                {"code": "field2", "field_aliasing": "id"},
                {"code": "field3", "field_aliasing": "code"},
            ]
        }

        with patch.object(self.handler, "_get_fields_in_mirror_model", return_value=model_mirror["fields"]):
            result = self.handler._get_field_aliasing_in_mirror_model(model_mirror)

        expected = {"code": "field2", "field_aliasing": "id"}
        self.assertEqual(result, expected)

    @patch("omni.pro.webhook.webhook_handler.WebhookHandler._get_field_aliasing_in_mirror_model")
    @patch("omni.pro.webhook.webhook_handler.WebhookHandler._get_fields_in_mirror_model")
    def test_transforms_model_mirror_records_nosql(
        self, mock_get_fields_in_mirror_model, mock_get_field_aliasing_in_mirror_model
    ):
        model_mirror = {
            "persistence_type": "NO_SQL",
            "fields": [{"code": "field1", "field_aliasing": "alias1"}, {"code": "field2", "field_aliasing": "alias2"}],
        }

        records = [{"alias1": "value1", "alias2": "value2"}]

        mock_get_fields_in_mirror_model.return_value = model_mirror["fields"]
        mock_get_field_aliasing_in_mirror_model.return_value = True

        result = self.handler._transforms_model_mirror_records(model_mirror, records)

        expected = [{"field1": "value1", "field2": "value2", "context": {"tenant": "test_tenant", "user": "test_user"}}]

        self.assertEqual(result, expected)

    def test_set_instances_by_model_name_and_id(self):
        mock_model = MagicMock()
        mock_instance1 = MagicMock(id=1)
        mock_instance2 = MagicMock(id=2)
        self.handler.session.query.return_value.filter.return_value.all.return_value = [mock_instance1, mock_instance2]
        self.handler.class_by_name["TestModel"] = mock_model

        self.handler.created_attrs = {"TestModel": {1: "attrs1", 2: "attrs2"}}
        self.handler._set_instances_by_model_name_and_id()

        expected = {"TestModel": {1: mock_instance1, 2: mock_instance2}}
        self.assertEqual(self.handler.instances_by_model_name_and_id, expected)

    def test_instances_convert_datetime_fields_to_iso(self):
        instances = [
            {"field1": datetime(2024, 1, 1), "field2": "value"},
            {"field1": "no date", "field2": datetime(2024, 2, 1)},
        ]
        result = self.handler._instances_convert_datetime_fields_to_iso(instances)
        expected = [
            {"field1": "2024-01-01T00:00:00", "field2": "value"},
            {"field1": "no date", "field2": "2024-02-01T00:00:00"},
        ]
        self.assertEqual(result, expected)

    @patch("omni.pro.webhook.webhook_handler._logger")  # Reemplaza con la ruta correcta
    def test_set_webhooks_by_event_id(self, mock_logger):
        self.handler.rpc_webhook.read_webhook.return_value = (MagicMock(webhooks=[]), True, None)
        self.handler._set_webhooks_by_event_id()
        self.handler.rpc_webhook.read_webhook.assert_called_once()
        self.assertEqual(self.handler.webhooks_by_event_id, {})

    @patch("omni.pro.webhook.webhook_handler._logger")  # Reemplaza con la ruta correcta
    def test_set_webhooks_by_event_id_error(self, mock_logger):
        self.handler.rpc_webhook.read_webhook.side_effect = Exception("Error")
        self.handler._set_webhooks_by_event_id()
        mock_logger.error.assert_called_with("_set_webhooks_by_event_id: Error")

    @patch("omni.pro.webhook.webhook_handler._logger")  # Reemplaza con la ruta correcta
    def test_set_event_by_code(self, mock_logger):
        self.handler.rpc_event.read_event.return_value = (MagicMock(events=[]), True, None)
        self.handler._set_event_by_code()
        self.handler.rpc_event.read_event.assert_called_once()
        self.assertEqual(self.handler.event_by_code, {})

    @patch("omni.pro.webhook.webhook_handler._logger")  # Reemplaza con la ruta correcta
    def test_set_event_by_code_error(self, mock_logger):
        self.handler.rpc_event.read_event.side_effect = Exception("Error")
        self.handler._set_event_by_code()
        mock_logger.error.assert_called_with("_set_event_by_code: Error")

    @patch("omni.pro.webhook.webhook_handler._logger")  # Reemplaza con la ruta correcta
    def test_set_models_mirror_by_code(self, mock_logger):
        self.handler.rpc_model.read_model.return_value = (MagicMock(models=[]), True, None)
        self.handler._set_models_mirror_by_code()
        self.handler.rpc_model.read_model.assert_called_once()
        self.assertEqual(self.handler.models_mirror_by_code, {})

    @patch("omni.pro.webhook.webhook_handler._logger")  # Reemplaza con la ruta correcta
    def test_set_models_mirror_by_code_error(self, mock_logger):
        self.handler.rpc_model.read_model.side_effect = Exception("Error")
        self.handler._set_models_mirror_by_code()
        mock_logger.error.assert_called_with("_set_models_mirror_by_code: Error")


if __name__ == "__main__":
    unittest.main()
