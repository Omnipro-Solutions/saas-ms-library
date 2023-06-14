from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryScheduleWarehouseHierarchy(_message.Message):
    __slots__ = ["active", "delivery_schedule_id", "id", "object_audit", "warehouse_hierarchy_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_HIERARCHY_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    delivery_schedule_id: int
    id: int
    object_audit: _base_pb2.ObjectAudit
    warehouse_hierarchy_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        delivery_schedule_id: _Optional[int] = ...,
        warehouse_hierarchy_id: _Optional[int] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleWarehouseHierarchyCreateRequest(_message.Message):
    __slots__ = ["context", "delivery_schedule_id", "warehouse_hierarchy_id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_HIERARCHY_ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_schedule_id: int
    warehouse_hierarchy_id: int
    def __init__(
        self,
        delivery_schedule_id: _Optional[int] = ...,
        warehouse_hierarchy_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleWarehouseHierarchyCreateResponse(_message.Message):
    __slots__ = ["delivery_schedule_warehouse_hierarchy", "response_standard"]
    DELIVERY_SCHEDULE_WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_schedule_warehouse_hierarchy: DeliveryScheduleWarehouseHierarchy
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_schedule_warehouse_hierarchy: _Optional[_Union[DeliveryScheduleWarehouseHierarchy, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleWarehouseHierarchyDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryScheduleWarehouseHierarchyDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryScheduleWarehouseHierarchyReadRequest(_message.Message):
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
    id: int
    paginated: _base_pb2.Paginated
    sort_by: _base_pb2.SortBy
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

class DeliveryScheduleWarehouseHierarchyReadResponse(_message.Message):
    __slots__ = ["delivery_schedule_warehouse_hierarchy", "meta_data", "response_standard"]
    DELIVERY_SCHEDULE_WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_schedule_warehouse_hierarchy: _containers.RepeatedCompositeFieldContainer[
        DeliveryScheduleWarehouseHierarchy
    ]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_schedule_warehouse_hierarchy: _Optional[
            _Iterable[_Union[DeliveryScheduleWarehouseHierarchy, _Mapping]]
        ] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleWarehouseHierarchyUpdateRequest(_message.Message):
    __slots__ = ["context", "delivery_schedule_warehouse_hierarchy"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SCHEDULE_WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_schedule_warehouse_hierarchy: DeliveryScheduleWarehouseHierarchy
    def __init__(
        self,
        delivery_schedule_warehouse_hierarchy: _Optional[_Union[DeliveryScheduleWarehouseHierarchy, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryScheduleWarehouseHierarchyUpdateResponse(_message.Message):
    __slots__ = ["delivery_schedule_warehouse_hierarchy", "response_standard"]
    DELIVERY_SCHEDULE_WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_schedule_warehouse_hierarchy: DeliveryScheduleWarehouseHierarchy
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_schedule_warehouse_hierarchy: _Optional[_Union[DeliveryScheduleWarehouseHierarchy, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
