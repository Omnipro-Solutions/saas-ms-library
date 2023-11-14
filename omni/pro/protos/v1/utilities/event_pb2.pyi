from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.utilities import model_pb2 as _model_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ["id", "name", "code", "model", "operation", "active", "external_id", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    model: _model_pb2.Model
    operation: str
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        model: _Optional[_Union[_model_pb2.Model, _Mapping]] = ...,
        operation: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class EventCreateRequest(_message.Message):
    __slots__ = ["name", "code", "model_id", "operation", "external_id", "context"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    model_id: str
    operation: str
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        model_id: _Optional[str] = ...,
        operation: _Optional[str] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class EventCreateResponse(_message.Message):
    __slots__ = ["response_standard", "event"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    event: Event
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        event: _Optional[_Union[Event, _Mapping]] = ...,
    ) -> None: ...

class EventReadRequest(_message.Message):
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

class EventReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "events"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...,
    ) -> None: ...

class EventUpdateRequest(_message.Message):
    __slots__ = ["event", "context"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    event: Event
    context: _base_pb2.Context
    def __init__(
        self,
        event: _Optional[_Union[Event, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class EventUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "event"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    event: Event
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        event: _Optional[_Union[Event, _Mapping]] = ...,
    ) -> None: ...

class EventDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class EventDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
