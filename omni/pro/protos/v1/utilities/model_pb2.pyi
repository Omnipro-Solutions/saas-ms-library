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

class Model(_message.Message):
    __slots__ = [
        "id",
        "microservice",
        "persistence_type",
        "name",
        "code",
        "class_name",
        "hash_code",
        "fields",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    MICROSERVICE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    HASH_CODE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    microservice: str
    persistence_type: str
    name: str
    code: str
    class_name: str
    hash_code: str
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        microservice: _Optional[str] = ...,
        persistence_type: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        class_name: _Optional[str] = ...,
        hash_code: _Optional[str] = ...,
        fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class Field(_message.Message):
    __slots__ = ["name", "type", "description", "code", "size", "required", "relation", "widget", "view", "options"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    description: str
    code: str
    size: int
    required: _wrappers_pb2.BoolValue
    relation: _struct_pb2.Struct
    widget: str
    view: str
    options: _struct_pb2.ListValue
    def __init__(
        self,
        name: _Optional[str] = ...,
        type: _Optional[str] = ...,
        description: _Optional[str] = ...,
        code: _Optional[str] = ...,
        size: _Optional[int] = ...,
        required: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        relation: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        widget: _Optional[str] = ...,
        view: _Optional[str] = ...,
        options: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
    ) -> None: ...

class ModelCreateRequest(_message.Message):
    __slots__ = ["microservice", "persistence_type", "name", "code", "class_name", "hash_code", "fields", "context"]
    MICROSERVICE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    HASH_CODE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    microservice: str
    persistence_type: str
    name: str
    code: str
    class_name: str
    hash_code: str
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    context: _base_pb2.Context
    def __init__(
        self,
        microservice: _Optional[str] = ...,
        persistence_type: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        class_name: _Optional[str] = ...,
        hash_code: _Optional[str] = ...,
        fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ModelCreateResponse(_message.Message):
    __slots__ = ["response_standard", "model"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    model: Model
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        model: _Optional[_Union[Model, _Mapping]] = ...,
    ) -> None: ...

class ModelReadRequest(_message.Message):
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

class ModelReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "models"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    models: _containers.RepeatedCompositeFieldContainer[Model]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ...,
    ) -> None: ...

class ModelUpdateRequest(_message.Message):
    __slots__ = ["model", "context"]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model: Model
    context: _base_pb2.Context
    def __init__(
        self,
        model: _Optional[_Union[Model, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ModelUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "model"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    model: Model
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        model: _Optional[_Union[Model, _Mapping]] = ...,
    ) -> None: ...

class ModelDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ModelDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
