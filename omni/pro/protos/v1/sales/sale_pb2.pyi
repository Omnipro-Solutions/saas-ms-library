from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Sale(_message.Message):
    __slots__ = [
        "active",
        "bill_address_id",
        "channel_id",
        "client_id",
        "confirm_date",
        "country_id",
        "currency_id",
        "date_order",
        "id",
        "json_order",
        "name",
        "object_audit",
        "origin",
        "warehouse_id",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    BILL_ADDRESS_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_ORDER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    JSON_ORDER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    bill_address_id: int
    channel_id: int
    client_id: int
    confirm_date: _timestamp_pb2.Timestamp
    country_id: int
    currency_id: int
    date_order: _timestamp_pb2.Timestamp
    id: int
    json_order: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    origin: str
    warehouse_id: int
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
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class SaleCreateRequest(_message.Message):
    __slots__ = [
        "bill_address_id",
        "channel_id",
        "client_id",
        "confirm_date",
        "context",
        "country_id",
        "currency_id",
        "date_order",
        "json_order",
        "name",
        "origin",
        "warehouse_id",
    ]
    BILL_ADDRESS_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DATE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_ORDER_FIELD_NUMBER: _ClassVar[int]
    JSON_ORDER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    bill_address_id: int
    channel_id: int
    client_id: int
    confirm_date: _timestamp_pb2.Timestamp
    context: _base_pb2.Context
    country_id: int
    currency_id: int
    date_order: _timestamp_pb2.Timestamp
    json_order: str
    name: str
    origin: str
    warehouse_id: int
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
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class SaleCreateResponse(_message.Message):
    __slots__ = ["response_standard", "sale"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    SALE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    sale: Sale
    def __init__(
        self,
        sale: _Optional[_Union[Sale, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class SaleDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class SaleDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class SaleReadRequest(_message.Message):
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

class SaleReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "sale"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    SALE_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    sale: _containers.RepeatedCompositeFieldContainer[Sale]
    def __init__(
        self,
        sale: _Optional[_Iterable[_Union[Sale, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class SaleUpdateRequest(_message.Message):
    __slots__ = ["context", "sale"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SALE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    sale: Sale
    def __init__(
        self,
        sale: _Optional[_Union[Sale, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class SaleUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "sale"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    SALE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    sale: Sale
    def __init__(
        self,
        sale: _Optional[_Union[Sale, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
