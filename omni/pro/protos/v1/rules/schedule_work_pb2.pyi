from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.rules import calendar_pb2 as _calendar_pb2
from omni.pro.protos.v1.rules import schedule_work_line_pb2 as _schedule_work_line_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ScheduleWork(_message.Message):
    __slots__ = ["active", "calendar_id", "id", "name", "object_audit", "schedule_work_line_ids"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_WORK_LINE_IDS_FIELD_NUMBER: _ClassVar[int]
    active: bool
    calendar_id: _calendar_pb2.Calendar
    id: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    schedule_work_line_ids: _containers.RepeatedCompositeFieldContainer[_schedule_work_line_pb2.ScheduleWorkLine]
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        calendar_id: _Optional[_Union[_calendar_pb2.Calendar, _Mapping]] = ...,
        schedule_work_line_ids: _Optional[_Iterable[_Union[_schedule_work_line_pb2.ScheduleWorkLine, _Mapping]]] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkCreateRequest(_message.Message):
    __slots__ = ["calendar_id", "context", "name", "schedule_work_line_ids"]
    CALENDAR_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_WORK_LINE_IDS_FIELD_NUMBER: _ClassVar[int]
    calendar_id: str
    context: _base_pb2.Context
    name: str
    schedule_work_line_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        calendar_id: _Optional[str] = ...,
        schedule_work_line_ids: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkCreateResponse(_message.Message):
    __slots__ = ["response_standard", "schedule_work"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_WORK_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    schedule_work: ScheduleWork
    def __init__(
        self,
        schedule_work: _Optional[_Union[ScheduleWork, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: str
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ScheduleWorkDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class ScheduleWorkReadRequest(_message.Message):
    __slots__ = ["context", "fields", "filter", "group_by", "id", "paginated", "sort_by"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    id: str
    paginated: _base_pb2.Paginated
    sort_by: _base_pb2.SortBy
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

class ScheduleWorkReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "schedules_work"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    SCHEDULES_WORK_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    schedules_work: _containers.RepeatedCompositeFieldContainer[ScheduleWork]
    def __init__(
        self,
        schedules_work: _Optional[_Iterable[_Union[ScheduleWork, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkUpdateRequest(_message.Message):
    __slots__ = ["context", "schedule_work"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_WORK_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    schedule_work: ScheduleWork
    def __init__(
        self,
        schedule_work: _Optional[_Union[ScheduleWork, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "schedule_work"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_WORK_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    schedule_work: ScheduleWork
    def __init__(
        self,
        schedule_work: _Optional[_Union[ScheduleWork, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
