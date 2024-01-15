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

DESCRIPTOR: _descriptor.FileDescriptor

class PickingPicker(_message.Message):
    __slots__ = [
        "id",
        "warehouse",
        "picking_type",
        "draft",
        "waiting",
        "confirmed",
        "assigned",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    WAITING_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    warehouse: _struct_pb2.Struct
    picking_type: _struct_pb2.Struct
    draft: int
    waiting: int
    confirmed: int
    assigned: int
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        warehouse: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        picking_type: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        draft: _Optional[int] = ...,
        waiting: _Optional[int] = ...,
        confirmed: _Optional[int] = ...,
        assigned: _Optional[int] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class PickingPickerReadRequest(_message.Message):
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

class PickingPickerReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "picking_pickers"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PICKING_PICKERS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    picking_pickers: _containers.RepeatedCompositeFieldContainer[PickingPicker]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        picking_pickers: _Optional[_Iterable[_Union[PickingPicker, _Mapping]]] = ...,
    ) -> None: ...
