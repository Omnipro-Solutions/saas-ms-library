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

DESCRIPTOR: _descriptor.FileDescriptor

class Sale(_message.Message):
    __slots__ = [
        "id",
        "name",
        "date_order",
        "origin",
        "channel_id",
        "currency_id",
        "confirm_date",
        "client_id",
        "bill_address_id",
        "country_id",
        "warehouse_id",
        "json_order",
        "state_id",
        "state",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_ORDER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BILL_ADDRESS_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    JSON_ORDER_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    date_order: _timestamp_pb2.Timestamp
    origin: str
    channel_id: int
    currency_id: int
    confirm_date: _timestamp_pb2.Timestamp
    client_id: int
    bill_address_id: int
    country_id: int
    warehouse_id: int
    json_order: str
    state_id: int
    state: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        date_order: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        origin: _Optional[str] = ...,
        channel_id: _Optional[int] = ...,
        currency_id: _Optional[int] = ...,
        confirm_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        client_id: _Optional[int] = ...,
        bill_address_id: _Optional[int] = ...,
        country_id: _Optional[int] = ...,
        warehouse_id: _Optional[int] = ...,
        json_order: _Optional[str] = ...,
        state_id: _Optional[int] = ...,
        state: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class SaleIntegration(_message.Message):
    __slots__ = ["order_details", "oms_rules", "client_details", "payment", "order_items", "shipping"]
    ORDER_DETAILS_FIELD_NUMBER: _ClassVar[int]
    OMS_RULES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    ORDER_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_FIELD_NUMBER: _ClassVar[int]
    order_details: _struct_pb2.Struct
    oms_rules: _struct_pb2.Struct
    client_details: _struct_pb2.Struct
    payment: _struct_pb2.Struct
    order_items: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    shipping: _struct_pb2.Struct
    def __init__(
        self,
        order_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        oms_rules: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        client_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        payment: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        order_items: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        shipping: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
    ) -> None: ...

class SaleCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "date_order",
        "origin",
        "channel_id",
        "currency_id",
        "confirm_date",
        "client_id",
        "bill_address_id",
        "country_id",
        "warehouse_id",
        "json_order",
        "state_id",
        "state",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_ORDER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    BILL_ADDRESS_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    JSON_ORDER_FIELD_NUMBER: _ClassVar[int]
    STATE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    date_order: _timestamp_pb2.Timestamp
    origin: str
    channel_id: int
    currency_id: int
    confirm_date: _timestamp_pb2.Timestamp
    client_id: int
    bill_address_id: int
    country_id: int
    warehouse_id: int
    json_order: str
    state_id: int
    state: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        date_order: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        origin: _Optional[str] = ...,
        channel_id: _Optional[int] = ...,
        currency_id: _Optional[int] = ...,
        confirm_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        client_id: _Optional[int] = ...,
        bill_address_id: _Optional[int] = ...,
        country_id: _Optional[int] = ...,
        warehouse_id: _Optional[int] = ...,
        json_order: _Optional[str] = ...,
        state_id: _Optional[int] = ...,
        state: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class SaleCreateResponse(_message.Message):
    __slots__ = ["sale", "response_standard"]
    SALE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    sale: Sale
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        sale: _Optional[_Union[Sale, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class SaleReadRequest(_message.Message):
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

class SaleReadResponse(_message.Message):
    __slots__ = ["sale", "response_standard", "meta_data"]
    SALE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    sale: _containers.RepeatedCompositeFieldContainer[Sale]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    def __init__(
        self,
        sale: _Optional[_Iterable[_Union[Sale, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class SaleUpdateRequest(_message.Message):
    __slots__ = ["sale", "context"]
    SALE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    sale: Sale
    context: _base_pb2.Context
    def __init__(
        self,
        sale: _Optional[_Union[Sale, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class SaleUpdateResponse(_message.Message):
    __slots__ = ["sale", "response_standard"]
    SALE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    sale: Sale
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        sale: _Optional[_Union[Sale, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class SaleDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: int
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class SaleDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class SaleCreateIntegrationRequest(_message.Message):
    __slots__ = ["sale_integration", "context"]
    SALE_INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    sale_integration: SaleIntegration
    context: _base_pb2.Context
    def __init__(
        self,
        sale_integration: _Optional[_Union[SaleIntegration, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class SaleCreateIntegrationResponse(_message.Message):
    __slots__ = ["sale", "response_standard"]
    SALE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    sale: Sale
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        sale: _Optional[_Union[Sale, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
