from common import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DocumentType(_message.Message):
    __slots__ = ["active", "code", "name", "object_audit", "size"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    code: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    size: int
    def __init__(self, name: _Optional[str] = ..., code: _Optional[str] = ..., size: _Optional[int] = ..., active: bool = ..., object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...) -> None: ...

class DocumentTypeAddRequest(_message.Message):
    __slots__ = ["active", "code", "context", "country_id", "name", "size"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    code: str
    context: _base_pb2.Context
    country_id: str
    name: str
    size: int
    def __init__(self, country_id: _Optional[str] = ..., name: _Optional[str] = ..., code: _Optional[str] = ..., size: _Optional[int] = ..., active: bool = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class DocumentTypeAddResponse(_message.Message):
    __slots__ = ["document_type", "response_standard"]
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    document_type: DocumentType
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ..., document_type: _Optional[_Union[DocumentType, _Mapping]] = ...) -> None: ...

class DocumentTypeDeleteRequest(_message.Message):
    __slots__ = ["code", "context", "country_id"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    country_id: str
    def __init__(self, country_id: _Optional[str] = ..., code: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class DocumentTypeDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DocumentTypeReadRequest(_message.Message):
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

class DocumentTypeReadResponse(_message.Message):
    __slots__ = ["document_types", "meta_data", "response_standard"]
    DOCUMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    document_types: _containers.RepeatedCompositeFieldContainer[DocumentType]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ..., meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ..., document_types: _Optional[_Iterable[_Union[DocumentType, _Mapping]]] = ...) -> None: ...

class DocumentTypeUpdateRequest(_message.Message):
    __slots__ = ["code", "context", "country_id", "document_type"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    country_id: str
    document_type: DocumentType
    def __init__(self, country_id: _Optional[str] = ..., code: _Optional[str] = ..., document_type: _Optional[_Union[DocumentType, _Mapping]] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class DocumentTypeUpdateResponse(_message.Message):
    __slots__ = ["document_type", "response_standard"]
    DOCUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    document_type: DocumentType
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ..., document_type: _Optional[_Union[DocumentType, _Mapping]] = ...) -> None: ...