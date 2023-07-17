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

DESCRIPTOR: _descriptor.FileDescriptor

class Currency(_message.Message):
    __slots__ = [
        "active",
        "code",
        "currency_subunit_label",
        "currency_unit_label",
        "decimal_places",
        "id",
        "name",
        "object_audit",
        "position",
        "rate",
        "rounding",
        "symbol",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SUBUNIT_LABEL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_UNIT_LABEL_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PLACES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    ROUNDING_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    code: str
    currency_subunit_label: str
    currency_unit_label: str
    decimal_places: int
    id: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    position: str
    rate: int
    rounding: float
    symbol: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        currency_unit_label: _Optional[str] = ...,
        currency_subunit_label: _Optional[str] = ...,
        rate: _Optional[int] = ...,
        rounding: _Optional[float] = ...,
        decimal_places: _Optional[int] = ...,
        symbol: _Optional[str] = ...,
        position: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class CurrencyAddRequest(_message.Message):
    __slots__ = [
        "active",
        "code",
        "context",
        "currency_subunit_label",
        "currency_unit_label",
        "decimal_places",
        "name",
        "position",
        "rate",
        "rounding",
        "symbol",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_SUBUNIT_LABEL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_UNIT_LABEL_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PLACES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    ROUNDING_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    code: str
    context: _base_pb2.Context
    currency_subunit_label: str
    currency_unit_label: str
    decimal_places: int
    name: str
    position: str
    rate: int
    rounding: float
    symbol: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        currency_unit_label: _Optional[str] = ...,
        currency_subunit_label: _Optional[str] = ...,
        rate: _Optional[int] = ...,
        rounding: _Optional[float] = ...,
        decimal_places: _Optional[int] = ...,
        symbol: _Optional[str] = ...,
        position: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CurrencyAddResponse(_message.Message):
    __slots__ = ["currency", "response_standard"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    currency: Currency
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        currency: _Optional[_Union[Currency, _Mapping]] = ...,
    ) -> None: ...

class CurrencyDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: str
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class CurrencyDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class CurrencyReadRequest(_message.Message):
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
    id: str
    paginated: _base_pb2.Paginated
    sort_by: _base_pb2.SortBy
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

class CurrencyReadResponse(_message.Message):
    __slots__ = ["currencies", "meta_data", "response_standard"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[Currency]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        currencies: _Optional[_Iterable[_Union[Currency, _Mapping]]] = ...,
    ) -> None: ...

class CurrencyUpdateRequest(_message.Message):
    __slots__ = ["context", "currency"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    currency: Currency
    def __init__(
        self,
        currency: _Optional[_Union[Currency, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CurrencyUpdateResponse(_message.Message):
    __slots__ = ["currency", "response_standard"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    currency: Currency
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        currency: _Optional[_Union[Currency, _Mapping]] = ...,
    ) -> None: ...
