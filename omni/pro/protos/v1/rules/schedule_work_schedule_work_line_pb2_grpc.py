# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.rules import (
    schedule_work_schedule_work_line_pb2 as v1_dot_rules_dot_schedule__work__schedule__work__line__pb2,
)


class ScheduleWorkScheduleWorkLineServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ScheduleWorkScheduleWorkLineCreate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineService/ScheduleWorkScheduleWorkLineCreate",
            request_serializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineCreateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineCreateResponse.FromString,
        )
        self.ScheduleWorkScheduleWorkLineRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineService/ScheduleWorkScheduleWorkLineRead",
            request_serializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineReadRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineReadResponse.FromString,
        )
        self.ScheduleWorkScheduleWorkLineUpdate = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineService/ScheduleWorkScheduleWorkLineUpdate",
            request_serializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineUpdateRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineUpdateResponse.FromString,
        )
        self.ScheduleWorkScheduleWorkLineDelete = channel.unary_unary(
            "/pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineService/ScheduleWorkScheduleWorkLineDelete",
            request_serializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineDeleteRequest.SerializeToString,
            response_deserializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineDeleteResponse.FromString,
        )


class ScheduleWorkScheduleWorkLineServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ScheduleWorkScheduleWorkLineCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ScheduleWorkScheduleWorkLineRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ScheduleWorkScheduleWorkLineUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def ScheduleWorkScheduleWorkLineDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ScheduleWorkScheduleWorkLineServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ScheduleWorkScheduleWorkLineCreate": grpc.unary_unary_rpc_method_handler(
            servicer.ScheduleWorkScheduleWorkLineCreate,
            request_deserializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineCreateRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineCreateResponse.SerializeToString,
        ),
        "ScheduleWorkScheduleWorkLineRead": grpc.unary_unary_rpc_method_handler(
            servicer.ScheduleWorkScheduleWorkLineRead,
            request_deserializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineReadRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineReadResponse.SerializeToString,
        ),
        "ScheduleWorkScheduleWorkLineUpdate": grpc.unary_unary_rpc_method_handler(
            servicer.ScheduleWorkScheduleWorkLineUpdate,
            request_deserializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineUpdateRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineUpdateResponse.SerializeToString,
        ),
        "ScheduleWorkScheduleWorkLineDelete": grpc.unary_unary_rpc_method_handler(
            servicer.ScheduleWorkScheduleWorkLineDelete,
            request_deserializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineDeleteRequest.FromString,
            response_serializer=v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineService",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ScheduleWorkScheduleWorkLineService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ScheduleWorkScheduleWorkLineCreate(
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
            "/pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineService/ScheduleWorkScheduleWorkLineCreate",
            v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineCreateRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineCreateResponse.FromString,
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
    def ScheduleWorkScheduleWorkLineRead(
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
            "/pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineService/ScheduleWorkScheduleWorkLineRead",
            v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineReadRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineReadResponse.FromString,
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
    def ScheduleWorkScheduleWorkLineUpdate(
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
            "/pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineService/ScheduleWorkScheduleWorkLineUpdate",
            v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineUpdateRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineUpdateResponse.FromString,
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
    def ScheduleWorkScheduleWorkLineDelete(
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
            "/pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineService/ScheduleWorkScheduleWorkLineDelete",
            v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineDeleteRequest.SerializeToString,
            v1_dot_rules_dot_schedule__work__schedule__work__line__pb2.ScheduleWorkScheduleWorkLineDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )