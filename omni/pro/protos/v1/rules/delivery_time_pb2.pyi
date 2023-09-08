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
from omni.pro.protos.v1.rules import delivery_locality_pb2 as _delivery_locality_pb2
from omni.pro.protos.v1.rules import delivery_method_pb2 as _delivery_method_pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryTime(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "delivery_methods",
        "warehouses_to",
        "warehouses_from",
        "locality_available",
        "time_type",
        "value_min",
        "value_max",
        "inversely",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHODS_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSES_TO_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSES_FROM_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_MIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_MAX_FIELD_NUMBER: _ClassVar[int]
    INVERSELY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    delivery_methods: _containers.RepeatedCompositeFieldContainer[_delivery_method_pb2.DeliveryMethod]
    warehouses_to: _containers.RepeatedCompositeFieldContainer[_warehouse_pb2.Warehouse]
    warehouses_from: _containers.RepeatedCompositeFieldContainer[_warehouse_pb2.Warehouse]
    locality_available: _delivery_locality_pb2.DeliveryLocality
    time_type: str
    value_min: int
    value_max: int
    inversely: _wrappers_pb2.BoolValue
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        delivery_methods: _Optional[_Iterable[_Union[_delivery_method_pb2.DeliveryMethod, _Mapping]]] = ...,
        warehouses_to: _Optional[_Iterable[_Union[_warehouse_pb2.Warehouse, _Mapping]]] = ...,
        warehouses_from: _Optional[_Iterable[_Union[_warehouse_pb2.Warehouse, _Mapping]]] = ...,
        locality_available: _Optional[_Union[_delivery_locality_pb2.DeliveryLocality, _Mapping]] = ...,
        time_type: _Optional[str] = ...,
        value_min: _Optional[int] = ...,
        value_max: _Optional[int] = ...,
        inversely: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryTimeCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "locality_available_id",
        "time_type",
        "value_min",
        "value_max",
        "warehouse_to_ids",
        "warehouse_from_ids",
        "delivery_method_ids",
        "inversely",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_MIN_FIELD_NUMBER: _ClassVar[int]
    VALUE_MAX_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_TO_IDS_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FROM_IDS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_IDS_FIELD_NUMBER: _ClassVar[int]
    INVERSELY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    locality_available_id: str
    time_type: str
    value_min: int
    value_max: int
    warehouse_to_ids: _containers.RepeatedScalarFieldContainer[int]
    warehouse_from_ids: _containers.RepeatedScalarFieldContainer[int]
    delivery_method_ids: _containers.RepeatedScalarFieldContainer[str]
    inversely: _wrappers_pb2.BoolValue
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        locality_available_id: _Optional[str] = ...,
        time_type: _Optional[str] = ...,
        value_min: _Optional[int] = ...,
        value_max: _Optional[int] = ...,
        warehouse_to_ids: _Optional[_Iterable[int]] = ...,
        warehouse_from_ids: _Optional[_Iterable[int]] = ...,
        delivery_method_ids: _Optional[_Iterable[str]] = ...,
        inversely: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
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

class DeliveryTimeReadRequest(_message.Message):
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
    __slots__ = ["delivery_time", "context"]
    DELIVERY_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_time: DeliveryTime
    context: _base_pb2.Context
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

class DeliveryTimeDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryTimeDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class AddWarehousesToRequest(_message.Message):
    __slots__ = ["delivery_time_id", "warehouse_to_ids", "context"]
    DELIVERY_TIME_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_TO_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_time_id: str
    warehouse_to_ids: _containers.RepeatedScalarFieldContainer[int]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_time_id: _Optional[str] = ...,
        warehouse_to_ids: _Optional[_Iterable[int]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddWarehousesToResponse(_message.Message):
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

class RemoveWarehousesToRequest(_message.Message):
    __slots__ = ["delivery_time_id", "warehouse_to_ids", "context"]
    DELIVERY_TIME_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_TO_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_time_id: str
    warehouse_to_ids: _containers.RepeatedScalarFieldContainer[int]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_time_id: _Optional[str] = ...,
        warehouse_to_ids: _Optional[_Iterable[int]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RemoveWarehousesToResponse(_message.Message):
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

class AddWarehousesFromRequest(_message.Message):
    __slots__ = ["delivery_time_id", "warehouse_from_ids", "context"]
    DELIVERY_TIME_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FROM_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_time_id: str
    warehouse_from_ids: _containers.RepeatedScalarFieldContainer[int]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_time_id: _Optional[str] = ...,
        warehouse_from_ids: _Optional[_Iterable[int]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddWarehousesFromResponse(_message.Message):
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

class RemoveWarehousesFromRequest(_message.Message):
    __slots__ = ["delivery_time_id", "warehouse_from_ids", "context"]
    DELIVERY_TIME_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FROM_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_time_id: str
    warehouse_from_ids: _containers.RepeatedScalarFieldContainer[int]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_time_id: _Optional[str] = ...,
        warehouse_from_ids: _Optional[_Iterable[int]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RemoveWarehousesFromResponse(_message.Message):
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

class AddDeliveryMethodRequest(_message.Message):
    __slots__ = ["delivery_time_id", "delivery_method_ids", "context"]
    DELIVERY_TIME_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_time_id: str
    delivery_method_ids: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_time_id: _Optional[str] = ...,
        delivery_method_ids: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddDeliveryMethodResponse(_message.Message):
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

class RemoveDeliveryMethodRequest(_message.Message):
    __slots__ = ["delivery_time_id", "delivery_method_ids", "context"]
    DELIVERY_TIME_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_time_id: str
    delivery_method_ids: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_time_id: _Optional[str] = ...,
        delivery_method_ids: _Optional[_Iterable[str]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RemoveDeliveryMethodResponse(_message.Message):
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
