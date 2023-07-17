from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.rules import schedule_work_pb2 as _schedule_work_pb2
from omni.pro.protos.v1.rules import warehouse_hierarchy_pb2 as _warehouse_hierarchy_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeliverySchedule(_message.Message):
    __slots__ = ["active", "id", "name", "object_audit", "schedule_work_id", "transfer_warehouse_ids"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    active: bool
    id: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    schedule_work_id: _schedule_work_pb2.ScheduleWork
    transfer_warehouse_ids: _containers.RepeatedCompositeFieldContainer[_warehouse_hierarchy_pb2.WarehouseHierarchy]
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        schedule_work_id: _Optional[_Union[_schedule_work_pb2.ScheduleWork, _Mapping]] = ...,
        transfer_warehouse_ids: _Optional[
            _Iterable[_Union[_warehouse_hierarchy_pb2.WarehouseHierarchy, _Mapping]]
        ] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleCreateRequest(_message.Message):
    __slots__ = ["context", "name", "schedule_work_id", "transfer_warehouse_ids"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_WORK_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    name: str
    schedule_work_id: str
    transfer_warehouse_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        schedule_work_id: _Optional[str] = ...,
        transfer_warehouse_ids: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleCreateResponse(_message.Message):
    __slots__ = ["delivery_schedule", "response_standard"]
    DELIVERY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_schedule: DeliverySchedule
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_schedule: _Optional[_Union[DeliverySchedule, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: str
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryScheduleDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryScheduleReadRequest(_message.Message):
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

class DeliveryScheduleReadResponse(_message.Message):
    __slots__ = ["delivery_schedules", "meta_data", "response_standard"]
    DELIVERY_SCHEDULES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_schedules: _containers.RepeatedCompositeFieldContainer[DeliverySchedule]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_schedules: _Optional[_Iterable[_Union[DeliverySchedule, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleUpdateRequest(_message.Message):
    __slots__ = ["context", "delivery_schedule"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_schedule: DeliverySchedule
    def __init__(
        self,
        delivery_schedule: _Optional[_Union[DeliverySchedule, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleUpdateResponse(_message.Message):
    __slots__ = ["delivery_schedule", "response_standard"]
    DELIVERY_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_schedule: DeliverySchedule
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_schedule: _Optional[_Union[DeliverySchedule, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
