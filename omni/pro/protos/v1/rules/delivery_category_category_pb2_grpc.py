# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.rules import (
    delivery_category_category_pb2 as v1_dot_rules_dot_delivery__category__category__pb2,
)


class DeliveryCategoryCategoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeliveryCategoryCategoryCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_category_category.DeliveryCategoryCategoryService/DeliveryCategoryCategoryCreate",
            request_serializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryCreateResponse.FromString,
        )
        self.DeliveryCategoryCategoryRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_category_category.DeliveryCategoryCategoryService/DeliveryCategoryCategoryRead",
            request_serializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryReadResponse.FromString,
        )
        self.DeliveryCategoryCategoryUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_category_category.DeliveryCategoryCategoryService/DeliveryCategoryCategoryUpdate",
            request_serializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryUpdateResponse.FromString,
        )
        self.DeliveryCategoryCategoryDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_category_category.DeliveryCategoryCategoryService/DeliveryCategoryCategoryDelete",
            request_serializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryDeleteResponse.FromString,
        )


class DeliveryCategoryCategoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DeliveryCategoryCategoryCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryCategoryCategoryRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryCategoryCategoryUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryCategoryCategoryDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DeliveryCategoryCategoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "DeliveryCategoryCategoryCreate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryCategoryCategoryCreate,
            request_deserializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryCreateResponse.SerializeToString,
        ),
        "DeliveryCategoryCategoryRead": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryCategoryCategoryRead,
            request_deserializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryReadResponse.SerializeToString,
        ),
        "DeliveryCategoryCategoryUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryCategoryCategoryUpdate,
            request_deserializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryUpdateResponse.SerializeToString,
        ),
        "DeliveryCategoryCategoryDelete": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryCategoryCategoryDelete,
            request_deserializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.delivery_category_category.DeliveryCategoryCategoryService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DeliveryCategoryCategoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DeliveryCategoryCategoryCreate(
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
            "/pro.omni.oms.api.v1.rules.delivery_category_category.DeliveryCategoryCategoryService/DeliveryCategoryCategoryCreate",
            v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryCreateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryCreateResponse.FromString,
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
    def DeliveryCategoryCategoryRead(
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
            "/pro.omni.oms.api.v1.rules.delivery_category_category.DeliveryCategoryCategoryService/DeliveryCategoryCategoryRead",
            v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryReadRequest.SerializeToString,
            v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryReadResponse.FromString,
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
    def DeliveryCategoryCategoryUpdate(
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
            "/pro.omni.oms.api.v1.rules.delivery_category_category.DeliveryCategoryCategoryService/DeliveryCategoryCategoryUpdate",
            v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryUpdateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryUpdateResponse.FromString,
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
    def DeliveryCategoryCategoryDelete(
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
            "/pro.omni.oms.api.v1.rules.delivery_category_category.DeliveryCategoryCategoryService/DeliveryCategoryCategoryDelete",
            v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryDeleteRequest.SerializeToString,
            v1_dot_rules_dot_delivery__category__category__pb2.DeliveryCategoryCategoryDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )