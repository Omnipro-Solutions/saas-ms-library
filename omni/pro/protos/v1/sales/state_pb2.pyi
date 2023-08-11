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

DESCRIPTOR: _descriptor.FileDescriptor

class State(_message.Message):
    __slots__ = ["id", "name", "code", "flow_id", "type", "description", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    code: str
    flow_id: int
    type: str
    description: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        flow_id: _Optional[int] = ...,
        type: _Optional[str] = ...,
        description: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class StateCreateRequest(_message.Message):
    __slots__ = ["name", "code", "flow_id", "type", "description", "context"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    flow_id: int
    type: str
    description: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        flow_id: _Optional[int] = ...,
        type: _Optional[str] = ...,
        description: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class StateCreateResponse(_message.Message):
    __slots__ = ["state", "response_standard"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    state: State
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        state: _Optional[_Union[State, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class StateReadRequest(_message.Message):
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
    id: int
    context: _base_pb2.Context
    def __init__(
        self,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class StateReadResponse(_message.Message):
    __slots__ = ["states", "meta_data", "response_standard"]
    STATES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedCompositeFieldContainer[State]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        states: _Optional[_Iterable[_Union[State, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class StateUpdateRequest(_message.Message):
    __slots__ = ["state", "context"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    state: State
    context: _base_pb2.Context
    def __init__(
        self,
        state: _Optional[_Union[State, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class StateUpdateResponse(_message.Message):
    __slots__ = ["state", "response_standard"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    state: State
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        state: _Optional[_Union[State, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class StateDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class StateDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
