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


class Permission(object):
    CAN_CREATE_ACCESS = "CAN_CREATE_ACCESS"
    CAN_UPDATE_ACCESS = "CAN_UPDATE_ACCESS"
    CAN_READ_ACCESS = "CAN_READ_ACCESS"
    CAN_DELETE_ACCESS = "CAN_DELETE_ACCESS"
    CAN_CREATE_ACTION = "CAN_CREATE_ACTION"
    CAN_READ_ACTION = "CAN_READ_ACTION"
    CAN_UPDATE_ACTION = "CAN_UPDATE_ACTION"
    CAN_DELETE_ACTION = "CAN_DELETE_ACTION"
    CAN_CREATE_GROUP = "CAN_CREATE_GROUP"
    CAN_READ_GROUP = "CAN_READ_GROUP"
    CAN_UPDATE_GROUP = "CAN_UPDATE_GROUP"
    CAN_DELETE_GROUP = "CAN_DELETE_GROUP"
    CAN_CREATE_USER = "CAN_CREATE_USER"
    CAN_UPDATE_USER = "CAN_UPDATE_USER"
    CAN_READ_USER = "CAN_READ_USER"
    CAN_DELETE_USER = "CAN_DELETE_USER"
    CAN_CHANGE_PASSWORD_USER = "CAN_CHAMGE_PASSWORD_USER"
    CAN_CHANGE_EMAIL_USER = "CAN_CHANGE_EMAIL_USER"
