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

DESCRIPTOR: _descriptor.FileDescriptor

class Country(_message.Message):
    __slots__ = [
        "id",
        "code",
        "name",
        "phone_number_size",
        "phone_prefix",
        "require_zipcode",
        "currencies",
        "document_types",
        "territory_matrixes",
        "meta_data",
        "timezones",
        "languages",
        "low_level",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_SIZE_FIELD_NUMBER: _ClassVar[int]
    PHONE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ZIPCODE_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    TIMEZONES_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    LOW_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    name: str
    phone_number_size: int
    phone_prefix: str
    require_zipcode: _wrappers_pb2.BoolValue
    currencies: _struct_pb2.ListValue
    document_types: _struct_pb2.ListValue
    territory_matrixes: _struct_pb2.ListValue
    meta_data: _struct_pb2.Struct
    timezones: _struct_pb2.ListValue
    languages: _struct_pb2.ListValue
    low_level: str
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        phone_number_size: _Optional[int] = ...,
        phone_prefix: _Optional[str] = ...,
        require_zipcode: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        currencies: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        document_types: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        territory_matrixes: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        meta_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        timezones: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        languages: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        low_level: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class CountryCreateRequest(_message.Message):
    __slots__ = [
        "code",
        "name",
        "phone_number_size",
        "phone_prefix",
        "require_zipcode",
        "currencies_ids",
        "document_types_ids",
        "territory_matrixes_ids",
        "meta_data",
        "timezones_ids",
        "languages_ids",
        "low_level",
        "context",
    ]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_SIZE_FIELD_NUMBER: _ClassVar[int]
    PHONE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ZIPCODE_FIELD_NUMBER: _ClassVar[int]
    CURRENCIES_IDS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPES_IDS_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_IDS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    TIMEZONES_IDS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_IDS_FIELD_NUMBER: _ClassVar[int]
    LOW_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    phone_number_size: int
    phone_prefix: str
    require_zipcode: _wrappers_pb2.BoolValue
    currencies_ids: _struct_pb2.ListValue
    document_types_ids: _struct_pb2.ListValue
    territory_matrixes_ids: _struct_pb2.ListValue
    meta_data: _struct_pb2.Struct
    timezones_ids: _struct_pb2.ListValue
    languages_ids: _struct_pb2.ListValue
    low_level: str
    context: _base_pb2.Context
    def __init__(
        self,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        phone_number_size: _Optional[int] = ...,
        phone_prefix: _Optional[str] = ...,
        require_zipcode: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        currencies_ids: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        document_types_ids: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        territory_matrixes_ids: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        meta_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        timezones_ids: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        languages_ids: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        low_level: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CountryCreateResponse(_message.Message):
    __slots__ = ["response_standard", "country"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    country: Country
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        country: _Optional[_Union[Country, _Mapping]] = ...,
    ) -> None: ...

class CountryReadRequest(_message.Message):
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

class CountryReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "countries"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    countries: _containers.RepeatedCompositeFieldContainer[Country]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        countries: _Optional[_Iterable[_Union[Country, _Mapping]]] = ...,
    ) -> None: ...

class CountryUpdateRequest(_message.Message):
    __slots__ = ["country", "context"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    country: Country
    context: _base_pb2.Context
    def __init__(
        self,
        country: _Optional[_Union[Country, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class CountryUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "country"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    country: Country
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        country: _Optional[_Union[Country, _Mapping]] = ...,
    ) -> None: ...

class CountryDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class CountryDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
