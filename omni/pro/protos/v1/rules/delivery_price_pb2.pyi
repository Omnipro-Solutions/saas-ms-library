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
from omni.pro.protos.v1.rules import currency_pb2 as _currency_pb2
from omni.pro.protos.v1.rules import delivery_locality_pb2 as _delivery_locality_pb2
from omni.pro.protos.v1.rules import delivery_method_pb2 as _delivery_method_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryPrice(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "delivery_method",
        "purchase_rank",
        "operator_price_rank",
        "price_rank",
        "currency",
        "fixed_price",
        "operator_price",
        "purchase_price",
        "variable_factor",
        "usage",
        "price_by_variable_factor",
        "locality_available",
        "python_code",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_RANK_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_PRICE_RANK_FIELD_NUMBER: _ClassVar[int]
    PRICE_RANK_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    FIXED_PRICE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_PRICE_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_PRICE_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    PRICE_BY_VARIABLE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PYTHON_CODE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    delivery_method: _delivery_method_pb2.DeliveryMethod
    purchase_rank: _wrappers_pb2.BoolValue
    operator_price_rank: str
    price_rank: float
    currency: str
    fixed_price: float
    operator_price: str
    purchase_price: float
    variable_factor: str
    usage: str
    price_by_variable_factor: float
    locality_available: _delivery_locality_pb2.DeliveryLocality
    python_code: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        delivery_method: _Optional[_Union[_delivery_method_pb2.DeliveryMethod, _Mapping]] = ...,
        purchase_rank: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        operator_price_rank: _Optional[str] = ...,
        price_rank: _Optional[float] = ...,
        currency: _Optional[str] = ...,
        fixed_price: _Optional[float] = ...,
        operator_price: _Optional[str] = ...,
        purchase_price: _Optional[float] = ...,
        variable_factor: _Optional[str] = ...,
        usage: _Optional[str] = ...,
        price_by_variable_factor: _Optional[float] = ...,
        locality_available: _Optional[_Union[_delivery_locality_pb2.DeliveryLocality, _Mapping]] = ...,
        python_code: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryPriceCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "delivery_method_id",
        "purchase_rank",
        "operator_price_rank",
        "price_rank",
        "currency_id",
        "fixed_price",
        "operator_price",
        "purchase_price",
        "variable_factor",
        "usage",
        "price_by_variable_factor",
        "locality_available_id",
        "python_code",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_RANK_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_PRICE_RANK_FIELD_NUMBER: _ClassVar[int]
    PRICE_RANK_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    FIXED_PRICE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_PRICE_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_PRICE_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    PRICE_BY_VARIABLE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    PYTHON_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    delivery_method_id: str
    purchase_rank: _wrappers_pb2.BoolValue
    operator_price_rank: str
    price_rank: float
    currency_id: str
    fixed_price: float
    operator_price: str
    purchase_price: float
    variable_factor: str
    usage: str
    price_by_variable_factor: float
    locality_available_id: str
    python_code: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        delivery_method_id: _Optional[str] = ...,
        purchase_rank: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        operator_price_rank: _Optional[str] = ...,
        price_rank: _Optional[float] = ...,
        currency_id: _Optional[str] = ...,
        fixed_price: _Optional[float] = ...,
        operator_price: _Optional[str] = ...,
        purchase_price: _Optional[float] = ...,
        variable_factor: _Optional[str] = ...,
        usage: _Optional[str] = ...,
        price_by_variable_factor: _Optional[float] = ...,
        locality_available_id: _Optional[str] = ...,
        python_code: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryPriceCreateResponse(_message.Message):
    __slots__ = ["delivery_price", "response_standard"]
    DELIVERY_PRICE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_price: DeliveryPrice
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_price: _Optional[_Union[DeliveryPrice, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryPriceReadRequest(_message.Message):
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

class DeliveryPriceReadResponse(_message.Message):
    __slots__ = ["delivery_prices", "meta_data", "response_standard"]
    DELIVERY_PRICES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_prices: _containers.RepeatedCompositeFieldContainer[DeliveryPrice]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_prices: _Optional[_Iterable[_Union[DeliveryPrice, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryPriceUpdateRequest(_message.Message):
    __slots__ = ["delivery_price", "context"]
    DELIVERY_PRICE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_price: DeliveryPrice
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_price: _Optional[_Union[DeliveryPrice, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryPriceUpdateResponse(_message.Message):
    __slots__ = ["delivery_price", "response_standard"]
    DELIVERY_PRICE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_price: DeliveryPrice
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_price: _Optional[_Union[DeliveryPrice, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryPriceDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryPriceDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
