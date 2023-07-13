import importlib
from pathlib import Path

import grpc
from omni.pro import util
from omni.pro.cloudmap import CloudMap
from omni.pro.logger import configure_logger


@measure_time
def lambda_handler(event, context):
    logging.basicConfig()
    return json_format.MessageToDict(
        Client().call_api_method(event),
        preserving_proto_field_name=True,
        including_default_value_fields=True,
    )


logger = configure_logger(name=__name__)


class GRPCClient(object):
    def __init__(self, service_id):
        response = CloudMap().discover_instances()
        for instance in response["Instances"]:
            if instance.get("InstanceId") == service_id:
                self.url = "{}:{}".format(
                    instance.get("Attributes").get("host"),
                    instance.get("Attributes").get("port"),
                )
                break

    def call_api_method(self, event: dict):
        stub = event.get("service_stub")
        method = event.get("rpc_method")
        api_method = self.api_methods()[method]
        credentials = grpc.ssl_channel_credentials()
        # with grpc.secure_channel(
        #     self.url,
        #     credentials,
        #     options=[("grpc.ssl_target_name_override", "omni.pro")],
        # ) as channel:
        with grpc.insecure_channel(self.url) as channel:
            stub_classname = util.to_camel_case(event.get("stub_classname"))
            modulo_grpc = util.load_file_module(
                Path(__file__) / event.get("module_grpc").replace(".", "/") / ".py", stub_classname
            )
            stub = getattr(modulo_grpc, stub_classname)(channel)
            request_class = util.to_camel_case(event["request_class"])
            module_pb2 = util.load_file_module(
                Path(__file__) / event.get("module_grpc").replace(".", "/") / ".py", request_class
            )
            response = getattr(stub, api_method["method"])(getattr(address_pb2, api_method["request"])(**event[method]))
            return response

    def api_methods(self):
        return {
            "module_grpc": "v1.users.users_pb2_grpc",
            "stub_classname": "UserStub",
            "rpc_method": "UserRead",
            "module_pb2": "v1.users.users_pb2",
            "request_class": "UserReadRequest",
            "params": {"id": "id"},
        }


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
