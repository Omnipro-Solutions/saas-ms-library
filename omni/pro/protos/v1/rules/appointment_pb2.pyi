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
from omni.pro.protos.v1.rules import delivery_method_pb2 as _delivery_method_pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AppointmentLines(_message.Message):
    __slots__ = ["hour_start", "hour_end", "order_numbers", "appointment_available", "cids", "id"]
    HOUR_START_FIELD_NUMBER: _ClassVar[int]
    HOUR_END_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    APPOINTMENT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    CIDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    hour_start: str
    hour_end: str
    order_numbers: int
    appointment_available: int
    cids: _containers.RepeatedScalarFieldContainer[str]
    id: str
    def __init__(
        self,
        hour_start: _Optional[str] = ...,
        hour_end: _Optional[str] = ...,
        order_numbers: _Optional[int] = ...,
        appointment_available: _Optional[int] = ...,
        cids: _Optional[_Iterable[str]] = ...,
        id: _Optional[str] = ...,
    ) -> None: ...

class Appointment(_message.Message):
    __slots__ = ["id", "warehouse", "method", "date", "lines", "active", "external_id", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    warehouse: _warehouse_pb2.Warehouse
    method: _delivery_method_pb2.DeliveryMethod
    date: str
    lines: _containers.RepeatedCompositeFieldContainer[AppointmentLines]
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        warehouse: _Optional[_Union[_warehouse_pb2.Warehouse, _Mapping]] = ...,
        method: _Optional[_Union[_delivery_method_pb2.DeliveryMethod, _Mapping]] = ...,
        date: _Optional[str] = ...,
        lines: _Optional[_Iterable[_Union[AppointmentLines, _Mapping]]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class AppointmentCreateRequest(_message.Message):
    __slots__ = ["warehouse_id", "method_id", "date", "lines", "external_id", "context"]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    warehouse_id: int
    method_id: str
    date: str
    lines: _containers.RepeatedCompositeFieldContainer[AppointmentLines]
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        warehouse_id: _Optional[int] = ...,
        method_id: _Optional[str] = ...,
        date: _Optional[str] = ...,
        lines: _Optional[_Iterable[_Union[AppointmentLines, _Mapping]]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AppointmentCreateResponse(_message.Message):
    __slots__ = ["appointment", "response_standard"]
    APPOINTMENT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    appointment: Appointment
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        appointment: _Optional[_Union[Appointment, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AppointmentReadRequest(_message.Message):
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
    id: str
    context: _base_pb2.Context
    def __init__(
        self,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AppointmentReadResponse(_message.Message):
    __slots__ = ["appointments", "meta_data", "response_standard"]
    APPOINTMENTS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    appointments: _containers.RepeatedCompositeFieldContainer[Appointment]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        appointments: _Optional[_Iterable[_Union[Appointment, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AppointmentUpdateRequest(_message.Message):
    __slots__ = ["appointment", "context"]
    APPOINTMENT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    appointment: Appointment
    context: _base_pb2.Context
    def __init__(
        self,
        appointment: _Optional[_Union[Appointment, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AppointmentUpdateResponse(_message.Message):
    __slots__ = ["appointment", "response_standard"]
    APPOINTMENT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    appointment: Appointment
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        appointment: _Optional[_Union[Appointment, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AppointmentDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class AppointmentDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class SearchAppointmentRequest(_message.Message):
    __slots__ = ["cids", "context"]
    CIDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    cids: _containers.RepeatedScalarFieldContainer[str]
    context: _base_pb2.Context
    def __init__(
        self, cids: _Optional[_Iterable[str]] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class SearchAppointmentResponse(_message.Message):
    __slots__ = ["data", "response_standard"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    data: _struct_pb2.Struct
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AppointmentConfirmData(_message.Message):
    __slots__ = ["aids", "cid"]
    AIDS_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    aids: _containers.RepeatedScalarFieldContainer[str]
    cid: str
    def __init__(self, aids: _Optional[_Iterable[str]] = ..., cid: _Optional[str] = ...) -> None: ...

class ConfirmAppointmentRequest(_message.Message):
    __slots__ = ["data", "context"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[AppointmentConfirmData]
    context: _base_pb2.Context
    def __init__(
        self,
        data: _Optional[_Iterable[_Union[AppointmentConfirmData, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ConfirmAppointmentResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
