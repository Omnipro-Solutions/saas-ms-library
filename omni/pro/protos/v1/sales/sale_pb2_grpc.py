# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.sales import sale_pb2 as v1_dot_sales_dot_sale__pb2


class SaleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SaleCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.sale.SaleService/SaleCreate",
            request_serializer=v1_dot_sales_dot_sale__pb2.SaleCreateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_sale__pb2.SaleCreateResponse.FromString,
        )
        self.SaleRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.sale.SaleService/SaleRead",
            request_serializer=v1_dot_sales_dot_sale__pb2.SaleReadRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_sale__pb2.SaleReadResponse.FromString,
        )
        self.SaleUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.sale.SaleService/SaleUpdate",
            request_serializer=v1_dot_sales_dot_sale__pb2.SaleUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_sale__pb2.SaleUpdateResponse.FromString,
        )
        self.SaleDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.sales.sale.SaleService/SaleDelete",
            request_serializer=v1_dot_sales_dot_sale__pb2.SaleDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_sales_dot_sale__pb2.SaleDeleteResponse.FromString,
        )


class SaleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SaleCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SaleRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SaleUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SaleDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SaleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SaleCreate": grpc.unary_unary_rpc_method_handler(
            servicer.SaleCreate,
            request_deserializer=v1_dot_sales_dot_sale__pb2.SaleCreateRequest.FromString,
            response_serializer=v1_dot_sales_dot_sale__pb2.SaleCreateResponse.SerializeToString,
        ),
        "SaleRead": grpc.unary_unary_rpc_method_handler(
            servicer.SaleRead,
            request_deserializer=v1_dot_sales_dot_sale__pb2.SaleReadRequest.FromString,
            response_serializer=v1_dot_sales_dot_sale__pb2.SaleReadResponse.SerializeToString,
        ),
        "SaleUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.SaleUpdate,
            request_deserializer=v1_dot_sales_dot_sale__pb2.SaleUpdateRequest.FromString,
            response_serializer=v1_dot_sales_dot_sale__pb2.SaleUpdateResponse.SerializeToString,
        ),
        "SaleDelete": grpc.unary_unary_rpc_method_handler(
            servicer.SaleDelete,
            request_deserializer=v1_dot_sales_dot_sale__pb2.SaleDeleteRequest.FromString,
            response_serializer=v1_dot_sales_dot_sale__pb2.SaleDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.sales.sale.SaleService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SaleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SaleCreate(
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
            "/pro.omni.oms.api.v1.sales.sale.SaleService/SaleCreate",
            v1_dot_sales_dot_sale__pb2.SaleCreateRequest.SerializeToString,
            v1_dot_sales_dot_sale__pb2.SaleCreateResponse.FromString,
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
    def SaleRead(
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
            "/pro.omni.oms.api.v1.sales.sale.SaleService/SaleRead",
            v1_dot_sales_dot_sale__pb2.SaleReadRequest.SerializeToString,
            v1_dot_sales_dot_sale__pb2.SaleReadResponse.FromString,
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
    def SaleUpdate(
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
            "/pro.omni.oms.api.v1.sales.sale.SaleService/SaleUpdate",
            v1_dot_sales_dot_sale__pb2.SaleUpdateRequest.SerializeToString,
            v1_dot_sales_dot_sale__pb2.SaleUpdateResponse.FromString,
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
    def SaleDelete(
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
            "/pro.omni.oms.api.v1.sales.sale.SaleService/SaleDelete",
            v1_dot_sales_dot_sale__pb2.SaleDeleteRequest.SerializeToString,
            v1_dot_sales_dot_sale__pb2.SaleDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )