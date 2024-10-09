import unittest
from unittest.mock import patch

import mongoengine as mongo
from omni.pro.database_connection import RedisManager, ms_register_connection, register_logger_connection
from omni_pro_base.config import Config


class TestRegisterLoggerConnection(unittest.TestCase):

    @patch("omni.pro.database_connection.mongo.register_connection")
    @patch.object(RedisManager, "get_mongodb_config")
    def test_register_logger_connection(self, mock_get_mongodb_config, mock_register_connection):
        mock_get_mongodb_config.return_value = {
            "name": "test_db",
            "host": "localhost",
            "port": "27017",
            "user": "test_user",
            "password": "test_pass",
            "complement": {},
        }

        Config.SERVICE_ID = "saas-loggers-oms"

        manager = RedisManager(host="localhost", port="6379", db="0", redis_ssl=False)

        register_logger_connection("test_tenant", manager)

        mock_get_mongodb_config.assert_called_once_with(Config.SERVICE_ID, "test_tenant")

        mock_register_connection.assert_called_once_with(
            alias="test_tenant_test_db",
            name="test_db",
            host="localhost",
            port=27017,
            username="test_user",
            password="test_pass",
            **{}
        )


class TestMsRegisterConnection(unittest.TestCase):

    @patch("omni.pro.database_connection.mongo.register_connection")
    @patch("omni.pro.database_connection.register_logger_connection")
    @patch.object(RedisManager, "get_mongodb_config")
    @patch.object(RedisManager, "get_tenant_codes")
    def test_ms_register_connection(
        self, mock_get_tenant_codes, mock_get_mongodb_config, mock_register_logger_connection, mock_register_connection
    ):
        mock_get_tenant_codes.return_value = ["tenant1", "tenant2"]

        mock_get_mongodb_config.return_value = {
            "name": "test_db",
            "host": "localhost",
            "port": "27017",
            "user": "test_user",
            "password": "test_pass",
            "complement": {},
        }

        ms_register_connection(logger_oms=True)

        mock_get_tenant_codes.assert_called_once()

        self.assertEqual(mock_get_mongodb_config.call_count, 2)

        self.assertEqual(mock_register_connection.call_count, 3)

        self.assertEqual(mock_register_logger_connection.call_count, 2)

        mock_register_connection.assert_any_call(
            alias="tenant1_test_db",
            name="test_db",
            host="localhost",
            port=27017,
            username="test_user",
            password="test_pass",
            **{}
        )

        mock_register_connection.assert_any_call(
            alias="tenant2_test_db",
            name="test_db",
            host="localhost",
            port=27017,
            username="test_user",
            password="test_pass",
            **{}
        )

        mock_register_connection.assert_any_call(
            alias=mongo.DEFAULT_CONNECTION_NAME,
            name=mongo.DEFAULT_CONNECTION_NAME,
            host="localhost",
            port=27017,
            username="test_user",
            password="test_pass",
            **{}
        )


if __name__ == "__main__":
    unittest.main()
