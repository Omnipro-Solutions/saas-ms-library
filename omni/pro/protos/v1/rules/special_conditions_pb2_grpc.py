# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.rules import special_conditions_pb2 as v1_dot_rules_dot_special__conditions__pb2


class SpecialConditionsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SpecialConditionsCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.special_conditions.SpecialConditionsService/SpecialConditionsCreate",
            request_serializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsCreateResponse.FromString,
        )
        self.SpecialConditionsRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.special_conditions.SpecialConditionsService/SpecialConditionsRead",
            request_serializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsReadResponse.FromString,
        )
        self.SpecialConditionsUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.special_conditions.SpecialConditionsService/SpecialConditionsUpdate",
            request_serializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsUpdateResponse.FromString,
        )
        self.SpecialConditionsDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.special_conditions.SpecialConditionsService/SpecialConditionsDelete",
            request_serializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsDeleteResponse.FromString,
        )


class SpecialConditionsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SpecialConditionsCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SpecialConditionsRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SpecialConditionsUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SpecialConditionsDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SpecialConditionsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SpecialConditionsCreate": grpc.unary_unary_rpc_method_handler(
            servicer.SpecialConditionsCreate,
            request_deserializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsCreateResponse.SerializeToString,
        ),
        "SpecialConditionsRead": grpc.unary_unary_rpc_method_handler(
            servicer.SpecialConditionsRead,
            request_deserializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsReadResponse.SerializeToString,
        ),
        "SpecialConditionsUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.SpecialConditionsUpdate,
            request_deserializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsUpdateResponse.SerializeToString,
        ),
        "SpecialConditionsDelete": grpc.unary_unary_rpc_method_handler(
            servicer.SpecialConditionsDelete,
            request_deserializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.special_conditions.SpecialConditionsService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SpecialConditionsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SpecialConditionsCreate(
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
            "/pro.omni.oms.api.v1.rules.special_conditions.SpecialConditionsService/SpecialConditionsCreate",
            v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsCreateRequest.SerializeToString,
            v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsCreateResponse.FromString,
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
    def SpecialConditionsRead(
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
            "/pro.omni.oms.api.v1.rules.special_conditions.SpecialConditionsService/SpecialConditionsRead",
            v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsReadRequest.SerializeToString,
            v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsReadResponse.FromString,
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
    def SpecialConditionsUpdate(
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
            "/pro.omni.oms.api.v1.rules.special_conditions.SpecialConditionsService/SpecialConditionsUpdate",
            v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsUpdateRequest.SerializeToString,
            v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsUpdateResponse.FromString,
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
    def SpecialConditionsDelete(
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
            "/pro.omni.oms.api.v1.rules.special_conditions.SpecialConditionsService/SpecialConditionsDelete",
            v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsDeleteRequest.SerializeToString,
            v1_dot_rules_dot_special__conditions__pb2.SpecialConditionsDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )