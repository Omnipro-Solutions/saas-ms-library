# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.rules import picker_pb2 as v1_dot_rules_dot_picker__pb2


class PickerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PickerCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.picker.PickerService/PickerCreate",
            request_serializer=v1_dot_rules_dot_picker__pb2.PickerCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_picker__pb2.PickerCreateResponse.FromString,
        )
        self.PickerRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.picker.PickerService/PickerRead",
            request_serializer=v1_dot_rules_dot_picker__pb2.PickerReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_picker__pb2.PickerReadResponse.FromString,
        )
        self.PickerUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.picker.PickerService/PickerUpdate",
            request_serializer=v1_dot_rules_dot_picker__pb2.PickerUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_picker__pb2.PickerUpdateResponse.FromString,
        )
        self.PickerDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.picker.PickerService/PickerDelete",
            request_serializer=v1_dot_rules_dot_picker__pb2.PickerDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_picker__pb2.PickerDeleteResponse.FromString,
        )


class PickerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PickerCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickerRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickerUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def PickerDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PickerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PickerCreate": grpc.unary_unary_rpc_method_handler(
            servicer.PickerCreate,
            request_deserializer=v1_dot_rules_dot_picker__pb2.PickerCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_picker__pb2.PickerCreateResponse.SerializeToString,
        ),
        "PickerRead": grpc.unary_unary_rpc_method_handler(
            servicer.PickerRead,
            request_deserializer=v1_dot_rules_dot_picker__pb2.PickerReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_picker__pb2.PickerReadResponse.SerializeToString,
        ),
        "PickerUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.PickerUpdate,
            request_deserializer=v1_dot_rules_dot_picker__pb2.PickerUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_picker__pb2.PickerUpdateResponse.SerializeToString,
        ),
        "PickerDelete": grpc.unary_unary_rpc_method_handler(
            servicer.PickerDelete,
            request_deserializer=v1_dot_rules_dot_picker__pb2.PickerDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_picker__pb2.PickerDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.picker.PickerService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PickerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PickerCreate(
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
            "/pro.omni.oms.api.v1.rules.picker.PickerService/PickerCreate",
            v1_dot_rules_dot_picker__pb2.PickerCreateRequest.SerializeToString,
            v1_dot_rules_dot_picker__pb2.PickerCreateResponse.FromString,
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
    def PickerRead(
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
            "/pro.omni.oms.api.v1.rules.picker.PickerService/PickerRead",
            v1_dot_rules_dot_picker__pb2.PickerReadRequest.SerializeToString,
            v1_dot_rules_dot_picker__pb2.PickerReadResponse.FromString,
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
    def PickerUpdate(
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
            "/pro.omni.oms.api.v1.rules.picker.PickerService/PickerUpdate",
            v1_dot_rules_dot_picker__pb2.PickerUpdateRequest.SerializeToString,
            v1_dot_rules_dot_picker__pb2.PickerUpdateResponse.FromString,
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
    def PickerDelete(
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
            "/pro.omni.oms.api.v1.rules.picker.PickerService/PickerDelete",
            v1_dot_rules_dot_picker__pb2.PickerDeleteRequest.SerializeToString,
            v1_dot_rules_dot_picker__pb2.PickerDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )