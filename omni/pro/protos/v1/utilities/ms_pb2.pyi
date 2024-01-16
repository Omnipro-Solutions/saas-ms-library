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

class Microservice(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "sumary",
        "description",
        "author",
        "category",
        "version",
        "depends",
        "data",
        "load_data",
        "settings",
        "active",
        "external_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUMARY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPENDS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOAD_DATA_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    sumary: str
    description: str
    author: str
    category: str
    version: str
    depends: _containers.RepeatedScalarFieldContainer[str]
    data: _struct_pb2.ListValue
    load_data: _wrappers_pb2.BoolValue
    settings: _struct_pb2.ListValue
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        sumary: _Optional[str] = ...,
        description: _Optional[str] = ...,
        author: _Optional[str] = ...,
        category: _Optional[str] = ...,
        version: _Optional[str] = ...,
        depends: _Optional[_Iterable[str]] = ...,
        data: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        load_data: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        settings: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class MicroserviceCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "code",
        "sumary",
        "description",
        "author",
        "category",
        "version",
        "depends",
        "data",
        "load_data",
        "settings",
        "external_id",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUMARY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPENDS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LOAD_DATA_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    sumary: str
    description: str
    author: str
    category: str
    version: str
    depends: _containers.RepeatedScalarFieldContainer[str]
    data: _struct_pb2.ListValue
    load_data: _wrappers_pb2.BoolValue
    settings: _struct_pb2.ListValue
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        sumary: _Optional[str] = ...,
        description: _Optional[str] = ...,
        author: _Optional[str] = ...,
        category: _Optional[str] = ...,
        version: _Optional[str] = ...,
        depends: _Optional[_Iterable[str]] = ...,
        data: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        load_data: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        settings: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class MicroserviceCreateResponse(_message.Message):
    __slots__ = ["response_standard", "microservice"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    MICROSERVICE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    microservice: Microservice
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        microservice: _Optional[_Union[Microservice, _Mapping]] = ...,
    ) -> None: ...

class MicroserviceReadRequest(_message.Message):
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

class MicroserviceReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "microservices"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    MICROSERVICES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    microservices: _containers.RepeatedCompositeFieldContainer[Microservice]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        microservices: _Optional[_Iterable[_Union[Microservice, _Mapping]]] = ...,
    ) -> None: ...

class MicroserviceUpdateRequest(_message.Message):
    __slots__ = ["microservice", "context"]
    MICROSERVICE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    microservice: Microservice
    context: _base_pb2.Context
    def __init__(
        self,
        microservice: _Optional[_Union[Microservice, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class MicroserviceUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "microservice"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    MICROSERVICE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    microservice: Microservice
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        microservice: _Optional[_Union[Microservice, _Mapping]] = ...,
    ) -> None: ...

class MicroserviceDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class MicroserviceDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
