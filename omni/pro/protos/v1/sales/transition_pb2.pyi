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
from omni.pro.protos.v1.sales import flow_pb2 as _flow_pb2
from omni.pro.protos.v1.sales import state_pb2 as _state_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Transition(_message.Message):
    __slots__ = [
        "id",
        "flow",
        "source_state",
        "destination_state",
        "trigger",
        "description",
        "logic",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    SOURCE_STATE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_STATE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOGIC_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    flow: _flow_pb2.Flow
    source_state: _state_pb2.State
    destination_state: _state_pb2.State
    trigger: str
    description: str
    logic: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        flow: _Optional[_Union[_flow_pb2.Flow, _Mapping]] = ...,
        source_state: _Optional[_Union[_state_pb2.State, _Mapping]] = ...,
        destination_state: _Optional[_Union[_state_pb2.State, _Mapping]] = ...,
        trigger: _Optional[str] = ...,
        description: _Optional[str] = ...,
        logic: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class TransitionCreateRequest(_message.Message):
    __slots__ = ["flow_id", "source_state_id", "destination_state_id", "trigger", "description", "logic", "context"]
    FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_STATE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_STATE_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOGIC_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    flow_id: int
    source_state_id: int
    destination_state_id: int
    trigger: str
    description: str
    logic: str
    context: _base_pb2.Context
    def __init__(
        self,
        flow_id: _Optional[int] = ...,
        source_state_id: _Optional[int] = ...,
        destination_state_id: _Optional[int] = ...,
        trigger: _Optional[str] = ...,
        description: _Optional[str] = ...,
        logic: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class TransitionCreateResponse(_message.Message):
    __slots__ = ["transition", "response_standard"]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    transition: Transition
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        transition: _Optional[_Union[Transition, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class TransitionReadRequest(_message.Message):
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

class TransitionReadResponse(_message.Message):
    __slots__ = ["transitions", "meta_data", "response_standard"]
    TRANSITIONS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    transitions: _containers.RepeatedCompositeFieldContainer[Transition]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        transitions: _Optional[_Iterable[_Union[Transition, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class TransitionUpdateRequest(_message.Message):
    __slots__ = ["transition", "context"]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    transition: Transition
    context: _base_pb2.Context
    def __init__(
        self,
        transition: _Optional[_Union[Transition, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class TransitionUpdateResponse(_message.Message):
    __slots__ = ["transition", "response_standard"]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    transition: Transition
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        transition: _Optional[_Union[Transition, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class TransitionDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class TransitionDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
