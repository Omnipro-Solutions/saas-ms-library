import importlib

import grpc
from grpc._channel import Channel
from grpc.experimental import _insecure_channel_credentials
from omni.pro.cloudmap import CloudMap
from omni.pro.config import Config
from omni.pro.database.redis import RedisManager
from omni.pro.logger import configure_logger
from omni.pro.protos.util import format_request
from omni.pro.util import nested

logger = configure_logger(name=__name__)


class Event(dict):
    def __init__(
        self,
        module_grpc: str,
        stub_classname: str,
        rpc_method: str,
        module_pb2: str,
        request_class: str,
        params: dict = {},
    ):
        super().__init__()
        self["module_grpc"] = module_grpc
        self["stub_classname"] = stub_classname
        self["rpc_method"] = rpc_method
        self["module_pb2"] = module_pb2
        self["request_class"] = request_class
        self["params"] = params


class OmniChannel(Channel):
    def __init__(
        self,
        service_id,
        credentials=None,
        options=None,
        compression=None,
        tennat=None,
    ):
        if not Config.DEBUG:
            credentials = credentials or grpc.ssl_channel_credentials()
            if credentials is None or credentials._credentials is _insecure_channel_credentials:
                raise ValueError(
                    "secure_channel cannot be called with insecure credentials." + " Call insecure_channel instead."
                )
            credentials = credentials._credentials
            options = options + [("grpc.ssl_target_name_override", "omni.pro")] or [
                ("grpc.ssl_target_name_override", "omni.pro")
            ]

        # cloud_map = CloudMap(service_name=Config.SERVICE_NAME_BALANCER)
        # target = cloud_map.get_url_channel(service_id)
        target = self.get_target(service_id, tennat)
        super().__init__(target, () if options is None else options, credentials, compression)

    def get_target(self, service_id, tennat):
        redis = RedisManager(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB)
        return redis.get_load_balancer_name(service_id, tennat)


class GRPClient(object):
    def __init__(self, service_id: str):
        self.service_id = service_id

    def call_rpc_fuction(self, event: Event, *args, **kwargs):
        """
        function to call rpc function
        :param event: Event with params to call rpc function
        ```
        event = Event(
            module_grpc="v1.users.user_pb2_grpc",
            stub_classname="UsersServiceStub",
            rpc_method="UserRead",
            module_pb2="v1.users.user_pb2",
            request_class="UserReadRequest",
            params={"id": "64adc0477be3ec5e9160b16e", "context": {"tenant": "SPLA", "user": "admin"}},
        )
        response, success = GRPClient(service_id=Config.SERVICE_ID).call_rpc_fuction(event)
        ```
        """
        with OmniChannel(
            self.service_id,
            options=[
                ("grpc.max_receive_message_length", 100 * 1024 * 1024),
                ("grpc.max_send_message_length", 100 * 1024 * 1024),
            ],
            *args,
            **kwargs,
            tennat=nested(event, "params.context.tenant"),
        ) as channel:
            stub = event.get("service_stub")
            stub_classname = event.get("stub_classname")
            path_module = "omni.pro.protos"
            module_grpc = importlib.import_module(f"{path_module}.{event.get('module_grpc')}")
            stub = getattr(module_grpc, stub_classname)(channel)
            request_class = event.get("request_class")
            module_pb2 = importlib.import_module(f"{path_module}.{event.get('module_pb2')}")
            request = format_request(event.get("params"), request_class, module_pb2)
            # Instance the method rpc que recibe el request
            response = getattr(stub, event.get("rpc_method"))(request)
            success = True
            if hasattr(response, "response_standard"):
                success = response.response_standard.status_code in range(200, 300)
            return response, success
