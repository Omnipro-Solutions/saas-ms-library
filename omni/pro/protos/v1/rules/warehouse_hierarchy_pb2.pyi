from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.rules import location_pb2 as _location_pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class WarehouseHierarchy(_message.Message):
    __slots__ = [
        "id",
        "warehouse_id",
        "location_id",
        "quantity_security",
        "sequence",
        "sequence_order",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SECURITY_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ORDER_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    warehouse_id: _warehouse_pb2.Warehouse
    location_id: _location_pb2.Location
    quantity_security: float
    sequence: int
    sequence_order: bool
    active: bool
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        warehouse_id: _Optional[_Union[_warehouse_pb2.Warehouse, _Mapping]] = ...,
        location_id: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        quantity_security: _Optional[float] = ...,
        sequence: _Optional[int] = ...,
        sequence_order: bool = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class WarehouseHierarchyCreateRequest(_message.Message):
    __slots__ = ["warehouse_id", "location_id", "quantity_security", "sequence", "sequence_order", "context"]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SECURITY_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ORDER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    warehouse_id: str
    location_id: str
    quantity_security: float
    sequence: int
    sequence_order: bool
    context: _base_pb2.Context
    def __init__(
        self,
        warehouse_id: _Optional[str] = ...,
        location_id: _Optional[str] = ...,
        quantity_security: _Optional[float] = ...,
        sequence: _Optional[int] = ...,
        sequence_order: bool = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class WarehouseHierarchyCreateResponse(_message.Message):
    __slots__ = ["warehouse_hierarchy", "response_standard"]
    WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    warehouse_hierarchy: WarehouseHierarchy
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        warehouse_hierarchy: _Optional[_Union[WarehouseHierarchy, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class WarehouseHierarchyReadRequest(_message.Message):
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

class WarehouseHierarchyReadResponse(_message.Message):
    __slots__ = ["warehouses_hierarchy", "meta_data", "response_standard"]
    WAREHOUSES_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    warehouses_hierarchy: _containers.RepeatedCompositeFieldContainer[WarehouseHierarchy]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        warehouses_hierarchy: _Optional[_Iterable[_Union[WarehouseHierarchy, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class WarehouseHierarchyUpdateRequest(_message.Message):
    __slots__ = ["warehouse_hierarchy", "context"]
    WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    warehouse_hierarchy: WarehouseHierarchy
    context: _base_pb2.Context
    def __init__(
        self,
        warehouse_hierarchy: _Optional[_Union[WarehouseHierarchy, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class WarehouseHierarchyUpdateResponse(_message.Message):
    __slots__ = ["warehouse_hierarchy", "response_standard"]
    WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    warehouse_hierarchy: WarehouseHierarchy
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        warehouse_hierarchy: _Optional[_Union[WarehouseHierarchy, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class WarehouseHierarchyDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class WarehouseHierarchyDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
