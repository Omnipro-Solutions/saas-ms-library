from common import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Language(_message.Message):
    __slots__ = ["active", "code", "name", "object_audit"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    active: bool
    code: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(self, name: _Optional[str] = ..., code: _Optional[str] = ..., active: bool = ..., object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...) -> None: ...

class LanguageAddRequest(_message.Message):
    __slots__ = ["code", "context", "country_id", "name"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    country_id: str
    name: str
    def __init__(self, country_id: _Optional[str] = ..., name: _Optional[str] = ..., code: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class LanguageAddResponse(_message.Message):
    __slots__ = ["language", "response_standard"]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    language: Language
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ..., language: _Optional[_Union[Language, _Mapping]] = ...) -> None: ...

class LanguageDeleteRequest(_message.Message):
    __slots__ = ["code", "context", "country_id"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    country_id: str
    def __init__(self, country_id: _Optional[str] = ..., code: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class LanguageDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class LanguageReadRequest(_message.Message):
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
    def __init__(self, group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ..., sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ..., fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ..., filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ..., paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ..., id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class LanguageReadResponse(_message.Message):
    __slots__ = ["languages", "meta_data", "response_standard"]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    languages: _containers.RepeatedCompositeFieldContainer[Language]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ..., meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ..., languages: _Optional[_Iterable[_Union[Language, _Mapping]]] = ...) -> None: ...

class LanguageUpdateRequest(_message.Message):
    __slots__ = ["code", "context", "country_id", "language"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    country_id: str
    language: Language
    def __init__(self, country_id: _Optional[str] = ..., code: _Optional[str] = ..., language: _Optional[_Union[Language, _Mapping]] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class LanguageUpdateResponse(_message.Message):
    __slots__ = ["language", "response_standard"]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    language: Language
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ..., language: _Optional[_Union[Language, _Mapping]] = ...) -> None: ...
