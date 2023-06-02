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

class DeliveryLocality(_message.Message):
    __slots__ = ["active", "country_id", "id", "name", "object_audit", "territory_matrix_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    country_id: int
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    territory_matrix_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        country_id: _Optional[int] = ...,
        territory_matrix_id: _Optional[int] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityCreateRequest(_message.Message):
    __slots__ = ["context", "country_id", "name", "territory_matrix_id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    country_id: int
    name: str
    territory_matrix_id: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        country_id: _Optional[int] = ...,
        territory_matrix_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityCreateResponse(_message.Message):
    __slots__ = ["delivery_locality", "response_standard"]
    DELIVERY_LOCALITY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_locality: DeliveryLocality
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_locality: _Optional[_Union[DeliveryLocality, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryLocalityDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryLocalityReadRequest(_message.Message):
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

class DeliveryLocalityReadResponse(_message.Message):
    __slots__ = ["delivery_localities", "meta_data", "response_standard"]
    DELIVERY_LOCALITIES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_localities: _containers.RepeatedCompositeFieldContainer[DeliveryLocality]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_localities: _Optional[_Iterable[_Union[DeliveryLocality, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityUpdateRequest(_message.Message):
    __slots__ = ["context", "delivery_locality"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCALITY_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_locality: DeliveryLocality
    def __init__(
        self,
        delivery_locality: _Optional[_Union[DeliveryLocality, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryLocalityUpdateResponse(_message.Message):
    __slots__ = ["delivery_locality", "response_standard"]
    DELIVERY_LOCALITY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_locality: DeliveryLocality
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_locality: _Optional[_Union[DeliveryLocality, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
