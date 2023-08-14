from omni.pro.config import Config
from omni.pro.protos.grpc_connector import Event, GRPClient


class ModelRPCFucntion(object):
    def __init__(self, context: dict) -> None:
        """
        :param context: context with tenant and user\n
        Example:
        ```
        context = {"tenant": "tenant_code", "user": "user_name"}
        ```
        """
        self.context = context
        self.service_id = Config.SAAS_MS_UTILITIES
        self.module_grpc = "v1.utilities.model_pb2_grpc"
        self.stub_classname = "ModelsServiceStub"
        self.module_pb2 = "v1.utilities.model_pb2"

        self.client: GRPClient = GRPClient(self.service_id)

    def register_model(self, **params):
        event = Event(
            module_grpc=self.module_grpc,
            stub_classname=self.stub_classname,
            rpc_method="ModelCreate",
            module_pb2=self.module_pb2,
            request_class="ModelCreateRequest",
            params={"context": self.context} | params,
        )
        return self.client.call_rpc_fuction(event)
