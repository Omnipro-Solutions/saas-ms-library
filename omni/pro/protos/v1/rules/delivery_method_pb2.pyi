from common import base_pb2 as _base_pb2
from v1.rules import warehouse_pb2 as _warehouse_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CONSOLIDATED: TypePickingTransfer
DESCRIPTOR: _descriptor.FileDescriptor
OPTIONAL: ValidateWarehouseCode
PARTIAL: TypePickingTransfer
REQUIRED: ValidateWarehouseCode
SHIPPING: TypeDelivery
STORE: TypeDelivery
UNNECESSARY: ValidateWarehouseCode

class DeliveryMethod(_message.Message):
    __slots__ = ["active", "category_template_id", "code", "delivery_location_id", "delivery_warehouse_ids", "id", "local_available_id", "name", "object_audit", "quantity_sequrity", "schedule_template_id", "transfer_template_id", "type_delivery", "type_picking_transfer", "validate_warehouse_code"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SEQURITY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    TYPE_PICKING_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_WAREHOUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    category_template_id: int
    code: str
    delivery_location_id: int
    delivery_warehouse_ids: _containers.RepeatedCompositeFieldContainer[_warehouse_pb2.Warehouse]
    id: int
    local_available_id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    quantity_sequrity: float
    schedule_template_id: int
    transfer_template_id: int
    type_delivery: TypeDelivery
    type_picking_transfer: TypePickingTransfer
    validate_warehouse_code: ValidateWarehouseCode
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., delivery_warehouse_ids: _Optional[_Iterable[_Union[_warehouse_pb2.Warehouse, _Mapping]]] = ..., type_picking_transfer: _Optional[_Union[TypePickingTransfer, str]] = ..., validate_warehouse_code: _Optional[_Union[ValidateWarehouseCode, str]] = ..., quantity_sequrity: _Optional[float] = ..., code: _Optional[str] = ..., type_delivery: _Optional[_Union[TypeDelivery, str]] = ..., delivery_location_id: _Optional[int] = ..., transfer_template_id: _Optional[int] = ..., category_template_id: _Optional[int] = ..., local_available_id: _Optional[int] = ..., schedule_template_id: _Optional[int] = ..., active: bool = ..., object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...) -> None: ...

class DeliveryMethodCreateRequest(_message.Message):
    __slots__ = ["category_template_id", "code", "context", "delivery_location_id", "local_available_id", "name", "quantity_sequrity", "schedule_template_id", "transfer_template_id", "type_delivery", "type_picking_transfer", "validate_warehouse_code"]
    CATEGORY_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SEQURITY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    TYPE_PICKING_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_WAREHOUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    category_template_id: int
    code: str
    context: _base_pb2.Context
    delivery_location_id: int
    local_available_id: int
    name: str
    quantity_sequrity: float
    schedule_template_id: int
    transfer_template_id: int
    type_delivery: TypeDelivery
    type_picking_transfer: TypePickingTransfer
    validate_warehouse_code: ValidateWarehouseCode
    def __init__(self, name: _Optional[str] = ..., type_picking_transfer: _Optional[_Union[TypePickingTransfer, str]] = ..., validate_warehouse_code: _Optional[_Union[ValidateWarehouseCode, str]] = ..., quantity_sequrity: _Optional[float] = ..., code: _Optional[str] = ..., type_delivery: _Optional[_Union[TypeDelivery, str]] = ..., delivery_location_id: _Optional[int] = ..., transfer_template_id: _Optional[int] = ..., category_template_id: _Optional[int] = ..., local_available_id: _Optional[int] = ..., schedule_template_id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class DeliveryMethodCreateResponse(_message.Message):
    __slots__ = ["delivery_method", "response_standard"]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method: DeliveryMethod
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, delivery_method: _Optional[_Union[DeliveryMethod, _Mapping]] = ..., response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryMethodDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class DeliveryMethodDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryMethodReadRequest(_message.Message):
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
    def __init__(self, group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ..., sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ..., fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ..., filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ..., paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ..., id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class DeliveryMethodReadResponse(_message.Message):
    __slots__ = ["delivery_methods", "meta_data", "response_standard"]
    DELIVERY_METHODS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_methods: _containers.RepeatedCompositeFieldContainer[DeliveryMethod]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, delivery_methods: _Optional[_Iterable[_Union[DeliveryMethod, _Mapping]]] = ..., meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ..., response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class DeliveryMethodUpdateRequest(_message.Message):
    __slots__ = ["context", "delivery_method"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_method: DeliveryMethod
    def __init__(self, delivery_method: _Optional[_Union[DeliveryMethod, _Mapping]] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...) -> None: ...

class DeliveryMethodUpdateResponse(_message.Message):
    __slots__ = ["delivery_method", "response_standard"]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method: DeliveryMethod
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, delivery_method: _Optional[_Union[DeliveryMethod, _Mapping]] = ..., response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class TypePickingTransfer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ValidateWarehouseCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TypeDelivery(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
