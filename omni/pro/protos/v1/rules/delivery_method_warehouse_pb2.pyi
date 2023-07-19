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

DESCRIPTOR: _descriptor.FileDescriptor

class SortBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ASC: _ClassVar[SortBy]
    DESC: _ClassVar[SortBy]

ASC: SortBy
DESC: SortBy

class DeliveryMethodWarehouse(_message.Message):
    __slots__ = ["id", "name", "hierarchi_warehouse_sort_by", "transfer_warehouse_ids", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HIERARCHI_WAREHOUSE_SORT_BY_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    hierarchi_warehouse_sort_by: SortBy
    transfer_warehouse_ids: _containers.RepeatedCompositeFieldContainer[_warehouse_hierarchy_pb2.WarehouseHierarchy]
    active: bool
    object_audit: _base_pb2.ObjectAudit
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
    __slots__ = ["name", "transfer_warehouse_ids", "hierarchi_warehouse_sort_by", "context"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    HIERARCHI_WAREHOUSE_SORT_BY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    transfer_warehouse_ids: _containers.RepeatedScalarFieldContainer[str]
    hierarchi_warehouse_sort_by: SortBy
    context: _base_pb2.Context
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

class DeliveryMethodWarehouseReadRequest(_message.Message):
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
    __slots__ = ["delivery_method_warehouse", "context"]
    DELIVERY_METHOD_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_method_warehouse: DeliveryMethodWarehouse
    context: _base_pb2.Context
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

class DeliveryMethodWarehouseDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryMethodWarehouseDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
