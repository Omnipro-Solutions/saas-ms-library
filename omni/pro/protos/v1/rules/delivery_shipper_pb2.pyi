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
from omni.pro.protos.v1.rules import carrier_pb2 as _carrier_pb2
from omni.pro.protos.v1.rules import delivery_locality_pb2 as _delivery_locality_pb2
from omni.pro.protos.v1.rules import delivery_method_pb2 as _delivery_method_pb2
from omni.pro.protos.v1.rules import schedule_work_pb2 as _schedule_work_pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryShipper(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "delivery_carrier",
        "delivery_methods",
        "maximum_weight",
        "maximum_volume",
        "schedule_pickup",
        "locality_available",
        "internal_transfer",
        "warehouses",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_CARRIER_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHODS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_VOLUME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_PICKUP_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    delivery_carrier: _carrier_pb2.Carrier
    delivery_methods: _containers.RepeatedCompositeFieldContainer[_delivery_method_pb2.DeliveryMethod]
    maximum_weight: float
    maximum_volume: float
    schedule_pickup: _schedule_work_pb2.ScheduleWork
    locality_available: _delivery_locality_pb2.DeliveryLocality
    internal_transfer: _wrappers_pb2.BoolValue
    warehouses: _containers.RepeatedCompositeFieldContainer[_warehouse_pb2.Warehouse]
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        delivery_carrier: _Optional[_Union[_carrier_pb2.Carrier, _Mapping]] = ...,
        delivery_methods: _Optional[_Iterable[_Union[_delivery_method_pb2.DeliveryMethod, _Mapping]]] = ...,
        maximum_weight: _Optional[float] = ...,
        maximum_volume: _Optional[float] = ...,
        schedule_pickup: _Optional[_Union[_schedule_work_pb2.ScheduleWork, _Mapping]] = ...,
        locality_available: _Optional[_Union[_delivery_locality_pb2.DeliveryLocality, _Mapping]] = ...,
        internal_transfer: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouses: _Optional[_Iterable[_Union[_warehouse_pb2.Warehouse, _Mapping]]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "delivery_carrier_id",
        "delivery_method_ids",
        "maximum_weight",
        "maximum_volume",
        "schedule_pickup_id",
        "locality_available_id",
        "internal_transfer",
        "warehouse_ids",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_CARRIER_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_IDS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_VOLUME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_PICKUP_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    delivery_carrier_id: int
    delivery_method_ids: _containers.RepeatedScalarFieldContainer[str]
    maximum_weight: float
    maximum_volume: float
    schedule_pickup_id: str
    locality_available_id: str
    internal_transfer: _wrappers_pb2.BoolValue
    warehouse_ids: _containers.RepeatedScalarFieldContainer[int]
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        delivery_carrier_id: _Optional[int] = ...,
        delivery_method_ids: _Optional[_Iterable[str]] = ...,
        maximum_weight: _Optional[float] = ...,
        maximum_volume: _Optional[float] = ...,
        schedule_pickup_id: _Optional[str] = ...,
        locality_available_id: _Optional[str] = ...,
        internal_transfer: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouse_ids: _Optional[_Iterable[int]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperCreateResponse(_message.Message):
    __slots__ = ["delivery_shipper", "response_standard"]
    DELIVERY_SHIPPER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_shipper: DeliveryShipper
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_shipper: _Optional[_Union[DeliveryShipper, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperReadRequest(_message.Message):
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

class DeliveryShipperReadResponse(_message.Message):
    __slots__ = ["delivery_shippers", "meta_data", "response_standard"]
    DELIVERY_SHIPPERS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_shippers: _containers.RepeatedCompositeFieldContainer[DeliveryShipper]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_shippers: _Optional[_Iterable[_Union[DeliveryShipper, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperUpdateRequest(_message.Message):
    __slots__ = ["delivery_shipper", "context"]
    DELIVERY_SHIPPER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_shipper: DeliveryShipper
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_shipper: _Optional[_Union[DeliveryShipper, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperUpdateResponse(_message.Message):
    __slots__ = ["delivery_shipper", "response_standard"]
    DELIVERY_SHIPPER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_shipper: DeliveryShipper
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_shipper: _Optional[_Union[DeliveryShipper, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryShipperDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
