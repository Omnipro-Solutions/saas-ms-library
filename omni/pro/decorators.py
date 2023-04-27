from omni.pro.aws import AWSCognitoClient
from omni.pro.config import Config
from omni.pro.database import DatabaseManager, PostgresDatabaseManager, RedisManager
from omni.pro.logger import configure_logger
from omni.pro.util import Resource

logger = configure_logger(name=__name__)


def resources_decorator(resource_list: list) -> callable:
    def decorador_func(funcion: callable) -> callable:
        def inner(instance, request, context):
            try:
                redis_manager = RedisManager(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)
                if Resource.AWS_COGNITO in resource_list:
                    cognito_params = redis_manager.get_aws_cognito_config(Config.SERVICE_ID, request.context.tenant)
                    context.cognito_client = AWSCognitoClient(**cognito_params)
                if Resource.MONGODB in resource_list:
                    db_params = redis_manager.get_mongodb_config(Config.SERVICE_ID, request.context.tenant)
                    context.db_name = db_params.pop("name")
                    context.db_manager = DatabaseManager(**db_params)
                if Resource.POSTGRES in resource_list:
                    db_params = redis_manager.get_postgres_config(Config.SERVICE_ID, request.context.tenant)
                    context.db_name = db_params.get("name")
                    context.db_manager = PostgresDatabaseManager(**db_params)
            except Exception as e:
                logger.info(f"Decorator Exception! {str(e)}")
            c = funcion(instance, request, context)
            return c

        return inner

    return decorador_func
