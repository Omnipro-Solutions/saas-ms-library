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

class Attachment(_message.Message):
    __slots__ = ["active", "doc_id", "id", "name", "object_audit", "type"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    doc_id: str
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    type: str
    def __init__(
        self,
        id: _Optional[int] = ...,
        doc_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        type: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class AttachmentCreateRequest(_message.Message):
    __slots__ = ["context", "doc_id", "name", "type"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    doc_id: str
    name: str
    type: str
    def __init__(
        self,
        doc_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        type: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttachmentCreateResponse(_message.Message):
    __slots__ = ["attachment", "response_standard"]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    attachment: Attachment
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attachment: _Optional[_Union[Attachment, _Mapping]] = ...,
    ) -> None: ...

class AttachmentDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class AttachmentDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class AttachmentReadRequest(_message.Message):
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

class AttachmentReadResponse(_message.Message):
    __slots__ = ["attachments", "meta_data", "response_standard"]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ...,
    ) -> None: ...

class AttachmentUpdateRequest(_message.Message):
    __slots__ = ["attachment", "context"]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    attachment: Attachment
    context: _base_pb2.Context
    def __init__(
        self,
        attachment: _Optional[_Union[Attachment, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttachmentUpdateResponse(_message.Message):
    __slots__ = ["attachment", "response_standard"]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    attachment: Attachment
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attachment: _Optional[_Union[Attachment, _Mapping]] = ...,
    ) -> None: ...

class Carrier(_message.Message):
    __slots__ = ["active", "code", "id", "name", "object_audit"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    code: str
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class CarrierCreateRequest(_message.Message):
    __slots__ = ["code", "context", "name"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    name: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CarrierCreateResponse(_message.Message):
    __slots__ = ["carrier", "response_standard"]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    carrier: Carrier
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        carrier: _Optional[_Union[Carrier, _Mapping]] = ...,
    ) -> None: ...

class CarrierDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class CarrierDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class CarrierReadRequest(_message.Message):
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

class CarrierReadResponse(_message.Message):
    __slots__ = ["carriers", "meta_data", "response_standard"]
    CARRIERS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    carriers: _containers.RepeatedCompositeFieldContainer[Carrier]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        carriers: _Optional[_Iterable[_Union[Carrier, _Mapping]]] = ...,
    ) -> None: ...

class CarrierUpdateRequest(_message.Message):
    __slots__ = ["carrier", "context"]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    carrier: Carrier
    context: _base_pb2.Context
    def __init__(
        self,
        carrier: _Optional[_Union[Carrier, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CarrierUpdateResponse(_message.Message):
    __slots__ = ["carrier", "response_standard"]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    carrier: Carrier
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        carrier: _Optional[_Union[Carrier, _Mapping]] = ...,
    ) -> None: ...

class Picking(_message.Message):
    __slots__ = [
        "active",
        "attachment_guide_id",
        "attachment_invoice_id",
        "carrier_id",
        "carrier_tracking_ref",
        "date_delivery",
        "date_done",
        "date_start_preparation",
        "group_id",
        "id",
        "location_dest_id",
        "location_id",
        "name",
        "object_audit",
        "origin",
        "picking_type_id",
        "scheduled_date",
        "shipping_weight",
        "time_assigned",
        "time_total_preparation",
        "user_id",
        "weight",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_GUIDE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    CARRIER_ID_FIELD_NUMBER: _ClassVar[int]
    CARRIER_TRACKING_REF_FIELD_NUMBER: _ClassVar[int]
    DATE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    DATE_DONE_FIELD_NUMBER: _ClassVar[int]
    DATE_START_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DEST_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    TIME_TOTAL_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    attachment_guide_id: int
    attachment_invoice_id: int
    carrier_id: int
    carrier_tracking_ref: str
    date_delivery: _timestamp_pb2.Timestamp
    date_done: _timestamp_pb2.Timestamp
    date_start_preparation: _timestamp_pb2.Timestamp
    group_id: int
    id: int
    location_dest_id: int
    location_id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    origin: str
    picking_type_id: int
    scheduled_date: _timestamp_pb2.Timestamp
    shipping_weight: float
    time_assigned: float
    time_total_preparation: float
    user_id: int
    weight: float
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        picking_type_id: _Optional[int] = ...,
        location_id: _Optional[int] = ...,
        location_dest_id: _Optional[int] = ...,
        user_id: _Optional[int] = ...,
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
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class PickingCreateRequest(_message.Message):
    __slots__ = [
        "attachment_guide_id",
        "attachment_invoice_id",
        "carrier_id",
        "carrier_tracking_ref",
        "context",
        "date_delivery",
        "date_done",
        "date_start_preparation",
        "group_id",
        "location_dest_id",
        "location_id",
        "name",
        "origin",
        "picking_type_id",
        "scheduled_date",
        "shipping_weight",
        "time_assigned",
        "time_total_preparation",
        "user_id",
        "weight",
    ]
    ATTACHMENT_GUIDE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    CARRIER_ID_FIELD_NUMBER: _ClassVar[int]
    CARRIER_TRACKING_REF_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DATE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    DATE_DONE_FIELD_NUMBER: _ClassVar[int]
    DATE_START_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_DEST_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_ASSIGNED_FIELD_NUMBER: _ClassVar[int]
    TIME_TOTAL_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    attachment_guide_id: int
    attachment_invoice_id: int
    carrier_id: int
    carrier_tracking_ref: str
    context: _base_pb2.Context
    date_delivery: _timestamp_pb2.Timestamp
    date_done: _timestamp_pb2.Timestamp
    date_start_preparation: _timestamp_pb2.Timestamp
    group_id: int
    location_dest_id: int
    location_id: int
    name: str
    origin: str
    picking_type_id: int
    scheduled_date: _timestamp_pb2.Timestamp
    shipping_weight: float
    time_assigned: float
    time_total_preparation: float
    user_id: int
    weight: float
    def __init__(
        self,
        name: _Optional[str] = ...,
        picking_type_id: _Optional[int] = ...,
        location_id: _Optional[int] = ...,
        location_dest_id: _Optional[int] = ...,
        user_id: _Optional[int] = ...,
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
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingCreateResponse(_message.Message):
    __slots__ = ["picking", "response_standard"]
    PICKING_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    picking: Picking
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        picking: _Optional[_Union[Picking, _Mapping]] = ...,
    ) -> None: ...

class PickingDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class PickingDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class PickingReadRequest(_message.Message):
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

class PickingReadResponse(_message.Message):
    __slots__ = ["meta_data", "pickings", "response_standard"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PICKINGS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    pickings: _containers.RepeatedCompositeFieldContainer[Picking]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        pickings: _Optional[_Iterable[_Union[Picking, _Mapping]]] = ...,
    ) -> None: ...

class PickingUpdateRequest(_message.Message):
    __slots__ = ["context", "picking"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PICKING_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    picking: Picking
    def __init__(
        self,
        picking: _Optional[_Union[Picking, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingUpdateResponse(_message.Message):
    __slots__ = ["picking", "response_standard"]
    PICKING_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    picking: Picking
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        picking: _Optional[_Union[Picking, _Mapping]] = ...,
    ) -> None: ...

class ProcurementGroup(_message.Message):
    __slots__ = ["active", "id", "move_type", "name", "object_audit"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MOVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    id: int
    move_type: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        move_type: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class ProcurementGroupCreateRequest(_message.Message):
    __slots__ = ["context", "move_type", "name"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MOVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    move_type: str
    name: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        move_type: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ProcurementGroupCreateResponse(_message.Message):
    __slots__ = ["procurement_group", "response_standard"]
    PROCUREMENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    procurement_group: ProcurementGroup
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        procurement_group: _Optional[_Union[ProcurementGroup, _Mapping]] = ...,
    ) -> None: ...

class ProcurementGroupDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ProcurementGroupDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class ProcurementGroupReadRequest(_message.Message):
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

class ProcurementGroupReadResponse(_message.Message):
    __slots__ = ["meta_data", "procurement_groups", "response_standard"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PROCUREMENT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    procurement_groups: _containers.RepeatedCompositeFieldContainer[ProcurementGroup]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        procurement_groups: _Optional[_Iterable[_Union[ProcurementGroup, _Mapping]]] = ...,
    ) -> None: ...

class ProcurementGroupUpdateRequest(_message.Message):
    __slots__ = ["context", "procurement_group"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PROCUREMENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    procurement_group: ProcurementGroup
    def __init__(
        self,
        procurement_group: _Optional[_Union[ProcurementGroup, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ProcurementGroupUpdateResponse(_message.Message):
    __slots__ = ["procurement_group", "response_standard"]
    PROCUREMENT_GROUP_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    procurement_group: ProcurementGroup
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        procurement_group: _Optional[_Union[ProcurementGroup, _Mapping]] = ...,
    ) -> None: ...

class User(_message.Message):
    __slots__ = ["active", "id", "name", "object_audit", "user_doc_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    USER_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    user_doc_id: str
    def __init__(
        self,
        id: _Optional[int] = ...,
        user_doc_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class UserCreateRequest(_message.Message):
    __slots__ = ["context", "name", "user_doc_id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    name: str
    user_doc_id: str
    def __init__(
        self,
        user_doc_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class UserCreateResponse(_message.Message):
    __slots__ = ["response_standard", "user"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    user: User
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        user: _Optional[_Union[User, _Mapping]] = ...,
    ) -> None: ...

class UserDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class UserDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class UserReadRequest(_message.Message):
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

class UserReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "users"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...,
    ) -> None: ...

class UserUpdateRequest(_message.Message):
    __slots__ = ["context", "user"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    user: User
    def __init__(
        self,
        user: _Optional[_Union[User, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class UserUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "user"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    user: User
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        user: _Optional[_Union[User, _Mapping]] = ...,
    ) -> None: ...
