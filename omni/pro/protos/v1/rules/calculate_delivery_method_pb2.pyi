from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CalculateDeliveryMethodRequest(_message.Message):
    __slots__ = ["cart_details", "items", "shipping_details"]
    CART_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    cart_details: _struct_pb2.Struct
    items: _struct_pb2.Struct
    shipping_details: _struct_pb2.Struct
    def __init__(
        self,
        cart_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        items: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        shipping_details: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
    ) -> None: ...

class CalculateDeliveryMethodResponse(_message.Message):
    __slots__ = ["deliveries", "response_standard"]
    DELIVERIES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    deliveries: _struct_pb2.ListValue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        deliveries: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
