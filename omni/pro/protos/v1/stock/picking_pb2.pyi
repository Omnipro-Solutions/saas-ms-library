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
from omni.pro.protos.v1.stock import attachment_pb2 as _attachment_pb2
from omni.pro.protos.v1.stock import carrier_pb2 as _carrier_pb2
from omni.pro.protos.v1.stock import location_pb2 as _location_pb2
from omni.pro.protos.v1.stock import picking_type_pb2 as _picking_type_pb2
from omni.pro.protos.v1.stock import procurement_group_pb2 as _procurement_group_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Picking(_message.Message):
    __slots__ = [
        "id",
        "name",
        "picking_type",
        "location",
        "location_dest",
        "attachment_guide",
        "attachment_invoice",
        "origin",
        "date_start_preparation",
        "date_done",
        "scheduled_date",
        "time_total_preparation",
        "time_assigned",
        "carrier",
        "date_delivery",
        "carrier_tracking_ref",
        "group",
        "weight",
        "shipping_weight",
        "state",
        "dependency",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DEST_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_GUIDE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_INVOICE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DATE_START_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    DATE_DONE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
    TIME_TOTAL_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    TIME_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    DATE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    CARRIER_TRACKING_REF_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    picking_type: _picking_type_pb2.PickingType
    location: _location_pb2.Location
    location_dest: _location_pb2.Location
    attachment_guide: _attachment_pb2.Attachment
    attachment_invoice: _attachment_pb2.Attachment
    origin: str
    date_start_preparation: _timestamp_pb2.Timestamp
    date_done: _timestamp_pb2.Timestamp
    scheduled_date: _timestamp_pb2.Timestamp
    time_total_preparation: float
    time_assigned: float
    carrier: _carrier_pb2.Carrier
    date_delivery: _timestamp_pb2.Timestamp
    carrier_tracking_ref: str
    group: _procurement_group_pb2.ProcurementGroup
    weight: float
    shipping_weight: float
    state: str
    dependency: _base_pb2.ObjectResponse
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        picking_type: _Optional[_Union[_picking_type_pb2.PickingType, _Mapping]] = ...,
        location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        location_dest: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        attachment_guide: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...,
        attachment_invoice: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...,
        origin: _Optional[str] = ...,
        date_start_preparation: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        date_done: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        scheduled_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        time_total_preparation: _Optional[float] = ...,
        time_assigned: _Optional[float] = ...,
        carrier: _Optional[_Union[_carrier_pb2.Carrier, _Mapping]] = ...,
        date_delivery: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        carrier_tracking_ref: _Optional[str] = ...,
        group: _Optional[_Union[_procurement_group_pb2.ProcurementGroup, _Mapping]] = ...,
        weight: _Optional[float] = ...,
        shipping_weight: _Optional[float] = ...,
        state: _Optional[str] = ...,
        dependency: _Optional[_Union[_base_pb2.ObjectResponse, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class PickingCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "picking_type_id",
        "location_id",
        "location_dest_id",
        "attachment_guide_id",
        "attachment_invoice_id",
        "origin",
        "date_start_preparation",
        "date_done",
        "scheduled_date",
        "time_total_preparation",
        "time_assigned",
        "carrier_id",
        "date_delivery",
        "carrier_tracking_ref",
        "group_id",
        "weight",
        "shipping_weight",
        "state",
        "dependency_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DEST_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_GUIDE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DATE_START_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    DATE_DONE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
    TIME_TOTAL_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    TIME_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    CARRIER_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    CARRIER_TRACKING_REF_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    picking_type_id: int
    location_id: int
    location_dest_id: int
    attachment_guide_id: int
    attachment_invoice_id: int
    origin: str
    date_start_preparation: _timestamp_pb2.Timestamp
    date_done: _timestamp_pb2.Timestamp
    scheduled_date: _timestamp_pb2.Timestamp
    time_total_preparation: float
    time_assigned: float
    carrier_id: int
    date_delivery: _timestamp_pb2.Timestamp
    carrier_tracking_ref: str
    group_id: int
    weight: float
    shipping_weight: float
    state: str
    dependency_id: int
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        picking_type_id: _Optional[int] = ...,
        location_id: _Optional[int] = ...,
        location_dest_id: _Optional[int] = ...,
        attachment_guide_id: _Optional[int] = ...,
        attachment_invoice_id: _Optional[int] = ...,
        origin: _Optional[str] = ...,
        date_start_preparation: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        date_done: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        scheduled_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        time_total_preparation: _Optional[float] = ...,
        time_assigned: _Optional[float] = ...,
        carrier_id: _Optional[int] = ...,
        date_delivery: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        carrier_tracking_ref: _Optional[str] = ...,
        group_id: _Optional[int] = ...,
        weight: _Optional[float] = ...,
        shipping_weight: _Optional[float] = ...,
        state: _Optional[str] = ...,
        dependency_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingCreateResponse(_message.Message):
    __slots__ = ["response_standard", "picking"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    PICKING_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    picking: Picking
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        picking: _Optional[_Union[Picking, _Mapping]] = ...,
    ) -> None: ...

class PickingReadRequest(_message.Message):
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

class PickingReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "pickings"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PICKINGS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    pickings: _containers.RepeatedCompositeFieldContainer[Picking]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        pickings: _Optional[_Iterable[_Union[Picking, _Mapping]]] = ...,
    ) -> None: ...

class PickingUpdateRequest(_message.Message):
    __slots__ = ["picking", "context"]
    PICKING_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    picking: Picking
    context: _base_pb2.Context
    def __init__(
        self,
        picking: _Optional[_Union[Picking, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "picking"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    PICKING_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    picking: Picking
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        picking: _Optional[_Union[Picking, _Mapping]] = ...,
    ) -> None: ...

class PickingDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class PickingDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class ValidatePickingRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ValidatePickingResponse(_message.Message):
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
