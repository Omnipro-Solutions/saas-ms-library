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
from omni.pro.protos.v1.stock import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Route(_message.Message):
    __slots__ = [
        "id",
        "name",
        "sequence",
        "product_categ_selectable",
        "product_selectable",
        "packing_selectable",
        "warehouse_selectable",
        "warehouse",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEG_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    PACKING_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    sequence: int
    product_categ_selectable: _wrappers_pb2.BoolValue
    product_selectable: _wrappers_pb2.BoolValue
    packing_selectable: _wrappers_pb2.BoolValue
    warehouse_selectable: _wrappers_pb2.BoolValue
    warehouse: _warehouse_pb2.Warehouse
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        sequence: _Optional[int] = ...,
        product_categ_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        product_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        packing_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouse_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouse: _Optional[_Union[_warehouse_pb2.Warehouse, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class RouteCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "sequence",
        "product_categ_selectable",
        "product_selectable",
        "packing_selectable",
        "warehouse_selectable",
        "warehouse_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEG_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    PACKING_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    sequence: int
    product_categ_selectable: _wrappers_pb2.BoolValue
    product_selectable: _wrappers_pb2.BoolValue
    packing_selectable: _wrappers_pb2.BoolValue
    warehouse_selectable: _wrappers_pb2.BoolValue
    warehouse_id: int
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        sequence: _Optional[int] = ...,
        product_categ_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        product_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        packing_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouse_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouse_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RouteCreateResponse(_message.Message):
    __slots__ = ["response_standard", "route"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    route: Route
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        route: _Optional[_Union[Route, _Mapping]] = ...,
    ) -> None: ...

class RouteReadRequest(_message.Message):
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

class RouteReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "routes"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    routes: _containers.RepeatedCompositeFieldContainer[Route]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        routes: _Optional[_Iterable[_Union[Route, _Mapping]]] = ...,
    ) -> None: ...

class RouteUpdateRequest(_message.Message):
    __slots__ = ["route", "context"]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    route: Route
    context: _base_pb2.Context
    def __init__(
        self,
        route: _Optional[_Union[Route, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RouteUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "route"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    route: Route
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        route: _Optional[_Union[Route, _Mapping]] = ...,
    ) -> None: ...

class RouteDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class RouteDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
