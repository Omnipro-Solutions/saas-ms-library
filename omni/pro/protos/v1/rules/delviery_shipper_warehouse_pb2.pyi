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

class DeliveryShipperWarehouse(_message.Message):
    __slots__ = ["active", "delivery_shipper_id", "id", "object_audit", "warehouse_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SHIPPER_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    delivery_shipper_id: int
    id: int
    object_audit: _base_pb2.ObjectAudit
    warehouse_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        delivery_shipper_id: _Optional[int] = ...,
        warehouse_id: _Optional[int] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperWarehouseCreateRequest(_message.Message):
    __slots__ = ["context", "delivery_shipper_id", "warehouse_id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SHIPPER_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_shipper_id: int
    warehouse_id: int
    def __init__(
        self,
        delivery_shipper_id: _Optional[int] = ...,
        warehouse_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperWarehouseCreateResponse(_message.Message):
    __slots__ = ["delivery_shipper_warehouse", "response_standard"]
    DELIVERY_SHIPPER_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_shipper_warehouse: DeliveryShipperWarehouse
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_shipper_warehouse: _Optional[_Union[DeliveryShipperWarehouse, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperWarehouseDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryShipperWarehouseDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryShipperWarehouseReadRequest(_message.Message):
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

class DeliveryShipperWarehouseReadResponse(_message.Message):
    __slots__ = ["delivery_shipper_warehouse", "meta_data", "response_standard"]
    DELIVERY_SHIPPER_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_shipper_warehouse: _containers.RepeatedCompositeFieldContainer[DeliveryShipperWarehouse]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_shipper_warehouse: _Optional[_Iterable[_Union[DeliveryShipperWarehouse, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperWarehouseUpdateRequest(_message.Message):
    __slots__ = ["context", "delivery_shipper_warehouse"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_SHIPPER_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_shipper_warehouse: DeliveryShipperWarehouse
    def __init__(
        self,
        delivery_shipper_warehouse: _Optional[_Union[DeliveryShipperWarehouse, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperWarehouseUpdateResponse(_message.Message):
    __slots__ = ["delivery_shipper_warehouse", "response_standard"]
    DELIVERY_SHIPPER_WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_shipper_warehouse: DeliveryShipperWarehouse
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_shipper_warehouse: _Optional[_Union[DeliveryShipperWarehouse, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
