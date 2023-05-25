from omni.pro.aws import AWSCloudMap, AWSCognitoClient
from omni.pro.config import Config
from omni.pro.database import DatabaseManager, PostgresDatabaseManager, RedisManager
from omni.pro.logger import LoggerTraceback, configure_logger
from omni.pro.util import Resource

logger = configure_logger(name=__name__)


def resources_decorator(resource_list: list) -> callable:
    def decorador_func(funcion: callable) -> callable:
        def inner(instance, request, context):
            try:
                cloud_map = AWSCloudMap(
                    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
                    region_name=Config.REGION_NAME,
                    service_name=Config.SERVICE_NAME,
                    namespace_name=Config.NAMESPACE_NAME,
                )
                redis_params = cloud_map.get_redis_config()
                redis_manager = RedisManager(**redis_params)
                if Resource.AWS_COGNITO in resource_list:
                    cognito_params = redis_manager.get_aws_cognito_config(Config.SERVICE_ID, request.context.tenant)
                    context.cognito_client = AWSCognitoClient(**cognito_params)
                if Resource.MONGODB in resource_list:
                    db_params = redis_manager.get_mongodb_config(Config.SERVICE_ID, request.context.tenant)
                    # FIXME: remove db_name param from all services, it's not necessary
                    context.db_name = db_params.get("name")
                    db_params["db"] = db_params.pop("name")
                    context.db_manager = DatabaseManager(**db_params)
                if Resource.POSTGRES in resource_list:
                    db_params = redis_manager.get_postgres_config(Config.SERVICE_ID, request.context.tenant)
                    context.db_name = db_params.get("name")
                    context.pg_manager = PostgresDatabaseManager(**db_params)
            except Exception as e:
                LoggerTraceback.error("Resource Decorator exception", e, logger)
            c = funcion(instance, request, context)
            return c

        return inner

    return decorador_func
