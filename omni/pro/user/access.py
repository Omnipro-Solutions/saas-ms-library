# create a decorator to check if the user has permission to access the resource
from enum import Enum, unique

from omni.pro.response import MessageResponse
from omni_pro_base.logger import LoggerTraceback, configure_logger
from omni_pro_base.microservice import MicroService
from omni_pro_grpc.grpc_connector import Event, GRPClient
from omni_pro_grpc.v1.users import user_pb2

logger = configure_logger(name=__name__)

INTERNAL_USER = "internal"


@unique
class Permission(Enum):
    IS_SUPERUSER = "IS_SUPERUSER"


def permission_required(permission_name: Permission, cls) -> callable:
    def decorador_func(funcion: callable) -> callable:
        def inner(instance, request, context):
            try:
                event = Event(
                    module_grpc="v1.users.user_pb2_grpc",
                    module_pb2="v1.users.user_pb2",
                    stub_classname="UsersServiceStub",
                    rpc_method="HasPermission",
                    request_class="HasPermissionRequest",
                    params={
                        "username": request.context.user,
                        "permission": permission_name.value,
                        "context": {"tenant": request.context.tenant},
                    },
                )
                response: user_pb2.HasPermissionResponse = None
                response, success = GRPClient(MicroService.SAAS_MS_USER.value).call_rpc_fuction(event)
                if not success or not response.has_permission:
                    return MessageResponse(cls).unauthorized_response()
            except Exception as e:
                LoggerTraceback.error("Permission required decorator exception", e, logger)
                return MessageResponse(cls).internal_response(message="Permission required decorator exception")
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
