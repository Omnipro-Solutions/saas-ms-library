import unittest
from unittest.mock import patch

from omni.pro.celery.celery_redis import CeleryRedis


class TestCeleryRedis(unittest.TestCase):

    @patch("omni.pro.celery.celery_redis.Celery", autospec=True)
    @patch("omni.pro.redis.RedisManager.get_resource_config")
    @patch("omni_pro_base.config.Config")
    def test_get_celery_app_by_tenant(self, mock_config, mock_get_resource_config, mock_celery):
        mock_config.REDIS_HOST = "localhost"
        mock_config.REDIS_PORT = 6379
        mock_config.REDIS_DB = 0
        mock_config.REDIS_SSL = False
        mock_config.SAAS_REDIS_CELERY = "saas-redis-celery"

        mock_get_resource_config.return_value = {"host": "localhost", "port": 6379, "db": 1}

        mock_celery_instance = mock_celery.return_value

        tenant = "test_tenant"
        app = CeleryRedis.get_celery_app_by_tenant(tenant)

        mock_get_resource_config.assert_called_once_with(service_id="saas-redis-celery", tenant_code=tenant)

        mock_celery.assert_called_once_with(
            "tasks", broker="redis://localhost:6379/1", backend="redis://localhost:6379/1"
        )

        self.assertEqual(app, mock_celery_instance)

    @patch("omni.pro.redis.RedisManager.get_resource_config")
    def test_get_celery_app_by_tenant_no_config(self, mock_get_resource_config):
        mock_get_resource_config.return_value = None

        tenant = "test_tenant"
        with self.assertRaises(Exception) as context:
            CeleryRedis.get_celery_app_by_tenant(tenant)

        self.assertEqual(str(context.exception), "Redis Celery configuration not found")


if __name__ == "__main__":
    unittest.main()
