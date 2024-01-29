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
from omni.pro.protos.v1.rules import delivery_method_pb2 as _delivery_method_pb2
from omni.pro.protos.v1.rules import holidays_pb2 as _holidays_pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AppointmentTemplateLines(_message.Message):
    __slots__ = ["day", "hour_start", "hour_end", "order_numbers"]
    DAY_FIELD_NUMBER: _ClassVar[int]
    HOUR_START_FIELD_NUMBER: _ClassVar[int]
    HOUR_END_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    day: str
    hour_start: str
    hour_end: str
    order_numbers: int
    def __init__(
        self,
        day: _Optional[str] = ...,
        hour_start: _Optional[str] = ...,
        hour_end: _Optional[str] = ...,
        order_numbers: _Optional[int] = ...,
    ) -> None: ...

class AppointmentTemplate(_message.Message):
    __slots__ = [
        "id",
        "name",
        "warehouses",
        "methods",
        "order_numbers",
        "hour_limit_same_day",
        "number_days_to_show",
        "holidays",
        "lines",
        "active",
        "external_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSES_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    HOUR_LIMIT_SAME_DAY_FIELD_NUMBER: _ClassVar[int]
    NUMBER_DAYS_TO_SHOW_FIELD_NUMBER: _ClassVar[int]
    HOLIDAYS_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    warehouses: _containers.RepeatedCompositeFieldContainer[_warehouse_pb2.Warehouse]
    methods: _containers.RepeatedCompositeFieldContainer[_delivery_method_pb2.DeliveryMethod]
    order_numbers: int
    hour_limit_same_day: str
    number_days_to_show: int
    holidays: _holidays_pb2.Holidays
    lines: _containers.RepeatedCompositeFieldContainer[AppointmentTemplateLines]
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        warehouses: _Optional[_Iterable[_Union[_warehouse_pb2.Warehouse, _Mapping]]] = ...,
        methods: _Optional[_Iterable[_Union[_delivery_method_pb2.DeliveryMethod, _Mapping]]] = ...,
        order_numbers: _Optional[int] = ...,
        hour_limit_same_day: _Optional[str] = ...,
        number_days_to_show: _Optional[int] = ...,
        holidays: _Optional[_Union[_holidays_pb2.Holidays, _Mapping]] = ...,
        lines: _Optional[_Iterable[_Union[AppointmentTemplateLines, _Mapping]]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class AppointmentTemplateCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "warehouse_ids",
        "method_ids",
        "order_numbers",
        "hour_limit_same_day",
        "number_days_to_show",
        "holiday_id",
        "lines",
        "external_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    METHOD_IDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    HOUR_LIMIT_SAME_DAY_FIELD_NUMBER: _ClassVar[int]
    NUMBER_DAYS_TO_SHOW_FIELD_NUMBER: _ClassVar[int]
    HOLIDAY_ID_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    warehouse_ids: _containers.RepeatedScalarFieldContainer[int]
    method_ids: _containers.RepeatedScalarFieldContainer[str]
    order_numbers: int
    hour_limit_same_day: str
    number_days_to_show: int
    holiday_id: str
    lines: _containers.RepeatedCompositeFieldContainer[AppointmentTemplateLines]
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        warehouse_ids: _Optional[_Iterable[int]] = ...,
        method_ids: _Optional[_Iterable[str]] = ...,
        order_numbers: _Optional[int] = ...,
        hour_limit_same_day: _Optional[str] = ...,
        number_days_to_show: _Optional[int] = ...,
        holiday_id: _Optional[str] = ...,
        lines: _Optional[_Iterable[_Union[AppointmentTemplateLines, _Mapping]]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AppointmentTemplateCreateResponse(_message.Message):
    __slots__ = ["appointment_template", "response_standard"]
    APPOINTMENT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    appointment_template: AppointmentTemplate
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        appointment_template: _Optional[_Union[AppointmentTemplate, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AppointmentTemplateReadRequest(_message.Message):
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

class AppointmentTemplateReadResponse(_message.Message):
    __slots__ = ["appointment_templates", "meta_data", "response_standard"]
    APPOINTMENT_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    appointment_templates: _containers.RepeatedCompositeFieldContainer[AppointmentTemplate]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        appointment_templates: _Optional[_Iterable[_Union[AppointmentTemplate, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AppointmentTemplateUpdateRequest(_message.Message):
    __slots__ = ["appointment_template", "context"]
    APPOINTMENT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    appointment_template: AppointmentTemplate
    context: _base_pb2.Context
    def __init__(
        self,
        appointment_template: _Optional[_Union[AppointmentTemplate, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AppointmentTemplateUpdateResponse(_message.Message):
    __slots__ = ["appointment_template", "response_standard"]
    APPOINTMENT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    appointment_template: AppointmentTemplate
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        appointment_template: _Optional[_Union[AppointmentTemplate, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class AppointmentTemplateDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class AppointmentTemplateDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
