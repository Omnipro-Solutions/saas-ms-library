import unittest
from pathlib import Path
from unittest.mock import ANY, MagicMock, mock_open, patch

from omni.pro.initial import Event, LoadData, Manifest, ManifestRPCFunction, MicroserviceProto, UserChannel


class TestLoadData(unittest.TestCase):

    def setUp(self):
        self.base_app = Path("/path/to/base/app")
        self.microservice = "test_microservice"
        self.persistence_type = "NO_SQL"
        self.load_data_instance = LoadData(self.base_app, self.microservice, self.persistence_type)

    @patch("omni.pro.initial.RedisManager")
    @patch("omni.pro.initial.Config")
    @patch.object(LoadData, "get_rpc_manifest_func_class")
    @patch("google.protobuf.json_format.MessageToDict")
    def test_load_data(self, mock_message_to_dict, mock_get_rpc_func, mock_config, mock_redis_manager):
        mock_redis = MagicMock()
        mock_redis_manager.return_value = mock_redis

        mock_redis.get_tenant_codes.return_value = ["tenant1", "tenant2"]
        mock_redis.get_user_admin.side_effect = [{"id": "admin1"}, {"id": "admin2"}]
        mock_redis.get_postgres_config.return_value = {"name": "pg_db_name"}
        mock_redis.get_mongodb_config.return_value = {"name": "mongo_db_name"}

        mock_microservice_proto = MagicMock()
        mock_get_rpc_func.return_value.return_value.get_micro.return_value = MagicMock()

        mock_message_to_dict.return_value = {"code": "test_code", "data": []}

        self.load_data_instance.load_data()

        self.assertEqual(mock_message_to_dict.call_count, 2)

        calls = mock_message_to_dict.call_args_list
        self.assertIsInstance(calls[0][0][0], MagicMock)
        self.assertIsInstance(calls[1][0][0], MagicMock)

    @patch("omni.pro.initial.UserChannel")
    @patch.object(LoadData, "load_data_dict")
    def test_create_user_admin(self, mock_load_data_dict, mock_user_channel):
        context = {"tenant": "test_tenant", "user": "admin_user"}
        mock_rc = MagicMock()

        mock_load_data_dict.return_value = [{"id": "user1", "username": "admin"}]

        mock_user_channel.return_value.create_users.return_value = (
            MagicMock(user=MagicMock(id="user1", username="admin")),
            True,
        )

        response, success = self.load_data_instance.create_user_admin(context, mock_rc)

        mock_user_channel.return_value.create_users.assert_called_once_with(mock_load_data_dict.return_value)

        mock_rc.json().set.assert_called_once_with(
            context.get("tenant"), "$.user_admin", {"id": response.user.id, "username": response.user.username}
        )
        self.assertTrue(success)

    @patch("builtins.open", new_callable=mock_open, read_data="id;name\n1;admin\n2;user")
    def test_load_data_dict(self, mock_file):
        file_path = Path("/path/to/file.csv")

        result = list(self.load_data_instance.load_data_dict(file_path))

        expected_result = [{"id": "1", "name": "admin"}, {"id": "2", "name": "user"}]
        self.assertEqual(result, expected_result)
        mock_file.assert_called_once_with(file_path, mode="r", encoding="utf-8-sig")

    @patch("omni.pro.initial.PostgresDatabaseManager")
    @patch.object(LoadData, "csv_to_class")
    def test_load_data_model(self, mock_csv_to_class, mock_pg_manager):
        db_pg_params = {"name": "test_db"}
        context = {"user": "admin", "tenant": "test_tenant"}
        file_path = "path/to/csv"
        model_str = "TestModel"
        mock_modulo = MagicMock()

        mock_model = MagicMock()
        setattr(mock_modulo, model_str, mock_model)

        self.load_data_instance.load_data_model(db_pg_params, context, file_path, mock_modulo, model_str)

        mock_pg_manager.assert_called_once_with(**db_pg_params)
        mock_csv_to_class.assert_called_once_with(
            file_path,
            mock_model,
            created_by="admin",
            updated_by="admin",
            created_at=ANY,
            updated_at=ANY,
            tenant="test_tenant",
        )

    @patch("omni.pro.initial.ExitStackDocument")
    @patch.object(LoadData, "csv_to_class")
    def test_load_data_document(self, mock_csv_to_class, mock_exit_stack):
        context = {"user": "admin", "tenant": "test_tenant"}
        file_path = "path/to/csv"
        db_alias = "tenant_db"
        model_str = "TestDocument"
        mock_modulo = MagicMock()

        mock_doc_class = MagicMock()
        setattr(mock_modulo, model_str, mock_doc_class)

        self.load_data_instance.load_data_document(context, file_path, db_alias, mock_modulo, model_str)

        mock_exit_stack.assert_called_once_with(
            mock_doc_class.reference_list(), db_alias=db_alias, use_doc_classes=True
        )
        mock_csv_to_class.assert_called_once_with(file_path, mock_doc_class, context=context, audit=ANY)


