from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StockMoveLine(_message.Message):
    __slots__ = [
        "active",
        "date",
        "id",
        "location_dest_id",
        "location_id",
        "object_audit",
        "origin",
        "picking_id",
        "product_id",
        "product_uom_id",
        "qty_done",
        "reference",
        "status",
        "stock_move_id",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DEST_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PICKING_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_ID_FIELD_NUMBER: _ClassVar[int]
    QTY_DONE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    date: _timestamp_pb2.Timestamp
    id: int
    location_dest_id: int
    location_id: int
    object_audit: _base_pb2.ObjectAudit
    origin: str
    picking_id: int
    product_id: int
    product_uom_id: int
    qty_done: int
    reference: str
    status: str
    stock_move_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        stock_move_id: _Optional[int] = ...,
        picking_id: _Optional[int] = ...,
        status: _Optional[str] = ...,
        reference: _Optional[str] = ...,
        date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        origin: _Optional[str] = ...,
        product_id: _Optional[int] = ...,
        location_id: _Optional[int] = ...,
        location_dest_id: _Optional[int] = ...,
        qty_done: _Optional[int] = ...,
        product_uom_id: _Optional[int] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class StockMoveLineCreateRequest(_message.Message):
    __slots__ = [
        "context",
        "date",
        "location_dest_id",
        "location_id",
        "origin",
        "picking_id",
        "product_id",
        "product_uom_id",
        "qty_done",
        "reference",
        "status",
        "stock_move_id",
    ]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DEST_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PICKING_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_UOM_ID_FIELD_NUMBER: _ClassVar[int]
    QTY_DONE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    date: _timestamp_pb2.Timestamp
    location_dest_id: int
    location_id: int
    origin: str
    picking_id: int
    product_id: int
    product_uom_id: int
    qty_done: int
    reference: str
    status: str
    stock_move_id: int
    def __init__(
        self,
        stock_move_id: _Optional[int] = ...,
        picking_id: _Optional[int] = ...,
        status: _Optional[str] = ...,
        reference: _Optional[str] = ...,
        date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        origin: _Optional[str] = ...,
        product_id: _Optional[int] = ...,
        location_id: _Optional[int] = ...,
        location_dest_id: _Optional[int] = ...,
        qty_done: _Optional[int] = ...,
        product_uom_id: _Optional[int] = ...,
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

class StockMoveLineDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class StockMoveLineDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class StockMoveLineReadRequest(_message.Message):
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

class StockMoveLineReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "stock_move_lines"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_LINES_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    stock_move_lines: _containers.RepeatedCompositeFieldContainer[StockMoveLine]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        stock_move_lines: _Optional[_Iterable[_Union[StockMoveLine, _Mapping]]] = ...,
    ) -> None: ...

class StockMoveLineUpdateRequest(_message.Message):
    __slots__ = ["context", "stock_move_line"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVE_LINE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    stock_move_line: StockMoveLine
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
