from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["active", "id", "name", "object_audit", "user_doc_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    USER_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    user_doc_id: str
    def __init__(
        self,
        id: _Optional[int] = ...,
        user_doc_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class UserCreateRequest(_message.Message):
    __slots__ = ["context", "name", "user_doc_id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    name: str
    user_doc_id: str
    def __init__(
        self,
        user_doc_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class UserCreateResponse(_message.Message):
    __slots__ = ["response_standard", "user"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    user: User
    def __init__(
        self,
        user: _Optional[_Union[User, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class UserDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class UserDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class UserReadRequest(_message.Message):
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

class UserReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "user"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    user: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(
        self,
        user: _Optional[_Iterable[_Union[User, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class UserUpdateRequest(_message.Message):
    __slots__ = ["context", "user"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    user: User
    def __init__(
        self,
        user: _Optional[_Union[User, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class UserUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "user"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    user: User
    def __init__(
        self,
        user: _Optional[_Union[User, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...