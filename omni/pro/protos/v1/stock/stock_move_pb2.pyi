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
from omni.pro.protos.v1.stock import picking_pb2 as _picking_pb2
from omni.pro.protos.v1.stock import product_pb2 as _product_pb2
from omni.pro.protos.v1.stock import uom_pb2 as _uom_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StockMove(_message.Message):
    __slots__ = [
        "id",
        "picking",
        "state",
        "product",
        "quantity_done",
        "product_uom",
        "description_picking",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    PICKING_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_DONE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_PICKING_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    picking: _picking_pb2.Picking
    state: str
    product: _product_pb2.Product
    quantity_done: float
    product_uom: _uom_pb2.Uom
    description_picking: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        picking: _Optional[_Union[_picking_pb2.Picking, _Mapping]] = ...,
        state: _Optional[str] = ...,
        product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...,
        quantity_done: _Optional[float] = ...,
        product_uom: _Optional[_Union[_uom_pb2.Uom, _Mapping]] = ...,
        description_picking: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class StockMoveCreateRequest(_message.Message):
    __slots__ = [
        "picking_id",
        "state",
        "product_id",
        "quantity_done",
        "product_uom_id",
        "description_picking",
        "context",
    ]
    PICKING_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_DONE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_PICKING_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    picking_id: int
    state: str
    product_id: str
    quantity_done: float
    product_uom_id: str
    description_picking: str
    context: _base_pb2.Context
    def __init__(
        self,
        picking_id: _Optional[int] = ...,
        state: _Optional[str] = ...,
        product_id: _Optional[str] = ...,
        quantity_done: _Optional[float] = ...,
        product_uom_id: _Optional[str] = ...,
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

class StockMoveReadRequest(_message.Message):
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

class StockMoveReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "stock_moves"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    stock_moves: _containers.RepeatedCompositeFieldContainer[StockMove]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        stock_moves: _Optional[_Iterable[_Union[StockMove, _Mapping]]] = ...,
    ) -> None: ...

class StockMoveUpdateRequest(_message.Message):
    __slots__ = ["stock_move", "context"]
    STOCK_MOVE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    stock_move: StockMove
    context: _base_pb2.Context
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

class StockMoveDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class StockMoveDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
