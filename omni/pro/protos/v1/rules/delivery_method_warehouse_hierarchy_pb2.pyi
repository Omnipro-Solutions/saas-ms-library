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

class DeliveryMethodWarehouseHierarchy(_message.Message):
    __slots__ = ["id", "delivery_method_warehouse_id", "warehouse_hierarchy_id", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_HIERARCHY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    delivery_method_warehouse_id: int
    warehouse_hierarchy_id: int
    active: bool
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        delivery_method_warehouse_id: _Optional[int] = ...,
        warehouse_hierarchy_id: _Optional[int] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseHierarchyCreateRequest(_message.Message):
    __slots__ = ["delivery_method_warehouse_id", "warehouse_hierarchy_id", "context"]
    DELIVERY_METHOD_WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_HIERARCHY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_method_warehouse_id: int
    warehouse_hierarchy_id: int
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_method_warehouse_id: _Optional[int] = ...,
        warehouse_hierarchy_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseHierarchyCreateResponse(_message.Message):
    __slots__ = ["delivery_method_warehouse_hierarchy", "response_standard"]
    DELIVERY_METHOD_WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method_warehouse_hierarchy: DeliveryMethodWarehouseHierarchy
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_method_warehouse_hierarchy: _Optional[_Union[DeliveryMethodWarehouseHierarchy, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseHierarchyReadRequest(_message.Message):
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

class DeliveryMethodWarehouseHierarchyReadResponse(_message.Message):
    __slots__ = ["delivery_method_warehouse_hierarchys", "meta_data", "response_standard"]
    DELIVERY_METHOD_WAREHOUSE_HIERARCHYS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method_warehouse_hierarchys: _containers.RepeatedCompositeFieldContainer[DeliveryMethodWarehouseHierarchy]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_method_warehouse_hierarchys: _Optional[
            _Iterable[_Union[DeliveryMethodWarehouseHierarchy, _Mapping]]
        ] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseHierarchyUpdateRequest(_message.Message):
    __slots__ = ["delivery_method_warehouse_hierarchy", "context"]
    DELIVERY_METHOD_WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_method_warehouse_hierarchy: DeliveryMethodWarehouseHierarchy
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_method_warehouse_hierarchy: _Optional[_Union[DeliveryMethodWarehouseHierarchy, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseHierarchyUpdateResponse(_message.Message):
    __slots__ = ["delivery_method_warehouse_hierarchy", "response_standard"]
    DELIVERY_METHOD_WAREHOUSE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method_warehouse_hierarchy: DeliveryMethodWarehouseHierarchy
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_method_warehouse_hierarchy: _Optional[_Union[DeliveryMethodWarehouseHierarchy, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodWarehouseHierarchyDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryMethodWarehouseHierarchyDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
