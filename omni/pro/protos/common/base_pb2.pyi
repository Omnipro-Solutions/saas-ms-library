from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class Object(_message.Message):
    __slots__ = ["code_name", "code"]
    CODE_NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code_name: str
    code: str
    def __init__(self, code_name: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class GroupBy(_message.Message):
    __slots__ = ["name_field"]
    NAME_FIELD_FIELD_NUMBER: _ClassVar[int]
    name_field: str
    def __init__(self, name_field: _Optional[str] = ...) -> None: ...

class SortBy(_message.Message):
    __slots__ = ["name_field", "type"]

    class SortType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ASC: _ClassVar[SortBy.SortType]
        DESC: _ClassVar[SortBy.SortType]
    ASC: SortBy.SortType
    DESC: SortBy.SortType
    NAME_FIELD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name_field: str
    type: SortBy.SortType
    def __init__(
        self, name_field: _Optional[str] = ..., type: _Optional[_Union[SortBy.SortType, str]] = ...
    ) -> None: ...

class Fields(_message.Message):
    __slots__ = ["name_field"]
    NAME_FIELD_FIELD_NUMBER: _ClassVar[int]
    name_field: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name_field: _Optional[_Iterable[str]] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ["filter"]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: str
    def __init__(self, filter: _Optional[str] = ...) -> None: ...

class Paginated(_message.Message):
    __slots__ = ["offset", "limit"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    offset: int
    limit: int
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class LinkPage(_message.Message):
    __slots__ = ["type", "link"]

    class LinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        NEXT: _ClassVar[LinkPage.LinkType]
        PREV: _ClassVar[LinkPage.LinkType]
        LAST: _ClassVar[LinkPage.LinkType]
        FIRST: _ClassVar[LinkPage.LinkType]
    NEXT: LinkPage.LinkType
    PREV: LinkPage.LinkType
    LAST: LinkPage.LinkType
    FIRST: LinkPage.LinkType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    type: LinkPage.LinkType
    link: str
    def __init__(self, type: _Optional[_Union[LinkPage.LinkType, str]] = ..., link: _Optional[str] = ...) -> None: ...

class MetaData(_message.Message):
    __slots__ = ["total", "offset", "limit", "count", "link_page"]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    LINK_PAGE_FIELD_NUMBER: _ClassVar[int]
    total: int
    offset: int
    limit: int
    count: int
    link_page: _containers.RepeatedCompositeFieldContainer[LinkPage]
    def __init__(
        self,
        total: _Optional[int] = ...,
        offset: _Optional[int] = ...,
        limit: _Optional[int] = ...,
        count: _Optional[int] = ...,
        link_page: _Optional[_Iterable[_Union[LinkPage, _Mapping]]] = ...,
    ) -> None: ...

class ResponseStandard(_message.Message):
    __slots__ = ["success", "message", "status_code", "message_code"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    status_code: int
    message_code: str
    def __init__(
        self,
        success: bool = ...,
        message: _Optional[str] = ...,
        status_code: _Optional[int] = ...,
        message_code: _Optional[str] = ...,
    ) -> None: ...

class ObjectAudit(_message.Message):
    __slots__ = ["created_by", "updated_by", "deleted_by", "created_at", "updated_at", "deleted_at"]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    created_by: str
    updated_by: str
    deleted_by: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        created_by: _Optional[str] = ...,
        updated_by: _Optional[str] = ...,
        deleted_by: _Optional[str] = ...,
        created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
    ) -> None: ...

class Context(_message.Message):
    __slots__ = ["tenant", "user"]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    tenant: str
    user: str
    def __init__(self, tenant: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...

class ObjectResponse(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
