import re
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
from omni.pro.response import MessageResponse
from omni.pro.user.access import INTERNAL_USER, Permission
from omni.pro.util import Resource
from omni_pro_base.util import nested
from omni_pro_grpc.common.base_pb2 import Filter
from omni_pro_grpc.v1.users import user_pb2

logger = configure_logger(name=__name__)


def resources_decorator(
    resource_list: list, permission: bool = True, message_response=None, permission_code: str = None
) -> callable:
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
            if not request.context.user == INTERNAL_USER:
                if permission:
                    message_responses = message_response or funcion.__annotations__.get("return")
                    result = permission_required(redis_manager, request, funcion, message_responses, permission_code)
                    if result:
                        return result
            c = funcion(instance, request, context)
            return c

        return inner

    return decorador_func


def permission_required(rm: RedisManager, request, funcion: callable, message_response, permission_code: str):
    try:
        permission = permission_code or convert_name_upper_snake_case(
            funcion.__name__, funcion.__module__.split(".")[-1].upper()
        )
        config = rm.get_resource_config(Config.SAAS_MS_USER, request.context.tenant)
        rds_conn = nested(config, "dbs.redis")
        rm_per = RedisManager(**rds_conn)
        sub = request.context.user
        domain_val, is_superuser_val = rm_per.get_multi_hash(sub, permission, Permission.IS_SUPERUSER.value)
        if domain_val is None and is_superuser_val is None:
            return MessageResponse(message_response).unauthorized_response()

        if hasattr(request, "filter") and hasattr(request.filter, "filter"):
            filter_exist = str(request.filter.filter)
            filter_domain = domain_val

            if filter_exist and filter_domain:
                filter_exist = filter_exist.replace("]", "").replace("[", "")
                filter_domain = filter_domain.replace("[", "").replace("]", "")
                str_filter = f"['and', {filter_exist}, {filter_domain}]"
            else:
                str_filter = filter_exist or filter_domain

            request_filter = Filter(filter=str_filter)
            request.filter.CopyFrom(request_filter)

    except Exception as e:
        LoggerTraceback.error("Permission required decorator exception", e, logger)
        return MessageResponse(message_response).internal_response(message="Permission required decorator exception")


def convert_name_upper_snake_case(function_name: str, model_name: str) -> str:
    snake = re.sub(r"([A-Z])", r"_\1", function_name).lower()
    # Eliminar el guión bajo inicial si existe y convertir todo a mayúsculas
    snake_case = (snake[1:] if snake.startswith("_") else snake).upper()
    components = snake_case.split("_")

    # Identificar la acción y el modelo
    if set(model_name.split("_")).intersection(set(components)):
        resul = [component for component in components if component not in model_name.split("_")]
        action = "_".join(resul)
        return f"CAN_{model_name}_{action}".upper()
    return f"CAN_{snake_case}".upper()


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
