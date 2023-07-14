import importlib
from pathlib import Path

import grpc
from omni.pro import util
from omni.pro.cloudmap import CloudMap
from omni.pro.config import Config
from omni.pro.logger import configure_logger

logger = configure_logger(name=__name__)


class GRPClient(object):
    def __init__(self, service_id):
        self.service_id = service_id

    def call_rpc_fuction(self, event: dict):
        """
        function to call rpc function
        :param event: dict with params to call rpc function
        event = {
            "module_grpc": "v1.users.user_pb2_grpc",
            "stub_classname": "UsersServiceStub",
            "rpc_method": "UserRead",
            "module_pb2": "v1.users.user_pb2",
            "request_class": "UserReadRequest",
            "params": {"id": "64adc0477be3ec5e9160b16e", "context": {"tenant": "SPLA", "user": "admin"}},
        }
        """
        # credentials = grpc.ssl_channel_credentials()
        # with grpc.secure_channel(
        #     self.url,
        #     credentials,
        #     options=[("grpc.ssl_target_name_override", "omni.pro")],
        # ) as channel:
        cloud_map = CloudMap(service_name=Config.SERVICE_NAME_BALANCER)
        url = cloud_map.get_url_channel(self.service_id)
        with grpc.insecure_channel(url) as channel:
            stub = event.get("service_stub")
            stub_classname = event.get("stub_classname")
            parent_path = Path(__file__).parent
            modulo_grpc = util.load_file_module(
                parent_path / (event.get("module_grpc").replace(".", "/") + ".py"), stub_classname
            )
            stub = getattr(modulo_grpc, stub_classname)(channel)
            request_class = event.get("request_class")
            module_pb2 = util.load_file_module(
                parent_path / (event.get("module_pb2").replace(".", "/") + ".py"), request_class
            )
            request = getattr(module_pb2, request_class)(**event.get("params"))
            # Instance the method rpc que recibe el request
            response = getattr(stub, event.get("rpc_method"))(request)
            success = response.response_standard.status_code in range(200, 300)
            return response, success


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
