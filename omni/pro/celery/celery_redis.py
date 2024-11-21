import redis
from celery import Celery
from omni.pro.redis import RedisManager
from omni_pro_base.config import Config


class OmniCelery(Celery):
    def __init__(self, tenant: str, **kwargs) -> None:
        self.tenant = tenant
        self.conf = self._get_conf()
        if not all(k in kwargs for k in ["broker", "backend"]):
            broker = f"redis://{self.conf['host']}:{self.conf['port']}/{self.conf['db']}"
            backend = f"redis://{self.conf['host']}:{self.conf['port']}/{self.conf['db']}"

        kwargs["broker"] = kwargs.get("broker", broker)
        kwargs["backend"] = kwargs.get("backend", backend)
        kwargs["main"] = "tasks"
        super().__init__(**kwargs)
        self.app: Celery = self._get_app()

    def get_queue_with_min_tasks(self, queues: list[str] = ["critical", "high", "medium", "low", "very_low"]) -> str:
        """
        Determines which queue has the fewest tasks and returns the name of that queue.

        Args:
            queues (list[str]): A list of queue names to check. Defaults to a list of priority-based queues:
                                ["critical", "high", "medium", "low", "very_low"].

        Returns:
            str: The name of the queue with the fewest tasks.

        """
        redis_client = redis.Redis(host=self.conf["host"], port=self.conf["port"], db=self.conf["db"])
        min_tasks = float("inf")
        selected_queue = None

        for queue in queues:
            len_tasks: int = redis_client.llen(queue)
            if len_tasks < min_tasks:
                min_tasks = len_tasks
                selected_queue = queue

        return selected_queue

    def _get_conf(self):
        redis_manager = RedisManager(
            host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
        )
        conf = redis_manager.get_resource_config(service_id=Config.SAAS_REDIS_CELERY, tenant_code=self.tenant)
        if not conf:
            raise Exception("Redis Celery configuration not found")
        return conf

    def _get_app(self) -> Celery:
        return self


# TODO: Remove this alias in the future
CeleryRedis = OmniCelery
