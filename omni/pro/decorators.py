from omni.pro.aws import AWSCognitoClient
from omni.pro.config import Config
from omni.pro.database import DatabaseManager, RedisManager
from omni.pro.util import Resource


def resources_decorator(resource_list: list) -> callable:
    def decorador_func(funcion: callable) -> callable:
        def inner(instance, request, context):
            redis_manager = RedisManager(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)
            if Resource.AWS_COGNITO in resource_list:
                cognito_params = redis_manager.get_aws_cognito_config(Config.SERVICE_ID, request.context.tenant)
                context.cognito_client = AWSCognitoClient(**cognito_params)
            if Resource.MONGODB in resource_list:
                db_params = redis_manager.get_mongodb_config(Config.SERVICE_ID, request.context.tenant)
                context.db_name = db_params.pop("name")
                context.db_manager = DatabaseManager(**db_params)
            c = funcion(instance, request, context)
            return c

        return inner

    return decorador_func
