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
from omni.pro.protos.v1.rules import delivery_method_pb2 as _delivery_method_pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class TimeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN: _ClassVar[TimeType]
    MINUTES: _ClassVar[TimeType]
    HOURS: _ClassVar[TimeType]
    DAYS: _ClassVar[TimeType]

UNKNOWN: TimeType
MINUTES: TimeType
HOURS: TimeType
DAYS: TimeType

class DeliveryShipper(_message.Message):
    __slots__ = [
        "id",
        "name",
        "delivery_method_ids",
        "warehouse_ids",
        "locality_available_id",
        "time_type",
        "value_min",
        "value_max",
        "inversely",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_IDS_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_MIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_MAX_FIELD_NUMBER: _ClassVar[int]
    INVERSELY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    delivery_method_ids: _containers.RepeatedCompositeFieldContainer[_delivery_method_pb2.DeliveryMethod]
    warehouse_ids: _containers.RepeatedCompositeFieldContainer[_warehouse_pb2.Warehouse]
    locality_available_id: str
    time_type: TimeType
    value_min: str
    value_max: str
    inversely: bool
    active: bool
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        delivery_method_ids: _Optional[_Iterable[_Union[_delivery_method_pb2.DeliveryMethod, _Mapping]]] = ...,
        warehouse_ids: _Optional[_Iterable[_Union[_warehouse_pb2.Warehouse, _Mapping]]] = ...,
        locality_available_id: _Optional[str] = ...,
        time_type: _Optional[_Union[TimeType, str]] = ...,
        value_min: _Optional[str] = ...,
        value_max: _Optional[str] = ...,
        inversely: bool = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryShipperCreateRequest(_message.Message):
    __slots__ = ["name", "locality_available_id", "time_type", "value_min", "value_max", "inversely", "context"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_MIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_MAX_FIELD_NUMBER: _ClassVar[int]
    INVERSELY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    locality_available_id: str
    time_type: TimeType
    value_min: str
    value_max: str
    inversely: bool
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        locality_available_id: _Optional[str] = ...,
        time_type: _Optional[_Union[TimeType, str]] = ...,
        value_min: _Optional[str] = ...,
        value_max: _Optional[str] = ...,
        inversely: bool = ...,
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
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryShipperDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
