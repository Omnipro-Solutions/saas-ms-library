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

class DeliveryLocalityMatrixValues(_message.Message):
    __slots__ = ["active", "delivery_locality_id", "id", "object_audit", "territory_matrix_values_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCALITY_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_VALUES_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    delivery_locality_id: int
    id: int
    object_audit: _base_pb2.ObjectAudit
    territory_matrix_values_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        delivery_locality_id: _Optional[int] = ...,
        territory_matrix_values_id: _Optional[int] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityMatrixValuesCreateRequest(_message.Message):
    __slots__ = ["context", "delivery_locality_id", "territory_matrix_values_id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCALITY_ID_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_VALUES_ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_locality_id: int
    territory_matrix_values_id: int
    def __init__(
        self,
        delivery_locality_id: _Optional[int] = ...,
        territory_matrix_values_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityMatrixValuesCreateResponse(_message.Message):
    __slots__ = ["delivery_locality_matrix_values", "response_standard"]
    DELIVERY_LOCALITY_MATRIX_VALUES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_locality_matrix_values: DeliveryLocalityMatrixValues
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_locality_matrix_values: _Optional[_Union[DeliveryLocalityMatrixValues, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityMatrixValuesDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryLocalityMatrixValuesDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryLocalityMatrixValuesReadRequest(_message.Message):
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

class DeliveryLocalityMatrixValuesReadResponse(_message.Message):
    __slots__ = ["delivery_locality_matrix_valuess", "meta_data", "response_standard"]
    DELIVERY_LOCALITY_MATRIX_VALUESS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_locality_matrix_valuess: _containers.RepeatedCompositeFieldContainer[DeliveryLocalityMatrixValues]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_locality_matrix_valuess: _Optional[_Iterable[_Union[DeliveryLocalityMatrixValues, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityMatrixValuesUpdateRequest(_message.Message):
    __slots__ = ["context", "delivery_locality_matrix_values"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCALITY_MATRIX_VALUES_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_locality_matrix_values: DeliveryLocalityMatrixValues
    def __init__(
        self,
        delivery_locality_matrix_values: _Optional[_Union[DeliveryLocalityMatrixValues, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityMatrixValuesUpdateResponse(_message.Message):
    __slots__ = ["delivery_locality_matrix_values", "response_standard"]
    DELIVERY_LOCALITY_MATRIX_VALUES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_locality_matrix_values: DeliveryLocalityMatrixValues
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_locality_matrix_values: _Optional[_Union[DeliveryLocalityMatrixValues, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
