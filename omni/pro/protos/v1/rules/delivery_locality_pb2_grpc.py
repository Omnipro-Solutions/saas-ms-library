# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.rules import delivery_locality_pb2 as v1_dot_rules_dot_delivery__locality__pb2


class DeliveryLocalityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeliveryLocalityCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityService/DeliveryLocalityCreate",
            request_serializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityCreateResponse.FromString,
        )
        self.DeliveryLocalityRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityService/DeliveryLocalityRead",
            request_serializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityReadResponse.FromString,
        )
        self.DeliveryLocalityUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityService/DeliveryLocalityUpdate",
            request_serializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityUpdateResponse.FromString,
        )
        self.DeliveryLocalityDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityService/DeliveryLocalityDelete",
            request_serializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityDeleteResponse.FromString,
        )


class DeliveryLocalityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DeliveryLocalityCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryLocalityRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryLocalityUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeliveryLocalityDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DeliveryLocalityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "DeliveryLocalityCreate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryLocalityCreate,
            request_deserializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityCreateResponse.SerializeToString,
        ),
        "DeliveryLocalityRead": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryLocalityRead,
            request_deserializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityReadResponse.SerializeToString,
        ),
        "DeliveryLocalityUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryLocalityUpdate,
            request_deserializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityUpdateResponse.SerializeToString,
        ),
        "DeliveryLocalityDelete": grpc.unary_unary_rpc_method_handler(
            servicer.DeliveryLocalityDelete,
            request_deserializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DeliveryLocalityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DeliveryLocalityCreate(
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
            "/pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityService/DeliveryLocalityCreate",
            v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityCreateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityCreateResponse.FromString,
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
    def DeliveryLocalityRead(
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
            "/pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityService/DeliveryLocalityRead",
            v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityReadRequest.SerializeToString,
            v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityReadResponse.FromString,
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
    def DeliveryLocalityUpdate(
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
            "/pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityService/DeliveryLocalityUpdate",
            v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityUpdateRequest.SerializeToString,
            v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityUpdateResponse.FromString,
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
    def DeliveryLocalityDelete(
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
            "/pro.omni.oms.api.v1.rules.delivery_locality.DeliveryLocalityService/DeliveryLocalityDelete",
            v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityDeleteRequest.SerializeToString,
            v1_dot_rules_dot_delivery__locality__pb2.DeliveryLocalityDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )