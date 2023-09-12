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
from omni.pro.protos.v1.sales import order_pb2 as _order_pb2
from omni.pro.protos.v1.sales import product_pb2 as _product_pb2
from omni.pro.protos.v1.sales import tax_pb2 as _tax_pb2
from omni.pro.protos.v1.sales import uom_pb2 as _uom_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class OrderLine(_message.Message):
    __slots__ = [
        "id",
        "order",
        "product",
        "quantity",
        "uom",
        "price_unit",
        "tax",
        "discount",
        "price_total",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UOM_FIELD_NUMBER: _ClassVar[int]
    PRICE_UNIT_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    order: _order_pb2.Order
    product: _product_pb2.Product
    quantity: float
    uom: _uom_pb2.Uom
    price_unit: float
    tax: _tax_pb2.Tax
    discount: float
    price_total: float
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        order: _Optional[_Union[_order_pb2.Order, _Mapping]] = ...,
        product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...,
        quantity: _Optional[float] = ...,
        uom: _Optional[_Union[_uom_pb2.Uom, _Mapping]] = ...,
        price_unit: _Optional[float] = ...,
        tax: _Optional[_Union[_tax_pb2.Tax, _Mapping]] = ...,
        discount: _Optional[float] = ...,
        price_total: _Optional[float] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class OrderLineCreateRequest(_message.Message):
    __slots__ = [
        "order_id",
        "product_id",
        "quantity",
        "uom_id",
        "price_unit",
        "tax_id",
        "discount",
        "price_total",
        "context",
    ]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UOM_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_UNIT_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    order_id: int
    product_id: str
    quantity: float
    uom_id: str
    price_unit: float
    tax_id: int
    discount: float
    price_total: float
    context: _base_pb2.Context
    def __init__(
        self,
        order_id: _Optional[int] = ...,
        product_id: _Optional[str] = ...,
        quantity: _Optional[float] = ...,
        uom_id: _Optional[str] = ...,
        price_unit: _Optional[float] = ...,
        tax_id: _Optional[int] = ...,
        discount: _Optional[float] = ...,
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

class OrderLineReadRequest(_message.Message):
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

class OrderLineReadResponse(_message.Message):
    __slots__ = ["order_lines", "response_standard", "meta_data"]
    ORDER_LINES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    order_lines: _containers.RepeatedCompositeFieldContainer[OrderLine]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    def __init__(
        self,
        order_lines: _Optional[_Iterable[_Union[OrderLine, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class OrderLineUpdateRequest(_message.Message):
    __slots__ = ["order_line", "context"]
    ORDER_LINE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    order_line: OrderLine
    context: _base_pb2.Context
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

class OrderLineDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class OrderLineDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