class TestManifest(unittest.TestCase):

    def setUp(self):
        self.base_app = Path("/fake/path")
        self.manifest_instance = Manifest(self.base_app)

    @patch("builtins.open", new_callable=mock_open, read_data="{'key': 'value'}")
    @patch("pathlib.Path.exists", return_value=True)
    def test_get_manifest(self, mock_exists, mock_open_file):
        result = self.manifest_instance.get_manifest()

        mock_exists.assert_called_once_with()
        mock_open_file.assert_called_once_with(self.base_app / "__manifest__.py", "r")

        self.assertEqual(result, {"key": "value"})

    @patch("builtins.open", new_callable=mock_open, read_data="{'key': 'value'}")
    @patch("pathlib.Path.exists", return_value=False)
    def test_get_manifest_file_not_found(self, mock_exists, mock_open_file):
        result = self.manifest_instance.get_manifest()

        mock_exists.assert_called_once_with()
        mock_open_file.assert_not_called()

        self.assertEqual(result, {})

    @patch("omni.pro.initial.MicroServicePathValidator.load", return_value="validated_data")
    @patch("omni.pro.initial.Manifest.get_manifest", return_value={"code": "test_code"})
    def test_validate_manifest(self, mock_get_manifest, mock_validator_load):
        context = {"tenant": "test_tenant", "user": "admin"}
        micro_data = [{"data": "value"}]
        micro_settings = [{"settings": "value"}]

        result = self.manifest_instance.validate_manifest(context, {}, micro_data, micro_settings)

        mock_get_manifest.assert_called_once()
        mock_validator_load.assert_called_once_with(
            {"code": "test_code", "context": context}, micro_data=micro_data, micro_settings=micro_settings
        )

        self.assertEqual(result, "validated_data")


