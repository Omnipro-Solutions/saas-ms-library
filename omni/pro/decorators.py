from omni.pro import redis
from omni.pro.aws import AWSCognitoClient
from omni.pro.config import Config
from omni.pro.database import DatabaseManager, PostgresDatabaseManager
from omni.pro.logger import LoggerTraceback, configure_logger
from omni.pro.util import Resource

logger = configure_logger(name=__name__)


def resources_decorator(resource_list: list) -> callable:
    def decorador_func(funcion: callable) -> callable:
        def inner(instance, request, context):
            try:
                redis_manager = redis.get_redis_manager()
                context.redis_manager = redis_manager
                if Resource.AWS_COGNITO in resource_list:
                    cognito_params = redis_manager.get_aws_cognito_config(Config.SERVICE_ID, request.context.tenant)
                    # logger.info(f"Cognito params: {cognito_params}")
                    context.cognito_client = AWSCognitoClient(**cognito_params)
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
