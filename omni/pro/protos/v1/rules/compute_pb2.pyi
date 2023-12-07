from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Compute(_message.Message):
    __slots__ = [
        "id",
        "data_request",
        "data_process",
        "data_response_internal",
        "data_response_external",
        "time",
        "date_created",
        "active",
        "external_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DATA_PROCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_RESPONSE_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    DATA_RESPONSE_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    data_request: _struct_pb2.Struct
    data_process: _struct_pb2.Struct
    data_response_internal: _struct_pb2.Struct
    data_response_external: _struct_pb2.Struct
    time: float
    date_created: _timestamp_pb2.Timestamp
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        data_request: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        data_process: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        data_response_internal: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        data_response_external: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        time: _Optional[float] = ...,
        date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class ComputeCreateRequest(_message.Message):
    __slots__ = [
        "data_request",
        "data_process",
        "data_response_internal",
        "data_response_external",
        "time",
        "date_created",
        "external_id",
        "context",
    ]
    DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DATA_PROCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_RESPONSE_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    DATA_RESPONSE_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    data_request: _struct_pb2.Struct
    data_process: _struct_pb2.Struct
    data_response_internal: _struct_pb2.Struct
    data_response_external: _struct_pb2.Struct
    time: float
    date_created: _timestamp_pb2.Timestamp
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        data_request: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        data_process: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        data_response_internal: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        data_response_external: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        time: _Optional[float] = ...,
        date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ComputeCreateResponse(_message.Message):
    __slots__ = ["response_standard", "compute"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    compute: Compute
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        compute: _Optional[_Union[Compute, _Mapping]] = ...,
    ) -> None: ...

class ComputeReadRequest(_message.Message):
    __slots__ = ["group_by", "sort_by", "fields", "filter", "paginated", "id", "context"]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    id: str
    context: _base_pb2.Context
    def __init__(
        self,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ComputeReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "compute"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    compute: _containers.RepeatedCompositeFieldContainer[Compute]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        compute: _Optional[_Iterable[_Union[Compute, _Mapping]]] = ...,
    ) -> None: ...

class ComputeUpdateRequest(_message.Message):
    __slots__ = ["compute", "context"]
    COMPUTE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    compute: Compute
    context: _base_pb2.Context
    def __init__(
        self,
        compute: _Optional[_Union[Compute, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ComputeUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "compute"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    compute: Compute
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        compute: _Optional[_Union[Compute, _Mapping]] = ...,
    ) -> None: ...

class ComputeDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ComputeDeleteResponse(_message.Message):
    __slots__ = ["response_standard", "compute"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    compute: Compute
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        compute: _Optional[_Union[Compute, _Mapping]] = ...,
    ) -> None: ...
