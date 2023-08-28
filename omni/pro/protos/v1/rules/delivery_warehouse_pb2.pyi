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
from omni.pro.protos.v1.rules import warehouse_hierarchy_pb2 as _warehouse_hierarchy_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryWarehouse(_message.Message):
    __slots__ = ["id", "name", "hierarchy_warehouse_sort_by", "transfer_warehouses", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_WAREHOUSE_SORT_BY_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_WAREHOUSES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    hierarchy_warehouse_sort_by: str
    transfer_warehouses: _containers.RepeatedCompositeFieldContainer[_warehouse_hierarchy_pb2.WarehouseHierarchy]
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        hierarchy_warehouse_sort_by: _Optional[str] = ...,
        transfer_warehouses: _Optional[_Iterable[_Union[_warehouse_hierarchy_pb2.WarehouseHierarchy, _Mapping]]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryWarehouseCreateRequest(_message.Message):
    __slots__ = ["name", "hierarchy_warehouse_sort_by", "transfer_warehouse_ids", "context"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HIERARCHY_WAREHOUSE_SORT_BY_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    hierarchy_warehouse_sort_by: str
    transfer_warehouse_ids: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        hierarchy_warehouse_sort_by: _Optional[str] = ...,
        transfer_warehouse_ids: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryWarehouseCreateResponse(_message.Message):
    __slots__ = ["delivery_warehouse", "response_standard"]
    DELIVERY_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_warehouse: DeliveryWarehouse
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_warehouse: _Optional[_Union[DeliveryWarehouse, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryWarehouseReadRequest(_message.Message):
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

class DeliveryWarehouseReadResponse(_message.Message):
    __slots__ = ["delivery_warehouses", "meta_data", "response_standard"]
    DELIVERY_WAREHOUSES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_warehouses: _containers.RepeatedCompositeFieldContainer[DeliveryWarehouse]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_warehouses: _Optional[_Iterable[_Union[DeliveryWarehouse, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryWarehouseUpdateRequest(_message.Message):
    __slots__ = ["delivery_warehouse", "context"]
    DELIVERY_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_warehouse: DeliveryWarehouse
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_warehouse: _Optional[_Union[DeliveryWarehouse, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryWarehouseUpdateResponse(_message.Message):
    __slots__ = ["delivery_warehouse", "response_standard"]
    DELIVERY_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_warehouse: DeliveryWarehouse
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_warehouse: _Optional[_Union[DeliveryWarehouse, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryWarehouseDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryWarehouseDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class AddTransferWarehouseRequest(_message.Message):
    __slots__ = ["delivery_warehouse_id", "warehouse_herarchy_ids", "context"]
    DELIVERY_WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_HERARCHY_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_warehouse_id: str
    warehouse_herarchy_ids: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_warehouse_id: _Optional[str] = ...,
        warehouse_herarchy_ids: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddTransferWarehouseResponse(_message.Message):
    __slots__ = ["delivery_warehouse", "response_standard"]
    DELIVERY_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_warehouse: DeliveryWarehouse
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_warehouse: _Optional[_Union[DeliveryWarehouse, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class RemoveTransferWarehouseRequest(_message.Message):
    __slots__ = ["delivery_warehouse_id", "warehouse_herarchy_ids", "context"]
    DELIVERY_WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_HERARCHY_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_warehouse_id: str
    warehouse_herarchy_ids: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_warehouse_id: _Optional[str] = ...,
        warehouse_herarchy_ids: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RemoveTransferWarehouseResponse(_message.Message):
    __slots__ = ["delivery_warehouse", "response_standard"]
    DELIVERY_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_warehouse: DeliveryWarehouse
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_warehouse: _Optional[_Union[DeliveryWarehouse, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
