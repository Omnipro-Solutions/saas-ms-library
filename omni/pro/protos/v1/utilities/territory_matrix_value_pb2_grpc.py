# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.utilities import (
    territory_matrix_value_pb2 as v1_dot_utilities_dot_territory__matrix__value__pb2,
)


class TerritoryMatrixValueServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TerritoryMatrixValueAdd = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueService/TerritoryMatrixValueAdd",
            request_serializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueAddRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueAddResponse.FromString,
        )
        self.TerritoryMatrixValueRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueService/TerritoryMatrixValueRead",
            request_serializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueReadRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueReadResponse.FromString,
        )
        self.TerritoryMatrixValueUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueService/TerritoryMatrixValueUpdate",
            request_serializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueUpdateResponse.FromString,
        )
        self.TerritoryMatrixValueDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueService/TerritoryMatrixValueDelete",
            request_serializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueDeleteResponse.FromString,
        )


class TerritoryMatrixValueServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TerritoryMatrixValueAdd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TerritoryMatrixValueRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TerritoryMatrixValueUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def TerritoryMatrixValueDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TerritoryMatrixValueServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "TerritoryMatrixValueAdd": grpc.unary_unary_rpc_method_handler(
            servicer.TerritoryMatrixValueAdd,
            request_deserializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueAddRequest.FromString,
            response_serializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueAddResponse.SerializeToString,
        ),
        "TerritoryMatrixValueRead": grpc.unary_unary_rpc_method_handler(
            servicer.TerritoryMatrixValueRead,
            request_deserializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueReadRequest.FromString,
            response_serializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueReadResponse.SerializeToString,
        ),
        "TerritoryMatrixValueUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.TerritoryMatrixValueUpdate,
            request_deserializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueUpdateRequest.FromString,
            response_serializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueUpdateResponse.SerializeToString,
        ),
        "TerritoryMatrixValueDelete": grpc.unary_unary_rpc_method_handler(
            servicer.TerritoryMatrixValueDelete,
            request_deserializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueDeleteRequest.FromString,
            response_serializer=v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TerritoryMatrixValueService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TerritoryMatrixValueAdd(
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
            "/pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueService/TerritoryMatrixValueAdd",
            v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueAddRequest.SerializeToString,
            v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueAddResponse.FromString,
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
    def TerritoryMatrixValueRead(
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
            "/pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueService/TerritoryMatrixValueRead",
            v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueReadRequest.SerializeToString,
            v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueReadResponse.FromString,
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
    def TerritoryMatrixValueUpdate(
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
            "/pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueService/TerritoryMatrixValueUpdate",
            v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueUpdateRequest.SerializeToString,
            v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueUpdateResponse.FromString,
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
    def TerritoryMatrixValueDelete(
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
            "/pro.omni.oms.api.v1.utilities.territory_matrix_value.TerritoryMatrixValueService/TerritoryMatrixValueDelete",
            v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueDeleteRequest.SerializeToString,
            v1_dot_utilities_dot_territory__matrix__value__pb2.TerritoryMatrixValueDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )