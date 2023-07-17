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

class OrderLine(_message.Message):
    __slots__ = [
        "active",
        "discount",
        "id",
        "object_audit",
        "order_id",
        "price_subtotal",
        "price_total",
        "price_unit",
        "product_id",
        "quantity",
        "tax_id",
        "uom_id",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    PRICE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    PRICE_UNIT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_FIELD_NUMBER: _ClassVar[int]
    UOM_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    discount: float
    id: int
    object_audit: _base_pb2.ObjectAudit
    order_id: int
    price_subtotal: float
    price_total: float
    price_unit: float
    product_id: int
    quantity: float
    tax_id: int
    uom_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        order_id: _Optional[int] = ...,
        product_id: _Optional[int] = ...,
        quantity: _Optional[float] = ...,
        uom_id: _Optional[int] = ...,
        price_unit: _Optional[float] = ...,
        tax_id: _Optional[int] = ...,
        discount: _Optional[float] = ...,
        price_subtotal: _Optional[float] = ...,
        price_total: _Optional[float] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class OrderLineCreateRequest(_message.Message):
    __slots__ = [
        "context",
        "discount",
        "order_id",
        "price_subtotal",
        "price_total",
        "price_unit",
        "product_id",
        "quantity",
        "tax_id",
        "uom_id",
    ]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    PRICE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    PRICE_UNIT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_FIELD_NUMBER: _ClassVar[int]
    UOM_ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    discount: float
    order_id: int
    price_subtotal: float
    price_total: float
    price_unit: float
    product_id: int
    quantity: float
    tax_id: int
    uom_id: int
    def __init__(
        self,
        order_id: _Optional[int] = ...,
        product_id: _Optional[int] = ...,
        quantity: _Optional[float] = ...,
        uom_id: _Optional[int] = ...,
        price_unit: _Optional[float] = ...,
        tax_id: _Optional[int] = ...,
        discount: _Optional[float] = ...,
        price_subtotal: _Optional[float] = ...,
        price_total: _Optional[float] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class OrderLineCreateResponse(_message.Message):
    __slots__ = ["order_line", "response_standard"]
    ORDER_LINE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    order_line: OrderLine
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        order_line: _Optional[_Union[OrderLine, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class OrderLineDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class OrderLineDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class OrderLineReadRequest(_message.Message):
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

class OrderLineReadResponse(_message.Message):
    __slots__ = ["meta_data", "order_lines", "response_standard"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ORDER_LINES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    order_lines: _containers.RepeatedCompositeFieldContainer[OrderLine]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        order_lines: _Optional[_Iterable[_Union[OrderLine, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class OrderLineUpdateRequest(_message.Message):
    __slots__ = ["context", "order_line"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORDER_LINE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    order_line: OrderLine
    def __init__(
        self,
        order_line: _Optional[_Union[OrderLine, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class OrderLineUpdateResponse(_message.Message):
    __slots__ = ["order_line", "response_standard"]
    ORDER_LINE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    order_line: OrderLine
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        order_line: _Optional[_Union[OrderLine, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
