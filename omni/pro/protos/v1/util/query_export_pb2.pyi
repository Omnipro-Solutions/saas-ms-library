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

class QueryExportRequest(_message.Message):
    __slots__ = ["model_path", "query", "fields", "context"]
    MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model_path: str
    query: str
    fields: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self,
        model_path: _Optional[str] = ...,
        query: _Optional[str] = ...,
        fields: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class QueryExportResponse(_message.Message):
    __slots__ = ["response_standard", "result"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    result: _struct_pb2.ListValue
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        result: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
    ) -> None: ...
