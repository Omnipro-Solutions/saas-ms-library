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

DESCRIPTOR: _descriptor.FileDescriptor

class StockMove(_message.Message):
    __slots__ = [
        "active",
        "description_picking",
        "id",
        "object_audit",
        "picking_id",
        "product_id",
        "product_uom_id",
        "product_uom_qty",
        "quantity_done",
        "state",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_PICKING_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PICKING_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_QTY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_DONE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    description_picking: str
    id: int
    object_audit: _base_pb2.ObjectAudit
    picking_id: int
    product_id: int
    product_uom_id: int
    product_uom_qty: float
    quantity_done: float
    state: str
    def __init__(
        self,
        id: _Optional[int] = ...,
        picking_id: _Optional[int] = ...,
        state: _Optional[str] = ...,
        product_id: _Optional[int] = ...,
        product_uom_qty: _Optional[float] = ...,
        quantity_done: _Optional[float] = ...,
        product_uom_id: _Optional[int] = ...,
        description_picking: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class StockMoveCreateRequest(_message.Message):
    __slots__ = [
        "context",
        "description_picking",
        "picking_id",
        "product_id",
        "product_uom_id",
        "product_uom_qty",
        "quantity_done",
        "state",
    ]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_PICKING_FIELD_NUMBER: _ClassVar[int]
    PICKING_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_QTY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_DONE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    description_picking: str
    picking_id: int
    product_id: int
    product_uom_id: int
    product_uom_qty: float
    quantity_done: float
    state: str
    def __init__(
        self,
        picking_id: _Optional[int] = ...,
        state: _Optional[str] = ...,
        product_id: _Optional[int] = ...,
        product_uom_qty: _Optional[float] = ...,
        quantity_done: _Optional[float] = ...,
        product_uom_id: _Optional[int] = ...,
        description_picking: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class StockMoveCreateResponse(_message.Message):
    __slots__ = ["response_standard", "stock_move"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    stock_move: StockMove
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        stock_move: _Optional[_Union[StockMove, _Mapping]] = ...,
    ) -> None: ...

class StockMoveDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class StockMoveDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class StockMoveReadRequest(_message.Message):
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

class StockMoveReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "stock_moves"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVES_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    stock_moves: _containers.RepeatedCompositeFieldContainer[StockMove]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        stock_moves: _Optional[_Iterable[_Union[StockMove, _Mapping]]] = ...,
    ) -> None: ...

class StockMoveUpdateRequest(_message.Message):
    __slots__ = ["context", "stock_move"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    stock_move: StockMove
    def __init__(
        self,
        stock_move: _Optional[_Union[StockMove, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class StockMoveUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "stock_move"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    stock_move: StockMove
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        stock_move: _Optional[_Union[StockMove, _Mapping]] = ...,
    ) -> None: ...
