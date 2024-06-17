import threading
import time
from functools import wraps
from queue import Empty, Queue

from newrelic.api.function_trace import function_trace
from omni.pro.aws import AWSCognitoClient, AWSS3Client
from omni.pro.config import Config
from omni.pro.database import DatabaseManager, PostgresDatabaseManager
from omni.pro.logger import LoggerTraceback, configure_logger
from omni.pro.redis import RedisManager
from omni.pro.util import Resource

logger = configure_logger(name=__name__)


def resources_decorator(resource_list: list) -> callable:
    def decorador_func(funcion: callable) -> callable:
        @function_trace(name=funcion.__name__)
        @wraps(funcion)
        def inner(instance, request, context):
            try:
                redis_manager = RedisManager(
                    host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB, redis_ssl=Config.REDIS_SSL
                )
                context.redis_manager = redis_manager
                if Resource.AWS_COGNITO in resource_list:
                    cognito_params = redis_manager.get_aws_cognito_config(Config.SERVICE_ID, request.context.tenant)
                    # logger.info(f"Cognito params: {cognito_params}")
                    context.cognito_client = AWSCognitoClient(**cognito_params)
                if Resource.AWS_S3 in resource_list:
                    s3_params = redis_manager.get_aws_s3_config(Config.SERVICE_ID, request.context.tenant)
                    # logger.info(f"S3 params: {s3_params}")
                    context.s3_client = AWSS3Client(**s3_params)
                if Resource.MONGODB in resource_list:
                    # logger.info(f"Tenant: {request.context.tenant}, Service ID: {Config.SERVICE_ID}")
                    db_params = redis_manager.get_mongodb_config(Config.SERVICE_ID, request.context.tenant)
                    context.db_name = f"{request.context.tenant}_{db_params.get('name')}"
                    db_params["db"] = db_params.pop("name")
                    # logger.info(f"MongoDB params: {db_params}")
                    context.db_manager = DatabaseManager(**db_params)
                if Resource.POSTGRES in resource_list:
                    # logger.info(f"Tenant: {request.context.tenant}, Service ID: {Config.SERVICE_ID}")
                    db_params = redis_manager.get_postgres_config(Config.SERVICE_ID, request.context.tenant)
                    context.db_name = db_params.get("name")
                    context.pg_db_params = db_params
                    # logger.info(f"Postgres params: {db_params}")
                    context.pg_manager = PostgresDatabaseManager(**db_params)
            except Exception as e:
                LoggerTraceback.error("Resource Decorator exception", e, logger)
            c = funcion(instance, request, context)
            return c

        return inner

    return decorador_func


class FunctionThreadController:
    def __init__(self, timeout=Config.TIMEOUT_THREAD_CONTROLLER):
        self.timeout = timeout
        self.function_threads = {}

    def _worker(self, function_name, queue):
        while True:
            try:
                target, args, kwargs = queue.get(timeout=self.timeout)
                target(*args, **kwargs)
                queue.task_done()
            except Empty:
                with self.function_threads[function_name]["lock"]:
                    if time.time() - self.function_threads[function_name]["last_activity"] >= self.timeout:
                        self.function_threads[function_name]["thread"] = None
                        break

    def run_thread_controller(self, target):
        function_name = target.__name__

        @wraps(target)
        def wrapper(*args, **kwargs):
            if function_name not in self.function_threads:
                self.function_threads[function_name] = {
                    "queue": Queue(),
                    "lock": threading.Lock(),
                    "last_activity": time.time(),
                    "thread": None,
                }

            function_info = self.function_threads[function_name]

            with function_info["lock"]:
                function_info["last_activity"] = time.time()
                if function_info["thread"] is None or not function_info["thread"].is_alive():
                    function_info["thread"] = threading.Thread(
                        target=self._worker,
                        args=(function_name, function_info["queue"]),
                        name=f"Thread-Func-{function_name}-Worker",
                    )
                    function_info["thread"].start()
                function_info["queue"].put((target, args, kwargs))

        return wrapper


function_thread_controller = FunctionThreadController(timeout=Config.TIMEOUT_THREAD_CONTROLLER)
