# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.sales import order_line_pb2 as v1_dot_sales_dot_order__line__pb2


class OrderLineServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OrderLineCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.line.OrderLineService/OrderLineCreate",
            request_serializer=v1_dot_sales_dot_order__line__pb2.OrderLineCreateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__line__pb2.OrderLineCreateResponse.FromString,
        )
        self.OrderLineRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.line.OrderLineService/OrderLineRead",
            request_serializer=v1_dot_sales_dot_order__line__pb2.OrderLineReadRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__line__pb2.OrderLineReadResponse.FromString,
        )
        self.OrderLineUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.line.OrderLineService/OrderLineUpdate",
            request_serializer=v1_dot_sales_dot_order__line__pb2.OrderLineUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__line__pb2.OrderLineUpdateResponse.FromString,
        )
        self.OrderLineDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.order.line.OrderLineService/OrderLineDelete",
            request_serializer=v1_dot_sales_dot_order__line__pb2.OrderLineDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_order__line__pb2.OrderLineDeleteResponse.FromString,
        )


class OrderLineServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OrderLineCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderLineRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderLineUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def OrderLineDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_OrderLineServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "OrderLineCreate": grpc.unary_unary_rpc_method_handler(
            servicer.OrderLineCreate,
            request_deserializer=v1_dot_sales_dot_order__line__pb2.OrderLineCreateRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__line__pb2.OrderLineCreateResponse.SerializeToString,
        ),
        "OrderLineRead": grpc.unary_unary_rpc_method_handler(
            servicer.OrderLineRead,
            request_deserializer=v1_dot_sales_dot_order__line__pb2.OrderLineReadRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__line__pb2.OrderLineReadResponse.SerializeToString,
        ),
        "OrderLineUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.OrderLineUpdate,
            request_deserializer=v1_dot_sales_dot_order__line__pb2.OrderLineUpdateRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__line__pb2.OrderLineUpdateResponse.SerializeToString,
        ),
        "OrderLineDelete": grpc.unary_unary_rpc_method_handler(
            servicer.OrderLineDelete,
            request_deserializer=v1_dot_sales_dot_order__line__pb2.OrderLineDeleteRequest.FromString,
            response_serializer=v1_dot_sales_dot_order__line__pb2.OrderLineDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.sales.order.line.OrderLineService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class OrderLineService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OrderLineCreate(
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
            "/pro.omni.oms.api.v1.sales.order.line.OrderLineService/OrderLineCreate",
            v1_dot_sales_dot_order__line__pb2.OrderLineCreateRequest.SerializeToString,
            v1_dot_sales_dot_order__line__pb2.OrderLineCreateResponse.FromString,
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
    def OrderLineRead(
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
            "/pro.omni.oms.api.v1.sales.order.line.OrderLineService/OrderLineRead",
            v1_dot_sales_dot_order__line__pb2.OrderLineReadRequest.SerializeToString,
            v1_dot_sales_dot_order__line__pb2.OrderLineReadResponse.FromString,
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
    def OrderLineUpdate(
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
            "/pro.omni.oms.api.v1.sales.order.line.OrderLineService/OrderLineUpdate",
            v1_dot_sales_dot_order__line__pb2.OrderLineUpdateRequest.SerializeToString,
            v1_dot_sales_dot_order__line__pb2.OrderLineUpdateResponse.FromString,
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
    def OrderLineDelete(
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
            "/pro.omni.oms.api.v1.sales.order.line.OrderLineService/OrderLineDelete",
            v1_dot_sales_dot_order__line__pb2.OrderLineDeleteRequest.SerializeToString,
            v1_dot_sales_dot_order__line__pb2.OrderLineDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )