from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Field(_message.Message):
    __slots__ = ["key", "x_amz_algorithm", "x_amz_credential", "x_amz_date", "policy", "x_amz_signature"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    X_AMZ_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    X_AMZ_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    X_AMZ_DATE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    X_AMZ_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    key: str
    x_amz_algorithm: str
    x_amz_credential: str
    x_amz_date: str
    policy: str
    x_amz_signature: str
    def __init__(
        self,
        key: _Optional[str] = ...,
        x_amz_algorithm: _Optional[str] = ...,
        x_amz_credential: _Optional[str] = ...,
        x_amz_date: _Optional[str] = ...,
        policy: _Optional[str] = ...,
        x_amz_signature: _Optional[str] = ...,
    ) -> None: ...

class UploadFile(_message.Message):
    __slots__ = ["url", "fields"]
    URL_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    url: str
    fields: Field
    def __init__(self, url: _Optional[str] = ..., fields: _Optional[_Union[Field, _Mapping]] = ...) -> None: ...

class UploadXlsxRequest(_message.Message):
    __slots__ = ["file_name", "context"]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    context: _base_pb2.Context
    def __init__(
        self, file_name: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class UploadXlsxResponse(_message.Message):
    __slots__ = ["response_standard", "result"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    result: UploadFile
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        result: _Optional[_Union[UploadFile, _Mapping]] = ...,
    ) -> None: ...
