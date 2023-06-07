# create a decorator to check if the user has permission to access the resource
from omni.pro.logger import LoggerTraceback, configure_logger
from omni.pro.protos.v1.users import user_pb2

logger = configure_logger(name=__name__)


def permission_required(permission_name: str) -> callable:
    def decorador_func(funcion: callable) -> callable:
        def inner(instance, request, context):
            try:
                pass
            except Exception as e:
                LoggerTraceback.error("Resource Decorator exception", e, logger)
            c = funcion(instance, request, context)
            return c

        return inner

    return decorador_func


def sync_cognito_access(sync_allow_access):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            result = funcion(*args, **kwargs)
            sync_allow_access(result)
            return result

        return wrapper

    return decorador


# Definimos la función que queremos ejecutar al final
def sync_allow_access(result):
    try:
        logger.info("sync_allow_access")
        if isinstance(result, user_pb2.GroupCreateResponse):
            pass
    except Exception as e:
        LoggerTraceback.error("Resource Decorator exception", e, logger)
    return True
