from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.utilities import model_pb2 as _model_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ModelRegisterJobRequest(_message.Message):
    __slots__ = ["service_id", "update", "model_create", "model_update"]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    MODEL_CREATE_FIELD_NUMBER: _ClassVar[int]
    MODEL_UPDATE_FIELD_NUMBER: _ClassVar[int]
    service_id: str
    update: _wrappers_pb2.BoolValue
    model_create: _model_pb2.ModelCreateRequest
    model_update: _model_pb2.ModelUpdateRequest
    def __init__(
        self,
        service_id: _Optional[str] = ...,
        update: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        model_create: _Optional[_Union[_model_pb2.ModelCreateRequest, _Mapping]] = ...,
        model_update: _Optional[_Union[_model_pb2.ModelUpdateRequest, _Mapping]] = ...,
    ) -> None: ...

class ModelRegisterJobResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
