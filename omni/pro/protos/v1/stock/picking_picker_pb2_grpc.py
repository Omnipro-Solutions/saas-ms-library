# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from omni.pro.protos.v1.stock import picking_picker_pb2 as v1_dot_stock_dot_picking__picker__pb2


class PickingPickerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PickingPickerRead = channel.unary_unary(
            "/pro.omni.oms.api.v1.stock.picking_picker.PickingPickerService/PickingPickerRead",
            request_serializer=v1_dot_stock_dot_picking__picker__pb2.PickingPickerReadRequest.SerializeToString,
            response_deserializer=v1_dot_stock_dot_picking__picker__pb2.PickingPickerReadResponse.FromString,
        )


class PickingPickerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PickingPickerRead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PickingPickerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "PickingPickerRead": grpc.unary_unary_rpc_method_handler(
            servicer.PickingPickerRead,
            request_deserializer=v1_dot_stock_dot_picking__picker__pb2.PickingPickerReadRequest.FromString,
            response_serializer=v1_dot_stock_dot_picking__picker__pb2.PickingPickerReadResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "pro.omni.oms.api.v1.stock.picking_picker.PickingPickerService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PickingPickerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PickingPickerRead(
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
            "/pro.omni.oms.api.v1.stock.picking_picker.PickingPickerService/PickingPickerRead",
            v1_dot_stock_dot_picking__picker__pb2.PickingPickerReadRequest.SerializeToString,
            v1_dot_stock_dot_picking__picker__pb2.PickingPickerReadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )