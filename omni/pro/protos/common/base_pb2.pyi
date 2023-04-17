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

class Context(_message.Message):
    __slots__ = ["tenant", "user"]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    tenant: str
    user: str
    def __init__(self, tenant: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...

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

class GroupBy(_message.Message):
    __slots__ = ["name_field"]
    NAME_FIELD_FIELD_NUMBER: _ClassVar[int]
    name_field: str
    def __init__(self, name_field: _Optional[str] = ...) -> None: ...

class LinkPage(_message.Message):
    __slots__ = ["link", "type"]

    class LinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    FIRST: LinkPage.LinkType
    LAST: LinkPage.LinkType
    LINK_FIELD_NUMBER: _ClassVar[int]
    NEXT: LinkPage.LinkType
    PREV: LinkPage.LinkType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    link: str
    type: LinkPage.LinkType
    def __init__(self, type: _Optional[_Union[LinkPage.LinkType, str]] = ..., link: _Optional[str] = ...) -> None: ...

class MetaData(_message.Message):
    __slots__ = ["count", "limit", "link_page", "offset", "total"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LINK_PAGE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    count: int
    limit: int
    link_page: _containers.RepeatedCompositeFieldContainer[LinkPage]
    offset: int
    total: int
    def __init__(
        self,
        total: _Optional[int] = ...,
        offset: _Optional[int] = ...,
        limit: _Optional[int] = ...,
        count: _Optional[int] = ...,
        link_page: _Optional[_Iterable[_Union[LinkPage, _Mapping]]] = ...,
    ) -> None: ...

class Object(_message.Message):
    __slots__ = ["code", "name"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    def __init__(self, name: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class ObjectAudit(_message.Message):
    __slots__ = ["created_at", "created_by", "deleted_at", "deleted_by", "updated_at", "updated_by"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    deleted_at: _timestamp_pb2.Timestamp
    deleted_by: str
    updated_at: _timestamp_pb2.Timestamp
    updated_by: str
    def __init__(
        self,
        created_by: _Optional[str] = ...,
        updated_by: _Optional[str] = ...,
        deleted_by: _Optional[str] = ...,
        created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
    ) -> None: ...

class Paginated(_message.Message):
    __slots__ = ["limit", "offset"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ResponseStandard(_message.Message):
    __slots__ = ["message", "status_code", "success"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status_code: int
    success: bool
    def __init__(
        self, success: bool = ..., message: _Optional[str] = ..., status_code: _Optional[int] = ...
    ) -> None: ...

class SortBy(_message.Message):
    __slots__ = ["name_field", "type"]

    class SortType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ASC: SortBy.SortType
    DESC: SortBy.SortType
    NAME_FIELD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name_field: str
    type: SortBy.SortType
    def __init__(
        self, name_field: _Optional[str] = ..., type: _Optional[_Union[SortBy.SortType, str]] = ...
    ) -> None: ...
