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
from omni.pro.protos.v1.stock import country_pb2 as _country_pb2
from omni.pro.protos.v1.stock import location_pb2 as _location_pb2
from omni.pro.protos.v1.stock import picking_type_pb2 as _picking_type_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Warehouse(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "country_id",
        "territory_matrix_value",
        "address",
        "complement",
        "active",
        "delivery_steps",
        "receptions_steps",
        "view_location_id",
        "lot_stock_id",
        "wh_input_stock_loc_id",
        "wh_qc_stock_loc_id",
        "wh_pack_stock_loc_id",
        "wh_output_stock_loc_id",
        "in_type_id",
        "int_type_id",
        "pick_type_id",
        "pack_type_id",
        "out_type_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_VALUE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_STEPS_FIELD_NUMBER: _ClassVar[int]
    RECEPTIONS_STEPS_FIELD_NUMBER: _ClassVar[int]
    VIEW_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOT_STOCK_ID_FIELD_NUMBER: _ClassVar[int]
    WH_INPUT_STOCK_LOC_ID_FIELD_NUMBER: _ClassVar[int]
    WH_QC_STOCK_LOC_ID_FIELD_NUMBER: _ClassVar[int]
    WH_PACK_STOCK_LOC_ID_FIELD_NUMBER: _ClassVar[int]
    WH_OUTPUT_STOCK_LOC_ID_FIELD_NUMBER: _ClassVar[int]
    IN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    INT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    PICK_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    PACK_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    OUT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    code: str
    country_id: _country_pb2.Country
    territory_matrix_value: _struct_pb2.Struct
    address: str
    complement: str
    active: _wrappers_pb2.BoolValue
    delivery_steps: str
    receptions_steps: str
    view_location_id: _location_pb2.Location
    lot_stock_id: _location_pb2.Location
    wh_input_stock_loc_id: _location_pb2.Location
    wh_qc_stock_loc_id: _location_pb2.Location
    wh_pack_stock_loc_id: _location_pb2.Location
    wh_output_stock_loc_id: _location_pb2.Location
    in_type_id: _picking_type_pb2.PickingType
    int_type_id: _picking_type_pb2.PickingType
    pick_type_id: _picking_type_pb2.PickingType
    pack_type_id: _picking_type_pb2.PickingType
    out_type_id: _picking_type_pb2.PickingType
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        country_id: _Optional[_Union[_country_pb2.Country, _Mapping]] = ...,
        territory_matrix_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        address: _Optional[str] = ...,
        complement: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        delivery_steps: _Optional[str] = ...,
        receptions_steps: _Optional[str] = ...,
        view_location_id: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        lot_stock_id: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        wh_input_stock_loc_id: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        wh_qc_stock_loc_id: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        wh_pack_stock_loc_id: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        wh_output_stock_loc_id: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        in_type_id: _Optional[_Union[_picking_type_pb2.PickingType, _Mapping]] = ...,
        int_type_id: _Optional[_Union[_picking_type_pb2.PickingType, _Mapping]] = ...,
        pick_type_id: _Optional[_Union[_picking_type_pb2.PickingType, _Mapping]] = ...,
        pack_type_id: _Optional[_Union[_picking_type_pb2.PickingType, _Mapping]] = ...,
        out_type_id: _Optional[_Union[_picking_type_pb2.PickingType, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class WarehouseCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "country_id",
        "territory_matrix_value",
        "address",
        "complement",
        "delivery_steps",
        "receptions_steps",
        "view_location_id",
        "lot_stock_id",
        "wh_input_stock_loc_id",
        "wh_qc_stock_loc_id",
        "wh_pack_stock_loc_id",
        "wh_output_stock_loc_id",
        "in_type_id",
        "int_type_id",
        "pick_type_id",
        "pack_type_id",
        "out_type_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_VALUE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_STEPS_FIELD_NUMBER: _ClassVar[int]
    RECEPTIONS_STEPS_FIELD_NUMBER: _ClassVar[int]
    VIEW_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOT_STOCK_ID_FIELD_NUMBER: _ClassVar[int]
    WH_INPUT_STOCK_LOC_ID_FIELD_NUMBER: _ClassVar[int]
    WH_QC_STOCK_LOC_ID_FIELD_NUMBER: _ClassVar[int]
    WH_PACK_STOCK_LOC_ID_FIELD_NUMBER: _ClassVar[int]
    WH_OUTPUT_STOCK_LOC_ID_FIELD_NUMBER: _ClassVar[int]
    IN_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    INT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    PICK_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    PACK_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    OUT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    country_id: int
    territory_matrix_value: _struct_pb2.Struct
    address: str
    complement: str
    delivery_steps: str
    receptions_steps: str
    view_location_id: int
    lot_stock_id: int
    wh_input_stock_loc_id: int
    wh_qc_stock_loc_id: int
    wh_pack_stock_loc_id: int
    wh_output_stock_loc_id: int
    in_type_id: int
    int_type_id: int
    pick_type_id: int
    pack_type_id: int
    out_type_id: int
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        country_id: _Optional[int] = ...,
        territory_matrix_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        address: _Optional[str] = ...,
        complement: _Optional[str] = ...,
        delivery_steps: _Optional[str] = ...,
        receptions_steps: _Optional[str] = ...,
        view_location_id: _Optional[int] = ...,
        lot_stock_id: _Optional[int] = ...,
        wh_input_stock_loc_id: _Optional[int] = ...,
        wh_qc_stock_loc_id: _Optional[int] = ...,
        wh_pack_stock_loc_id: _Optional[int] = ...,
        wh_output_stock_loc_id: _Optional[int] = ...,
        in_type_id: _Optional[int] = ...,
        int_type_id: _Optional[int] = ...,
        pick_type_id: _Optional[int] = ...,
        pack_type_id: _Optional[int] = ...,
        out_type_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class WarehouseCreateResponse(_message.Message):
    __slots__ = ["response_standard", "warehouse"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    warehouse: Warehouse
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        warehouse: _Optional[_Union[Warehouse, _Mapping]] = ...,
    ) -> None: ...

class WarehouseReadRequest(_message.Message):
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

class WarehouseReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "warehouses"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    warehouses: _containers.RepeatedCompositeFieldContainer[Warehouse]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        warehouses: _Optional[_Iterable[_Union[Warehouse, _Mapping]]] = ...,
    ) -> None: ...

class WarehouseUpdateRequest(_message.Message):
    __slots__ = ["warehouse", "context"]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    warehouse: Warehouse
    context: _base_pb2.Context
    def __init__(
        self,
        warehouse: _Optional[_Union[Warehouse, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class WarehouseUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "warehouse"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    warehouse: Warehouse
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        warehouse: _Optional[_Union[Warehouse, _Mapping]] = ...,
    ) -> None: ...

class WarehouseDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class WarehouseDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
