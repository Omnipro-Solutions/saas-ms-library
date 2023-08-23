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

class ValidateDeliveryCoverageRequest(_message.Message):
    __slots__ = [
        "card_id",
        "is_checkout",
        "store",
        "shipping_rule",
        "shipping_dicount",
        "subtotal",
        "shipping_address",
        "lines",
        "deliveries",
    ]
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    IS_CHECKOUT_FIELD_NUMBER: _ClassVar[int]
    STORE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_RULE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_DICOUNT_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    DELIVERIES_FIELD_NUMBER: _ClassVar[int]
    card_id: int
    is_checkout: _wrappers_pb2.BoolValue
    store: str
    shipping_rule: int
    shipping_dicount: int
    subtotal: int
    shipping_address: _struct_pb2.Struct
    lines: _struct_pb2.ListValue
    deliveries: _struct_pb2.ListValue
    def __init__(
        self,
        card_id: _Optional[int] = ...,
        is_checkout: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        store: _Optional[str] = ...,
        shipping_rule: _Optional[int] = ...,
        shipping_dicount: _Optional[int] = ...,
        subtotal: _Optional[int] = ...,
        shipping_address: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        lines: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
        deliveries: _Optional[_Union[_struct_pb2.ListValue, _Mapping]] = ...,
    ) -> None: ...

class ValidateDeliveryCoverageResponse(_message.Message):
    __slots__ = ["is_valid", "response_standard"]
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    is_valid: _wrappers_pb2.BoolValue
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        is_valid: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...
