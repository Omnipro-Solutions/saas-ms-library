from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class BatchUpsertRequest(_message.Message):
    __slots__ = ["tenant", "model_path", "models", "context"]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    tenant: str
    model_path: str
    models: _struct_pb2.ListValue
    context: _base_pb2.Context
    def __init__(
        self,
        tenant: _Optional[str] = ...,
        model_path: _Optional[str] = ...,
        models: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class BatchUpsertResponse(_message.Message):
    __slots__ = ["error_models", "response_standard"]
    ERROR_MODELS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    error_models: _struct_pb2.ListValue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        error_models: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
