from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ComputeMethodData(_message.Message):
    __slots__ = ["cart_details", "items", "shipping_details"]
    CART_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    cart_details: _struct_pb2.Struct
    items: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    shipping_details: _struct_pb2.Struct
    def __init__(
        self,
        cart_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        items: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        shipping_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
    ) -> None: ...

class ComputeMethodRequest(_message.Message):
    __slots__ = ["version", "data", "context"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    version: int
    data: _containers.RepeatedCompositeFieldContainer[ComputeMethodData]
    context: _base_pb2.Context
    def __init__(
        self,
        version: _Optional[int] = ...,
        data: _Optional[_Iterable[_Union[ComputeMethodData, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ComputeMethodResponse(_message.Message):
    __slots__ = ["result", "response_standard"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    result: _struct_pb2.ListValue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        result: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class ComputeMethodStockAvailableRequest(_message.Message):
    __slots__ = ["methods", "items", "context"]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    methods: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    items: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    context: _base_pb2.Context
    def __init__(
        self,
        methods: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        items: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ComputeMethodStockAvailableResponse(_message.Message):
    __slots__ = ["result", "response_standard"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    result: _struct_pb2.ListValue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        result: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
