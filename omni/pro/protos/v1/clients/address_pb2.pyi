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

class Address(_message.Message):
    __slots__ = [
        "active",
        "code",
        "country_id",
        "lat",
        "lng",
        "name",
        "object_audit",
        "street",
        "street2",
        "territory_matrixes",
        "type_address",
        "zip_code",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    STREET2_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_FIELD_NUMBER: _ClassVar[int]
    TYPE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    code: str
    country_id: str
    lat: str
    lng: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    street: str
    street2: str
    territory_matrixes: _containers.RepeatedCompositeFieldContainer[TerritoryMatrix]
    type_address: str
    zip_code: str
    def __init__(
        self,
        country_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        type_address: _Optional[str] = ...,
        street: _Optional[str] = ...,
        street2: _Optional[str] = ...,
        lat: _Optional[str] = ...,
        lng: _Optional[str] = ...,
        zip_code: _Optional[str] = ...,
        territory_matrixes: _Optional[_Iterable[_Union[TerritoryMatrix, _Mapping]]] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class AddressCreateRequest(_message.Message):
    __slots__ = [
        "client_id",
        "code",
        "context",
        "country_id",
        "lat",
        "lng",
        "name",
        "street",
        "street2",
        "territory_matrixes",
        "type_address",
        "zip_code",
    ]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STREET2_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIXES_FIELD_NUMBER: _ClassVar[int]
    TYPE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    code: str
    context: _base_pb2.Context
    country_id: str
    lat: str
    lng: str
    name: str
    street: str
    street2: str
    territory_matrixes: _containers.RepeatedCompositeFieldContainer[TerritoryMatrix]
    type_address: str
    zip_code: str
    def __init__(
        self,
        client_id: _Optional[str] = ...,
        country_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        type_address: _Optional[str] = ...,
        street: _Optional[str] = ...,
        street2: _Optional[str] = ...,
        lat: _Optional[str] = ...,
        lng: _Optional[str] = ...,
        zip_code: _Optional[str] = ...,
        territory_matrixes: _Optional[_Iterable[_Union[TerritoryMatrix, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddressCreateResponse(_message.Message):
    __slots__ = ["address", "response_standard"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    address: Address
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        address: _Optional[_Union[Address, _Mapping]] = ...,
    ) -> None: ...

class AddressDeleteRequest(_message.Message):
    __slots__ = ["client_id", "code", "context"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    code: str
    context: _base_pb2.Context
    def __init__(
        self,
        client_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddressDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class AddressUpdateRequest(_message.Message):
    __slots__ = ["address", "client_id", "context"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    address: Address
    client_id: str
    context: _base_pb2.Context
    def __init__(
        self,
        client_id: _Optional[str] = ...,
        address: _Optional[_Union[Address, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddressUpdateResponse(_message.Message):
    __slots__ = ["address", "response_standard"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    address: Address
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        address: _Optional[_Union[Address, _Mapping]] = ...,
    ) -> None: ...

class TerritoryMatrix(_message.Message):
    __slots__ = ["code", "name", "sequence"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    sequence: int
    def __init__(
        self, name: _Optional[str] = ..., code: _Optional[str] = ..., sequence: _Optional[int] = ...
    ) -> None: ...