class TestManifestRPCFunction(unittest.TestCase):

    def setUp(self):
        self.context = {"tenant": "test_tenant", "user": "admin"}
        self.manifest_rpc = ManifestRPCFunction(self.context)

    @patch("omni.pro.initial.GRPClient")
    @patch.object(Event, "update")
    def test_load_manifest(self, mock_event_update, mock_grpc_client):
        mock_response = MagicMock()
        mock_response.microservice.code = "test_microservice"
        mock_grpc_client.return_value.call_rpc_fuction.return_value = (mock_response, True)

        params = {"param1": "value1"}

        response = self.manifest_rpc.load_manifest(params)

        mock_event_update.assert_called_once_with(
            rpc_method="MicroserviceCreate",
            request_class="MicroserviceCreateRequest",
            params={"param1": "value1", "context": self.context},
        )

        mock_grpc_client.return_value.call_rpc_fuction.assert_called_once_with(self.manifest_rpc.event)

        self.assertEqual(response, mock_response)

    @patch("omni.pro.initial.GRPClient")
    @patch.object(Event, "update")
    def test_get_micro(self, mock_event_update, mock_grpc_client):
        mock_response = MagicMock()
        mock_response.microservices = [MicroserviceProto()]
        mock_grpc_client.return_value.call_rpc_fuction.return_value = (mock_response, True)

        micro = self.manifest_rpc.get_micro("test_code")

        mock_event_update.assert_called_once_with(
            rpc_method="MicroserviceRead",
            request_class="MicroserviceReadRequest",
            params={"filter": {"filter": "[('code','=','test_code')]"}, "context": self.context},
        )

        mock_grpc_client.return_value.call_rpc_fuction.assert_called_once_with(self.manifest_rpc.event)

        self.assertIsInstance(micro, MicroserviceProto)

    @patch("omni.pro.initial.GRPClient")
    @patch.object(Event, "update")
    def test_update_micro(self, mock_event_update, mock_grpc_client):
        mock_response = MagicMock()
        mock_response.microservice.code = "test_microservice"
        mock_grpc_client.return_value.call_rpc_fuction.return_value = (mock_response, True)

        params = {"param1": "value1"}

        response = self.manifest_rpc.update_micro(params)

        mock_event_update.assert_called_once_with(
            rpc_method="MicroserviceUpdate",
            request_class="MicroserviceUpdateRequest",
            params={"param1": "value1", "context": self.context},
        )

        mock_grpc_client.return_value.call_rpc_fuction.assert_called_once_with(self.manifest_rpc.event)

        self.assertEqual(response, mock_response)


class TestUserChannel(unittest.TestCase):

    def setUp(self):
        self.context = {"tenant": "test_tenant", "user": "admin"}
        self.user_channel = UserChannel(self.context)

    @patch("omni.pro.initial.GRPClient")
    @patch.object(Event, "update")
    def test_create_users(self, mock_event_update, mock_grpc_client):
        mock_response = MagicMock()
        mock_response_user_create = MagicMock()
        mock_response_user_create.user.id = "123"
        mock_response_user_create.user.username = "test_user"
        mock_grpc_client.return_value.call_rpc_fuction.return_value = (mock_response_user_create, True)

        list_value = [
            {
                "email": "test@example.com",
                "name": "Test User",
                "password": "password123",
                "username": "test_user",
                "sub": "test_sub",
            }
        ]

        response, success = self.user_channel.create_users(list_value)

        mock_event_update.assert_called_once_with(
            rpc_method="UserCreate",
            request_class="UserCreateRequest",
            params={
                "context": self.context,
                "email": "test@example.com",
                "email_confirm": "test@example.com",
                "language": {"code": "01", "code_name": "CO"},
                "name": "Test User",
                "password": "password123",
                "password_confirm": "password123",
                "timezone": {"code": "01", "code_name": "CO"},
                "username": "test_user",
                "is_superuser": True,
            },
        )

        mock_grpc_client.return_value.call_rpc_fuction.assert_called_once_with(self.user_channel.event)

        self.assertEqual(response, mock_response_user_create)
        self.assertTrue(success)

    @patch("omni.pro.initial.GRPClient")
    @patch.object(Event, "update")
    def test_create_users_multiple(self, mock_event_update, mock_grpc_client):
        mock_response = MagicMock()
        mock_grpc_client.return_value.call_rpc_fuction.return_value = (mock_response, True)

        list_value = [
            {
                "email": "test1@example.com",
                "name": "Test User 1",
                "password": "password123",
                "username": "test_user1",
                "sub": "test_sub1",
            },
            {
                "email": "test2@example.com",
                "name": "Test User 2",
                "password": "password123",
                "username": "test_user2",
                "sub": "test_sub2",
            },
        ]

        response, success = self.user_channel.create_users(list_value)

        self.assertEqual(mock_event_update.call_count, 2)

        self.assertEqual(mock_grpc_client.return_value.call_rpc_fuction.call_count, 2)

        self.assertEqual(response, mock_response)
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
