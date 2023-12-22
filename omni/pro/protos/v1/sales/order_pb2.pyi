from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.sales import address_pb2 as _address_pb2
from omni.pro.protos.v1.sales import delivery_method_pb2 as _delivery_method_pb2
from omni.pro.protos.v1.sales import picking_pb2 as _picking_pb2
from omni.pro.protos.v1.sales import sale_pb2 as _sale_pb2
from omni.pro.protos.v1.sales import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = [
        "id",
        "name",
        "sale",
        "ship_address",
        "delivery_method",
        "tax_total",
        "discount_total",
        "subtotal",
        "total",
        "active",
        "external_id",
        "warehouse",
        "cid",
        "pickings",
        "object_audit",
        "order_lines",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SALE_FIELD_NUMBER: _ClassVar[int]
    SHIP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    TAX_TOTAL_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    PICKINGS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_LINES_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    sale: _sale_pb2.Sale
    ship_address: _address_pb2.Address
    delivery_method: _delivery_method_pb2.DeliveryMethod
    tax_total: float
    discount_total: float
    subtotal: float
    total: float
    active: _wrappers_pb2.BoolValue
    external_id: str
    warehouse: _warehouse_pb2.Warehouse
    cid: str
    pickings: _containers.RepeatedCompositeFieldContainer[_picking_pb2.Picking]
    object_audit: _base_pb2.ObjectAudit
    order_lines: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        sale: _Optional[_Union[_sale_pb2.Sale, _Mapping]] = ...,
        ship_address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ...,
        delivery_method: _Optional[_Union[_delivery_method_pb2.DeliveryMethod, _Mapping]] = ...,
        tax_total: _Optional[float] = ...,
        discount_total: _Optional[float] = ...,
        subtotal: _Optional[float] = ...,
        total: _Optional[float] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        warehouse: _Optional[_Union[_warehouse_pb2.Warehouse, _Mapping]] = ...,
        cid: _Optional[str] = ...,
        pickings: _Optional[_Iterable[_Union[_picking_pb2.Picking, _Mapping]]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
        order_lines: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
    ) -> None: ...

class OrderCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "sale_id",
        "ship_address_code",
        "delivery_method_id",
        "tax_total",
        "discount_total",
        "subtotal",
        "total",
        "external_id",
        "warehouse_id",
        "cid",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SALE_ID_FIELD_NUMBER: _ClassVar[int]
    SHIP_ADDRESS_CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    TAX_TOTAL_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    sale_id: int
    ship_address_code: str
    delivery_method_id: int
    tax_total: float
    discount_total: float
    subtotal: float
    total: float
    external_id: str
    warehouse_id: int
    cid: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        sale_id: _Optional[int] = ...,
        ship_address_code: _Optional[str] = ...,
        delivery_method_id: _Optional[int] = ...,
        tax_total: _Optional[float] = ...,
        discount_total: _Optional[float] = ...,
        subtotal: _Optional[float] = ...,
        total: _Optional[float] = ...,
        external_id: _Optional[str] = ...,
        warehouse_id: _Optional[int] = ...,
        cid: _Optional[str] = ...,
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

class OrderReadRequest(_message.Message):
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

class OrderReadResponse(_message.Message):
    __slots__ = ["orders", "response_standard", "meta_data"]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[Order]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    def __init__(
        self,
        orders: _Optional[_Iterable[_Union[Order, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class OrderUpdateRequest(_message.Message):
    __slots__ = ["order", "context"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    order: Order
    context: _base_pb2.Context
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

class OrderDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class OrderDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class OrderConfirmRequest(_message.Message):
    __slots__ = ["payload", "context"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    payload: _struct_pb2.Struct
    context: _base_pb2.Context
    def __init__(
        self,
        payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class OrderConfirmResponse(_message.Message):
    __slots__ = ["confirm", "response_standard"]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    confirm: _struct_pb2.Struct
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        confirm: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
