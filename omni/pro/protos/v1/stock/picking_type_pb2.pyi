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
from omni.pro.protos.v1.stock import location_pb2 as _location_pb2
from omni.pro.protos.v1.stock import sequence_pb2 as _sequence_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class PickingType(_message.Message):
    __slots__ = [
        "id",
        "name",
        "sequence_code",
        "warehouse",
        "code",
        "return_picking_type",
        "show_operations",
        "show_reserved",
        "default_location_src",
        "default_location_dest",
        "sequence",
        "barcode",
        "reservation_method",
        "type_code",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_CODE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    RETURN_PICKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOW_RESERVED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_SRC_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_DEST_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    BARCODE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    TYPE_CODE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    sequence_code: str
    warehouse: _base_pb2.ObjectResponse
    code: str
    return_picking_type: _base_pb2.ObjectResponse
    show_operations: _wrappers_pb2.BoolValue
    show_reserved: _wrappers_pb2.BoolValue
    default_location_src: _location_pb2.Location
    default_location_dest: _location_pb2.Location
    sequence: _sequence_pb2.Sequence
    barcode: str
    reservation_method: str
    type_code: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        sequence_code: _Optional[str] = ...,
        warehouse: _Optional[_Union[_base_pb2.ObjectResponse, _Mapping]] = ...,
        code: _Optional[str] = ...,
        return_picking_type: _Optional[_Union[_base_pb2.ObjectResponse, _Mapping]] = ...,
        show_operations: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        show_reserved: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        default_location_src: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        default_location_dest: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        sequence: _Optional[_Union[_sequence_pb2.Sequence, _Mapping]] = ...,
        barcode: _Optional[str] = ...,
        reservation_method: _Optional[str] = ...,
        type_code: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class PickingTypeCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "sequence_code",
        "warehouse_id",
        "code",
        "return_picking_type_id",
        "show_operations",
        "show_reserved",
        "default_location_src_id",
        "default_location_dest_id",
        "barcode",
        "reservation_method",
        "type_code",
        "sequence_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_CODE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    RETURN_PICKING_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SHOW_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOW_RESERVED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_SRC_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_DEST_ID_FIELD_NUMBER: _ClassVar[int]
    BARCODE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    TYPE_CODE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    sequence_code: str
    warehouse_id: int
    code: str
    return_picking_type_id: int
    show_operations: _wrappers_pb2.BoolValue
    show_reserved: _wrappers_pb2.BoolValue
    default_location_src_id: int
    default_location_dest_id: int
    barcode: str
    reservation_method: str
    type_code: str
    sequence_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        sequence_code: _Optional[str] = ...,
        warehouse_id: _Optional[int] = ...,
        code: _Optional[str] = ...,
        return_picking_type_id: _Optional[int] = ...,
        show_operations: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        show_reserved: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        default_location_src_id: _Optional[int] = ...,
        default_location_dest_id: _Optional[int] = ...,
        barcode: _Optional[str] = ...,
        reservation_method: _Optional[str] = ...,
        type_code: _Optional[str] = ...,
        sequence_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingTypeCreateResponse(_message.Message):
    __slots__ = ["response_standard", "picking_type"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    picking_type: PickingType
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        picking_type: _Optional[_Union[PickingType, _Mapping]] = ...,
    ) -> None: ...

class PickingTypeReadRequest(_message.Message):
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

class PickingTypeReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "picking_types"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    picking_types: _containers.RepeatedCompositeFieldContainer[PickingType]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        picking_types: _Optional[_Iterable[_Union[PickingType, _Mapping]]] = ...,
    ) -> None: ...

class PickingTypeUpdateRequest(_message.Message):
    __slots__ = ["picking_type", "context"]
    PICKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    picking_type: PickingType
    context: _base_pb2.Context
    def __init__(
        self,
        picking_type: _Optional[_Union[PickingType, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingTypeUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "picking_type"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    picking_type: PickingType
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        picking_type: _Optional[_Union[PickingType, _Mapping]] = ...,
    ) -> None: ...

class PickingTypeDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class PickingTypeDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
