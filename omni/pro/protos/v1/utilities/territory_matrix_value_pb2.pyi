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

class TerritoryMatrixValue(_message.Message):
    __slots__ = ["id", "territory_matrixes", "data", "active", "object_audit"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    territory_matrixes: _struct_pb2.ListValue
    data: _struct_pb2.ListValue
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        territory_matrixes: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        data: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class TerritoryMatrixValueAddRequest(_message.Message):
    __slots__ = ["territory_matrixes", "data", "active", "context"]
    TERRITORY_MATRIXES_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    territory_matrixes: _struct_pb2.ListValue
    data: _struct_pb2.ListValue
    active: _wrappers_pb2.BoolValue
    context: _base_pb2.Context
    def __init__(
        self,
        territory_matrixes: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        data: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class TerritoryMatrixValueAddResponse(_message.Message):
    __slots__ = ["response_standard", "territory_matrix_value"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_VALUE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    territory_matrix_value: TerritoryMatrixValue
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        territory_matrix_value: _Optional[_Union[TerritoryMatrixValue, _Mapping]] = ...,
    ) -> None: ...

class TerritoryMatrixValueReadRequest(_message.Message):
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

class TerritoryMatrixValueReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "territory_matrixes_values"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_VALUES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    territory_matrixes_values: _containers.RepeatedCompositeFieldContainer[TerritoryMatrixValue]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        territory_matrixes_values: _Optional[_Iterable[_Union[TerritoryMatrixValue, _Mapping]]] = ...,
    ) -> None: ...

class TerritoryMatrixValueUpdateRequest(_message.Message):
    __slots__ = ["territory_matrix_value", "context"]
    TERRITORY_MATRIX_VALUE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    territory_matrix_value: TerritoryMatrixValue
    context: _base_pb2.Context
    def __init__(
        self,
        territory_matrix_value: _Optional[_Union[TerritoryMatrixValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class TerritoryMatrixValueUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "territory_matrix_value"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_VALUE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    territory_matrix_value: TerritoryMatrixValue
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        territory_matrix_value: _Optional[_Union[TerritoryMatrixValue, _Mapping]] = ...,
    ) -> None: ...

class TerritoryMatrixValueDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class TerritoryMatrixValueDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
