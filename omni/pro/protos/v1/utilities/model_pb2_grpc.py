# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.utilities import model_pb2 as v1_dot_utilities_dot_model__pb2


class ModelsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ModelCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.model.ModelsService/ModelCreate",
            request_serializer=v1_dot_utilities_dot_model__pb2.ModelCreateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_model__pb2.ModelCreateResponse.FromString,
        )
        self.ModelRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.model.ModelsService/ModelRead",
            request_serializer=v1_dot_utilities_dot_model__pb2.ModelReadRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_model__pb2.ModelReadResponse.FromString,
        )
        self.ModelUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.model.ModelsService/ModelUpdate",
            request_serializer=v1_dot_utilities_dot_model__pb2.ModelUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_model__pb2.ModelUpdateResponse.FromString,
        )
        self.ModelDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.model.ModelsService/ModelDelete",
            request_serializer=v1_dot_utilities_dot_model__pb2.ModelDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_model__pb2.ModelDeleteResponse.FromString,
        )


class ModelsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ModelCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ModelRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ModelUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ModelDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ModelsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ModelCreate": grpc.unary_unary_rpc_method_handler(
            servicer.ModelCreate,
            request_deserializer=v1_dot_utilities_dot_model__pb2.ModelCreateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_model__pb2.ModelCreateResponse.SerializeToString,
        ),
        "ModelRead": grpc.unary_unary_rpc_method_handler(
            servicer.ModelRead,
            request_deserializer=v1_dot_utilities_dot_model__pb2.ModelReadRequest.FromString,
            response_serializer=v1_dot_utilities_dot_model__pb2.ModelReadResponse.SerializeToString,
        ),
        "ModelUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.ModelUpdate,
            request_deserializer=v1_dot_utilities_dot_model__pb2.ModelUpdateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_model__pb2.ModelUpdateResponse.SerializeToString,
        ),
        "ModelDelete": grpc.unary_unary_rpc_method_handler(
            servicer.ModelDelete,
            request_deserializer=v1_dot_utilities_dot_model__pb2.ModelDeleteRequest.FromString,
            response_serializer=v1_dot_utilities_dot_model__pb2.ModelDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.model.ModelsService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ModelsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ModelCreate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.utilities.model.ModelsService/ModelCreate",
            v1_dot_utilities_dot_model__pb2.ModelCreateRequest.SerializeToString,
            v1_dot_utilities_dot_model__pb2.ModelCreateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ModelRead(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.utilities.model.ModelsService/ModelRead",
            v1_dot_utilities_dot_model__pb2.ModelReadRequest.SerializeToString,
            v1_dot_utilities_dot_model__pb2.ModelReadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ModelUpdate(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.utilities.model.ModelsService/ModelUpdate",
            v1_dot_utilities_dot_model__pb2.ModelUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_model__pb2.ModelUpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def ModelDelete(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/pro.omni.oms.api.v1.utilities.model.ModelsService/ModelDelete",
            v1_dot_utilities_dot_model__pb2.ModelDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_model__pb2.ModelDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )