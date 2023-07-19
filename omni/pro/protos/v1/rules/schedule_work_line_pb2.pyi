from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Day(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    MONDAY: _ClassVar[Day]
    TUESDAY: _ClassVar[Day]
    WEDNESDAY: _ClassVar[Day]
    THURSDAY: _ClassVar[Day]
    FRIDAY: _ClassVar[Day]
    SATURDAY: _ClassVar[Day]
    SUNDAY: _ClassVar[Day]

MONDAY: Day
TUESDAY: Day
WEDNESDAY: Day
THURSDAY: Day
FRIDAY: Day
SATURDAY: Day
SUNDAY: Day

class ScheduleWorkLine(_message.Message):
    __slots__ = ["id", "day", "opening_time", "closing_time", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    OPENING_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOSING_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    day: Day
    opening_time: _timestamp_pb2.Timestamp
    closing_time: _timestamp_pb2.Timestamp
    active: bool
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        day: _Optional[_Union[Day, str]] = ...,
        opening_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        closing_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkLineCreateRequest(_message.Message):
    __slots__ = ["day", "opening_time", "closing_time", "context"]
    DAY_FIELD_NUMBER: _ClassVar[int]
    OPENING_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOSING_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    day: Day
    opening_time: _timestamp_pb2.Timestamp
    closing_time: _timestamp_pb2.Timestamp
    context: _base_pb2.Context
    def __init__(
        self,
        day: _Optional[_Union[Day, str]] = ...,
        opening_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        closing_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkLineCreateResponse(_message.Message):
    __slots__ = ["schedule_work_line", "response_standard"]
    SCHEDULE_WORK_LINE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    schedule_work_line: ScheduleWorkLine
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        schedule_work_line: _Optional[_Union[ScheduleWorkLine, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkLineReadRequest(_message.Message):
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

class ScheduleWorkLineReadResponse(_message.Message):
    __slots__ = ["schedule_work_lines", "meta_data", "response_standard"]
    SCHEDULE_WORK_LINES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    schedule_work_lines: _containers.RepeatedCompositeFieldContainer[ScheduleWorkLine]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        schedule_work_lines: _Optional[_Iterable[_Union[ScheduleWorkLine, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkLineUpdateRequest(_message.Message):
    __slots__ = ["schedule_work_line", "context"]
    SCHEDULE_WORK_LINE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    schedule_work_line: ScheduleWorkLine
    context: _base_pb2.Context
    def __init__(
        self,
        schedule_work_line: _Optional[_Union[ScheduleWorkLine, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkLineUpdateResponse(_message.Message):
    __slots__ = ["schedule_work_line", "response_standard"]
    SCHEDULE_WORK_LINE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    schedule_work_line: ScheduleWorkLine
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        schedule_work_line: _Optional[_Union[ScheduleWorkLine, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ScheduleWorkLineDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ScheduleWorkLineDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
