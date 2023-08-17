from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StockBatcherRequest(_message.Message):
    __slots__ = ["stock_entries", "batch", "type", "context"]
    STOCK_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    stock_entries: _struct_pb2.ListValue
    batch: _struct_pb2.Struct
    type: str
    context: _base_pb2.Context
    def __init__(
        self,
        stock_entries: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        batch: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        type: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class StockBatcherResponse(_message.Message):
    __slots__ = ["record"]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    record: str
    def __init__(self, record: _Optional[str] = ...) -> None: ...
