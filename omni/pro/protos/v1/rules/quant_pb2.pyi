from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Quant(_message.Message):
    __slots__ = [
        "id",
        "product_doc_id",
        "location_sql_id",
        "quant_sql_id",
        "available_quantity",
        "active",
        "external_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    QUANT_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    product_doc_id: str
    location_sql_id: int
    quant_sql_id: int
    available_quantity: float
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        product_doc_id: _Optional[str] = ...,
        location_sql_id: _Optional[int] = ...,
        quant_sql_id: _Optional[int] = ...,
        available_quantity: _Optional[float] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class QuantCreateRequest(_message.Message):
    __slots__ = ["product_doc_id", "location_sql_id", "quant_sql_id", "available_quantity", "external_id", "context"]
    PRODUCT_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    QUANT_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    product_doc_id: str
    location_sql_id: int
    quant_sql_id: int
    available_quantity: float
    external_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        product_doc_id: _Optional[str] = ...,
        location_sql_id: _Optional[int] = ...,
        quant_sql_id: _Optional[int] = ...,
        available_quantity: _Optional[float] = ...,
        external_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class QuantCreateResponse(_message.Message):
    __slots__ = ["quant", "response_standard"]
    QUANT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    quant: Quant
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        quant: _Optional[_Union[Quant, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class QuantReadRequest(_message.Message):
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

class QuantReadResponse(_message.Message):
    __slots__ = ["quants", "meta_data", "response_standard"]
    QUANTS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    quants: _containers.RepeatedCompositeFieldContainer[Quant]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        quants: _Optional[_Iterable[_Union[Quant, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class QuantUpdateRequest(_message.Message):
    __slots__ = ["quant", "context"]
    QUANT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    quant: Quant
    context: _base_pb2.Context
    def __init__(
        self,
        quant: _Optional[_Union[Quant, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class QuantUpdateResponse(_message.Message):
    __slots__ = ["quant", "response_standard"]
    QUANT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    quant: Quant
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        quant: _Optional[_Union[Quant, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class QuantDeleteRequest(_message.Message):
    __slots__ = ["quant_sql_id", "context"]
    QUANT_SQL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    quant_sql_id: int
    context: _base_pb2.Context
    def __init__(
        self, quant_sql_id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class QuantDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
