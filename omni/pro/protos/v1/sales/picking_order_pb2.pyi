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

class PickingOrder(_message.Message):
    __slots__ = ["active", "id", "object_audit", "order_id", "picking_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PICKING_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    id: int
    object_audit: _base_pb2.ObjectAudit
    order_id: int
    picking_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        order_id: _Optional[int] = ...,
        picking_id: _Optional[int] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class PickingOrderCreateRequest(_message.Message):
    __slots__ = ["context", "order_id", "picking_id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PICKING_ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    order_id: int
    picking_id: int
    def __init__(
        self,
        order_id: _Optional[int] = ...,
        picking_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingOrderCreateResponse(_message.Message):
    __slots__ = ["picking_order", "response_standard"]
    PICKING_ORDER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    picking_order: PickingOrder
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        picking_order: _Optional[_Union[PickingOrder, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class PickingOrderDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class PickingOrderDeleteResponse(_message.Message):
    __slots__ = ["picking_order", "response_standard"]
    PICKING_ORDER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    picking_order: PickingOrder
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        picking_order: _Optional[_Union[PickingOrder, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class PickingOrderReadRequest(_message.Message):
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

class PickingOrderReadResponse(_message.Message):
    __slots__ = ["meta_data", "picking_orders", "response_standard"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PICKING_ORDERS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    picking_orders: _containers.RepeatedCompositeFieldContainer[PickingOrder]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        picking_orders: _Optional[_Iterable[_Union[PickingOrder, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class PickingOrderUpdateRequest(_message.Message):
    __slots__ = ["context", "picking_order"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PICKING_ORDER_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    picking_order: PickingOrder
    def __init__(
        self,
        picking_order: _Optional[_Union[PickingOrder, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingOrderUpdateResponse(_message.Message):
    __slots__ = ["picking_order", "response_standard"]
    PICKING_ORDER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    picking_order: PickingOrder
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        picking_order: _Optional[_Union[PickingOrder, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
