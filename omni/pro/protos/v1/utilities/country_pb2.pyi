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
from omni.pro.protos.v1.utilities import currency_pb2 as _currency_pb2
from omni.pro.protos.v1.utilities import document_type_pb2 as _document_type_pb2
from omni.pro.protos.v1.utilities import language_pb2 as _language_pb2
from omni.pro.protos.v1.utilities import territory_matrix_pb2 as _territory_matrix_pb2
from omni.pro.protos.v1.utilities import timezone_pb2 as _timezone_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Country(_message.Message):
    __slots__ = [
        "active",
        "code",
        "currency",
        "document_types",
        "id",
        "languages",
        "low_level",
        "meta_data",
        "name",
        "object_audit",
        "phone_number_size",
        "phone_prefix",
        "require_zipcode",
        "territory_matrixes",
        "timezones",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    LOW_LEVEL_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_SIZE_FIELD_NUMBER: _ClassVar[int]
    PHONE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ZIPCODE_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONES_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    code: str
    currency: _currency_pb2.Currency
    document_types: _containers.RepeatedCompositeFieldContainer[_document_type_pb2.DocumentType]
    id: str
    languages: _containers.RepeatedCompositeFieldContainer[_language_pb2.Language]
    low_level: str
    meta_data: _struct_pb2.Struct
    name: str
    object_audit: _base_pb2.ObjectAudit
    phone_number_size: int
    phone_prefix: str
    require_zipcode: _wrappers_pb2.BoolValue
    territory_matrixes: _containers.RepeatedCompositeFieldContainer[_territory_matrix_pb2.TerritoryMatrix]
    timezones: _containers.RepeatedCompositeFieldContainer[_timezone_pb2.Timezone]
    def __init__(
        self,
        id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        phone_number_size: _Optional[int] = ...,
        phone_prefix: _Optional[str] = ...,
        require_zipcode: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ...,
        document_types: _Optional[_Iterable[_Union[_document_type_pb2.DocumentType, _Mapping]]] = ...,
        territory_matrixes: _Optional[_Iterable[_Union[_territory_matrix_pb2.TerritoryMatrix, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        timezones: _Optional[_Iterable[_Union[_timezone_pb2.Timezone, _Mapping]]] = ...,
        languages: _Optional[_Iterable[_Union[_language_pb2.Language, _Mapping]]] = ...,
        low_level: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class CountryCreateRequest(_message.Message):
    __slots__ = [
        "code",
        "context",
        "currency",
        "document_types",
        "languages",
        "low_level",
        "meta_data",
        "name",
        "phone_number_size",
        "phone_prefix",
        "require_zipcode",
        "territory_matrixes",
        "timezones",
    ]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    LOW_LEVEL_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_SIZE_FIELD_NUMBER: _ClassVar[int]
    PHONE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ZIPCODE_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONES_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    currency: _currency_pb2.Currency
    document_types: _containers.RepeatedCompositeFieldContainer[_document_type_pb2.DocumentType]
    languages: _containers.RepeatedCompositeFieldContainer[_language_pb2.Language]
    low_level: str
    meta_data: _struct_pb2.Struct
    name: str
    phone_number_size: int
    phone_prefix: str
    require_zipcode: bool
    territory_matrixes: _containers.RepeatedCompositeFieldContainer[_territory_matrix_pb2.TerritoryMatrix]
    timezones: _containers.RepeatedCompositeFieldContainer[_timezone_pb2.Timezone]
    def __init__(
        self,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        phone_number_size: _Optional[int] = ...,
        phone_prefix: _Optional[str] = ...,
        require_zipcode: bool = ...,
        currency: _Optional[_Union[_currency_pb2.Currency, _Mapping]] = ...,
        document_types: _Optional[_Iterable[_Union[_document_type_pb2.DocumentType, _Mapping]]] = ...,
        territory_matrixes: _Optional[_Iterable[_Union[_territory_matrix_pb2.TerritoryMatrix, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        timezones: _Optional[_Iterable[_Union[_timezone_pb2.Timezone, _Mapping]]] = ...,
        languages: _Optional[_Iterable[_Union[_language_pb2.Language, _Mapping]]] = ...,
        low_level: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CountryCreateResponse(_message.Message):
    __slots__ = ["country", "response_standard"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    country: Country
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        country: _Optional[_Union[Country, _Mapping]] = ...,
    ) -> None: ...

class CountryDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: str
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class CountryDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class CountryReadRequest(_message.Message):
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

class CountryReadResponse(_message.Message):
    __slots__ = ["countries", "meta_data", "response_standard"]
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    countries: _containers.RepeatedCompositeFieldContainer[Country]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        countries: _Optional[_Iterable[_Union[Country, _Mapping]]] = ...,
    ) -> None: ...

class CountryUpdateRequest(_message.Message):
    __slots__ = ["context", "country"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    country: Country
    def __init__(
        self,
        country: _Optional[_Union[Country, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CountryUpdateResponse(_message.Message):
    __slots__ = ["country", "response_standard"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    country: Country
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        country: _Optional[_Union[Country, _Mapping]] = ...,
    ) -> None: ...
