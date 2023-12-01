from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class QueryStockRequest(_message.Message):
    __slots__ = ["query", "context"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    query: str
    context: _base_pb2.Context
    def __init__(
        self, query: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class QueryStockResponse(_message.Message):
    __slots__ = ["response_standard", "query"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    query: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        query: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
    ) -> None: ...
