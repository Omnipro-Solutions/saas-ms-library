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

class Order(_message.Message):
    __slots__ = [
        "active",
        "carrier_id",
        "delivery_method_id",
        "id",
        "name",
        "object_audit",
        "payment_method_id",
        "sale_id",
        "ship_address_id",
        "subtotal",
        "tax_total",
        "total",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CARRIER_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ID_FIELD_NUMBER: _ClassVar[int]
    SHIP_ADDRESS_ID_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TAX_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    active: bool
    carrier_id: int
    delivery_method_id: int
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    payment_method_id: int
    sale_id: int
    ship_address_id: int
    subtotal: float
    tax_total: float
    total: float
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        sale_id: _Optional[int] = ...,
        ship_address_id: _Optional[int] = ...,
        delivery_method_id: _Optional[int] = ...,
        carrier_id: _Optional[int] = ...,
        payment_method_id: _Optional[int] = ...,
        tax_total: _Optional[float] = ...,
        subtotal: _Optional[float] = ...,
        total: _Optional[float] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class OrderCreateRequest(_message.Message):
    __slots__ = [
        "carrier_id",
        "context",
        "delivery_method_id",
        "name",
        "payment_method_id",
        "sale_id",
        "ship_address_id",
        "subtotal",
        "tax_total",
        "total",
    ]
    CARRIER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ID_FIELD_NUMBER: _ClassVar[int]
    SHIP_ADDRESS_ID_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TAX_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    carrier_id: int
    context: _base_pb2.Context
    delivery_method_id: int
    name: str
    payment_method_id: int
    sale_id: int
    ship_address_id: int
    subtotal: float
    tax_total: float
    total: float
    def __init__(
        self,
        name: _Optional[str] = ...,
        sale_id: _Optional[int] = ...,
        ship_address_id: _Optional[int] = ...,
        delivery_method_id: _Optional[int] = ...,
        carrier_id: _Optional[int] = ...,
        payment_method_id: _Optional[int] = ...,
        tax_total: _Optional[float] = ...,
        subtotal: _Optional[float] = ...,
        total: _Optional[float] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class OrderCreateResponse(_message.Message):
    __slots__ = ["order", "response_standard"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    order: Order
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        order: _Optional[_Union[Order, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class OrderDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class OrderDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class OrderReadRequest(_message.Message):
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

class OrderReadResponse(_message.Message):
    __slots__ = ["meta_data", "order", "response_standard"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    order: _containers.RepeatedCompositeFieldContainer[Order]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        order: _Optional[_Iterable[_Union[Order, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class OrderUpdateRequest(_message.Message):
    __slots__ = ["context", "order"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    order: Order
    def __init__(
        self,
        order: _Optional[_Union[Order, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class OrderUpdateResponse(_message.Message):
    __slots__ = ["order", "response_standard"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    order: Order
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        order: _Optional[_Union[Order, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...