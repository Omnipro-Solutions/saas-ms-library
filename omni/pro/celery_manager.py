from celery import Celery
from omni.pro.redis import RedisManager
from omni_pro_base.config import Config


class RedisCeleryQueueManager(object):
    def __init__(self, tenant: str):
        self.tenant = tenant
        self.redis_manager = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        self.celery_app = self._setup_celery()

    def _setup_celery(self):
        conf = self.redis_manager.get_resource_config(service_id=Config.SAAS_REDIS_CELERY, tenant_code=self.tenant)
        if not conf:
            raise Exception("Redis Celery configuration not found")

        app = Celery(
            "tasks",
            broker=f"redis://{conf['host']}:{conf['port']}/{conf['db']}",
            backend=f"redis://{conf['host']}:{conf['port']}/{conf['db']}",
        )
        return app

    def send_task(self):
        pass
