# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.sales import picking_pb2 as v1_dot_sales_dot_picking__pb2


class PickingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PickingCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.picking.PickingService/PickingCreate",
            request_serializer=v1_dot_sales_dot_picking__pb2.PickingCreateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_picking__pb2.PickingCreateResponse.FromString,
        )
        self.PickingRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.picking.PickingService/PickingRead",
            request_serializer=v1_dot_sales_dot_picking__pb2.PickingReadRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_picking__pb2.PickingReadResponse.FromString,
        )
        self.PickingUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.picking.PickingService/PickingUpdate",
            request_serializer=v1_dot_sales_dot_picking__pb2.PickingUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_picking__pb2.PickingUpdateResponse.FromString,
        )
        self.PickingDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.picking.PickingService/PickingDelete",
            request_serializer=v1_dot_sales_dot_picking__pb2.PickingDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_picking__pb2.PickingDeleteResponse.FromString,
        )


class PickingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PickingCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickingRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickingUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickingDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PickingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PickingCreate": grpc.unary_unary_rpc_method_handler(
            servicer.PickingCreate,
            request_deserializer=v1_dot_sales_dot_picking__pb2.PickingCreateRequest.FromString,
            response_serializer=v1_dot_sales_dot_picking__pb2.PickingCreateResponse.SerializeToString,
        ),
        "PickingRead": grpc.unary_unary_rpc_method_handler(
            servicer.PickingRead,
            request_deserializer=v1_dot_sales_dot_picking__pb2.PickingReadRequest.FromString,
            response_serializer=v1_dot_sales_dot_picking__pb2.PickingReadResponse.SerializeToString,
        ),
        "PickingUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.PickingUpdate,
            request_deserializer=v1_dot_sales_dot_picking__pb2.PickingUpdateRequest.FromString,
            response_serializer=v1_dot_sales_dot_picking__pb2.PickingUpdateResponse.SerializeToString,
        ),
        "PickingDelete": grpc.unary_unary_rpc_method_handler(
            servicer.PickingDelete,
            request_deserializer=v1_dot_sales_dot_picking__pb2.PickingDeleteRequest.FromString,
            response_serializer=v1_dot_sales_dot_picking__pb2.PickingDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.sales.picking.PickingService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PickingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PickingCreate(
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
            "/pro.omni.oms.api.v1.sales.picking.PickingService/PickingCreate",
            v1_dot_sales_dot_picking__pb2.PickingCreateRequest.SerializeToString,
            v1_dot_sales_dot_picking__pb2.PickingCreateResponse.FromString,
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
    def PickingRead(
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
            "/pro.omni.oms.api.v1.sales.picking.PickingService/PickingRead",
            v1_dot_sales_dot_picking__pb2.PickingReadRequest.SerializeToString,
            v1_dot_sales_dot_picking__pb2.PickingReadResponse.FromString,
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
    def PickingUpdate(
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
            "/pro.omni.oms.api.v1.sales.picking.PickingService/PickingUpdate",
            v1_dot_sales_dot_picking__pb2.PickingUpdateRequest.SerializeToString,
            v1_dot_sales_dot_picking__pb2.PickingUpdateResponse.FromString,
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
    def PickingDelete(
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
            "/pro.omni.oms.api.v1.sales.picking.PickingService/PickingDelete",
            v1_dot_sales_dot_picking__pb2.PickingDeleteRequest.SerializeToString,
            v1_dot_sales_dot_picking__pb2.PickingDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )