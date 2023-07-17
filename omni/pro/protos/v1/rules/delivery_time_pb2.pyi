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

DAYS: TimeType
DESCRIPTOR: _descriptor.FileDescriptor
HOURS: TimeType
MINUTES: TimeType
UNKNOWN: TimeType

class DeliveryTime(_message.Message):
    __slots__ = [
        "active",
        "delivery_method_ids",
        "id",
        "inversely",
        "locality_available_id",
        "name",
        "object_audit",
        "time_type",
        "value_max",
        "value_min",
        "warehouse_ids",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INVERSELY_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_MAX_FIELD_NUMBER: _ClassVar[int]
    VALUE_MIN_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    active: bool
    delivery_method_ids: _containers.RepeatedCompositeFieldContainer[_delivery_method_pb2.DeliveryMethod]
    id: str
    inversely: bool
    locality_available_id: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    time_type: TimeType
    value_max: str
    value_min: str
    warehouse_ids: _containers.RepeatedCompositeFieldContainer[_warehouse_pb2.Warehouse]
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

class DeliveryTimeCreateRequest(_message.Message):
    __slots__ = ["context", "inversely", "locality_available_id", "name", "time_type", "value_max", "value_min"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INVERSELY_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_MAX_FIELD_NUMBER: _ClassVar[int]
    VALUE_MIN_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    inversely: bool
    locality_available_id: str
    name: str
    time_type: TimeType
    value_max: str
    value_min: str
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

class DeliveryTimeCreateResponse(_message.Message):
    __slots__ = ["delivery_time", "response_standard"]
    DELIVERY_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_time: DeliveryTime
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_time: _Optional[_Union[DeliveryTime, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryTimeDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryTimeDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryTimeReadRequest(_message.Message):
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

class DeliveryTimeReadResponse(_message.Message):
    __slots__ = ["delivery_times", "meta_data", "response_standard"]
    DELIVERY_TIMES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_times: _containers.RepeatedCompositeFieldContainer[DeliveryTime]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_times: _Optional[_Iterable[_Union[DeliveryTime, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryTimeUpdateRequest(_message.Message):
    __slots__ = ["context", "delivery_time"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TIME_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_time: DeliveryTime
    def __init__(
        self,
        delivery_time: _Optional[_Union[DeliveryTime, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryTimeUpdateResponse(_message.Message):
    __slots__ = ["delivery_time", "response_standard"]
    DELIVERY_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_time: DeliveryTime
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_time: _Optional[_Union[DeliveryTime, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class TimeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
