from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.rules import warehouse_hierarchy_pb2 as _warehouse_hierarchy_pb2

ASC: SortBy
DESC: SortBy
DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryMethodWarehouse(_message.Message):
    __slots__ = ["active", "hierarchi_warehouse_sort_by", "id", "name", "object_audit", "transfer_warehouse_ids"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    HIERARCHI_WAREHOUSE_SORT_BY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    active: bool
    hierarchi_warehouse_sort_by: SortBy
    id: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    transfer_warehouse_ids: _containers.RepeatedCompositeFieldContainer[_warehouse_hierarchy_pb2.WarehouseHierarchy]
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        hierarchi_warehouse_sort_by: _Optional[_Union[SortBy, str]] = ...,
        transfer_warehouse_ids: _Optional[
            _Iterable[_Union[_warehouse_hierarchy_pb2.WarehouseHierarchy, _Mapping]]
        ] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseCreateRequest(_message.Message):
    __slots__ = ["context", "hierarchi_warehouse_sort_by", "name", "transfer_warehouse_ids"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    HIERARCHI_WAREHOUSE_SORT_BY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    hierarchi_warehouse_sort_by: SortBy
    name: str
    transfer_warehouse_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        transfer_warehouse_ids: _Optional[_Iterable[str]] = ...,
        hierarchi_warehouse_sort_by: _Optional[_Union[SortBy, str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseCreateResponse(_message.Message):
    __slots__ = ["delivery_method_warehouse", "response_standard"]
    DELIVERY_METHOD_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method_warehouse: DeliveryMethodWarehouse
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_method_warehouse: _Optional[_Union[DeliveryMethodWarehouse, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: str
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryMethodWarehouseDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryMethodWarehouseReadRequest(_message.Message):
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

class DeliveryMethodWarehouseReadResponse(_message.Message):
    __slots__ = ["delivery_method_warehouses", "meta_data", "response_standard"]
    DELIVERY_METHOD_WAREHOUSES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method_warehouses: _containers.RepeatedCompositeFieldContainer[DeliveryMethodWarehouse]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_method_warehouses: _Optional[_Iterable[_Union[DeliveryMethodWarehouse, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseUpdateRequest(_message.Message):
    __slots__ = ["context", "delivery_method_warehouse"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_method_warehouse: DeliveryMethodWarehouse
    def __init__(
        self,
        delivery_method_warehouse: _Optional[_Union[DeliveryMethodWarehouse, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseUpdateResponse(_message.Message):
    __slots__ = ["delivery_method_warehouse", "response_standard"]
    DELIVERY_METHOD_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method_warehouse: DeliveryMethodWarehouse
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_method_warehouse: _Optional[_Union[DeliveryMethodWarehouse, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class SortBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
