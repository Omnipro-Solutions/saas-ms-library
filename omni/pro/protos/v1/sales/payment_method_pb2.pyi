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

class PaymentMethod(_message.Message):
    __slots__ = ["active", "code", "id", "name", "object_audit", "payment_method_doc_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    active: bool
    code: str
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    payment_method_doc_id: str
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        payment_method_doc_id: _Optional[str] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class PaymentMethodCreateRequest(_message.Message):
    __slots__ = ["code", "context", "name", "payment_method_doc_id"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    name: str
    payment_method_doc_id: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        payment_method_doc_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PaymentMethodCreateResponse(_message.Message):
    __slots__ = ["payment_method", "response_standard"]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class PaymentMethodDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class PaymentMethodDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class PaymentMethodReadRequest(_message.Message):
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

class PaymentMethodReadResponse(_message.Message):
    __slots__ = ["meta_data", "payment_methods", "response_standard"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    payment_methods: _containers.RepeatedCompositeFieldContainer[PaymentMethod]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        payment_methods: _Optional[_Iterable[_Union[PaymentMethod, _Mapping]]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
    ) -> None: ...

class PaymentMethodUpdateRequest(_message.Message):
    __slots__ = ["context", "payment_method"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    payment_method: PaymentMethod
    def __init__(
        self,
        payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PaymentMethodUpdateResponse(_message.Message):
    __slots__ = ["payment_method", "response_standard"]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...