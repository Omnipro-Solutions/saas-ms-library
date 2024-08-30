from celery import Celery
from omni.pro.redis import RedisManager
from omni_pro_base.config import Config


class CeleryRedis:
    @classmethod
    def get_celery_app_by_tenant(cls, tenant: str) -> Celery:
        redis_manager = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        conf = redis_manager.get_resource_config(service_id=Config.SAAS_REDIS_CELERY, tenant_code=tenant)
        if not conf:
            raise Exception("Redis Celery configuration not found")
        app = Celery(
            "tasks",
            broker=f"redis://{conf['host']}:{conf['port']}/{conf['db']}",
            backend=f"redis://{conf['host']}:{conf['port']}/{conf['db']}",
        )
        return app
