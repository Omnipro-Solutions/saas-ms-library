from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.stock import location_pb2 as _location_pb2
from omni.pro.protos.v1.stock import picking_pb2 as _picking_pb2
from omni.pro.protos.v1.stock import product_pb2 as _product_pb2
from omni.pro.protos.v1.stock import stock_move_pb2 as _stock_move_pb2
from omni.pro.protos.v1.stock import uom_pb2 as _uom_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StockMoveLine(_message.Message):
    __slots__ = [
        "id",
        "stock_move",
        "picking",
        "state",
        "reference",
        "date",
        "origin",
        "product",
        "location",
        "location_dest",
        "qty_done",
        "product_uom_qty",
        "product_uom",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_FIELD_NUMBER: _ClassVar[int]
    PICKING_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DEST_FIELD_NUMBER: _ClassVar[int]
    QTY_DONE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_QTY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    stock_move: _stock_move_pb2.StockMove
    picking: _picking_pb2.Picking
    state: str
    reference: str
    date: _timestamp_pb2.Timestamp
    origin: str
    product: _product_pb2.Product
    location: _location_pb2.Location
    location_dest: _location_pb2.Location
    qty_done: float
    product_uom_qty: float
    product_uom: _uom_pb2.Uom
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        stock_move: _Optional[_Union[_stock_move_pb2.StockMove, _Mapping]] = ...,
        picking: _Optional[_Union[_picking_pb2.Picking, _Mapping]] = ...,
        state: _Optional[str] = ...,
        reference: _Optional[str] = ...,
        date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        origin: _Optional[str] = ...,
        product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...,
        location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        location_dest: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        qty_done: _Optional[float] = ...,
        product_uom_qty: _Optional[float] = ...,
        product_uom: _Optional[_Union[_uom_pb2.Uom, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class StockMoveLineCreateRequest(_message.Message):
    __slots__ = [
        "stock_move_id",
        "picking_id",
        "state",
        "reference",
        "date",
        "origin",
        "product_id",
        "location_id",
        "location_dest_id",
        "qty_done",
        "product_uom_qty",
        "product_uom_id",
        "context",
    ]
    STOCK_MOVE_ID_FIELD_NUMBER: _ClassVar[int]
    PICKING_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DEST_ID_FIELD_NUMBER: _ClassVar[int]
    QTY_DONE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_QTY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    stock_move_id: int
    picking_id: int
    state: str
    reference: str
    date: _timestamp_pb2.Timestamp
    origin: str
    product_id: str
    location_id: int
    location_dest_id: int
    qty_done: float
    product_uom_qty: float
    product_uom_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        stock_move_id: _Optional[int] = ...,
        picking_id: _Optional[int] = ...,
        state: _Optional[str] = ...,
        reference: _Optional[str] = ...,
        date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        origin: _Optional[str] = ...,
        product_id: _Optional[str] = ...,
        location_id: _Optional[int] = ...,
        location_dest_id: _Optional[int] = ...,
        qty_done: _Optional[float] = ...,
        product_uom_qty: _Optional[float] = ...,
        product_uom_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class StockMoveLineCreateResponse(_message.Message):
    __slots__ = ["response_standard", "stock_move_line"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_LINE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    stock_move_line: StockMoveLine
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        stock_move_line: _Optional[_Union[StockMoveLine, _Mapping]] = ...,
    ) -> None: ...

class StockMoveLineReadRequest(_message.Message):
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

class StockMoveLineReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "stock_move_lines"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_LINES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    stock_move_lines: _containers.RepeatedCompositeFieldContainer[StockMoveLine]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        stock_move_lines: _Optional[_Iterable[_Union[StockMoveLine, _Mapping]]] = ...,
    ) -> None: ...

class StockMoveLineUpdateRequest(_message.Message):
    __slots__ = ["stock_move_line", "context"]
    STOCK_MOVE_LINE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    stock_move_line: StockMoveLine
    context: _base_pb2.Context
    def __init__(
        self,
        stock_move_line: _Optional[_Union[StockMoveLine, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class StockMoveLineUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "stock_move_line"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_LINE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    stock_move_line: StockMoveLine
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        stock_move_line: _Optional[_Union[StockMoveLine, _Mapping]] = ...,
    ) -> None: ...

class StockMoveLineDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class StockMoveLineDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class MoveLineAddQtyRequest(_message.Message):
    __slots__ = ["id", "quantity", "payload", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    quantity: int
    payload: _struct_pb2.Struct
    context: _base_pb2.Context
    def __init__(
        self,
        id: _Optional[int] = ...,
        quantity: _Optional[int] = ...,
        payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class MoveLineAddQtyResponse(_message.Message):
    __slots__ = ["response_standard", "data"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    data: _struct_pb2.Struct
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
    ) -> None: ...
