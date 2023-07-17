from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.rules import delivery_category_pb2 as _delivery_category_pb2
from omni.pro.protos.v1.rules import delivery_locality_pb2 as _delivery_locality_pb2
from omni.pro.protos.v1.rules import delivery_method_warehouse_pb2 as _delivery_method_warehouse_pb2
from omni.pro.protos.v1.rules import delivery_schedule_pb2 as _delivery_schedule_pb2
from omni.pro.protos.v1.rules import location_pb2 as _location_pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as _warehouse_pb2

CONSOLIDATED: TypePickingTransfer
DESCRIPTOR: _descriptor.FileDescriptor
OPTIONAL: ValidateWarehouseCode
PARTIAL: TypePickingTransfer
REQUIRED: ValidateWarehouseCode
SHIPPING: TypeDelivery
STORE: TypeDelivery
UNNECESSARY: ValidateWarehouseCode

class DeliveryMethod(_message.Message):
    __slots__ = [
        "active",
        "category_template_id",
        "code",
        "delivery_location_id",
        "delivery_warehouse_ids",
        "id",
        "locality_available_id",
        "name",
        "object_audit",
        "quantity_security",
        "schedule_template_id",
        "transfer_template_id",
        "type_delivery",
        "type_picking_transfer",
        "validate_warehouse_code",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SECURITY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    TYPE_PICKING_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_WAREHOUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    category_template_id: _delivery_category_pb2.DeliveryCategory
    code: str
    delivery_location_id: _location_pb2.Location
    delivery_warehouse_ids: _containers.RepeatedCompositeFieldContainer[_warehouse_pb2.Warehouse]
    id: str
    locality_available_id: _delivery_locality_pb2.DeliveryLocality
    name: str
    object_audit: _base_pb2.ObjectAudit
    quantity_security: float
    schedule_template_id: _delivery_schedule_pb2.DeliverySchedule
    transfer_template_id: _delivery_method_warehouse_pb2.DeliveryMethodWarehouse
    type_delivery: TypeDelivery
    type_picking_transfer: TypePickingTransfer
    validate_warehouse_code: ValidateWarehouseCode
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        delivery_warehouse_ids: _Optional[_Iterable[_Union[_warehouse_pb2.Warehouse, _Mapping]]] = ...,
        type_picking_transfer: _Optional[_Union[TypePickingTransfer, str]] = ...,
        validate_warehouse_code: _Optional[_Union[ValidateWarehouseCode, str]] = ...,
        quantity_security: _Optional[float] = ...,
        code: _Optional[str] = ...,
        type_delivery: _Optional[_Union[TypeDelivery, str]] = ...,
        delivery_location_id: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        transfer_template_id: _Optional[_Union[_delivery_method_warehouse_pb2.DeliveryMethodWarehouse, _Mapping]] = ...,
        category_template_id: _Optional[_Union[_delivery_category_pb2.DeliveryCategory, _Mapping]] = ...,
        locality_available_id: _Optional[_Union[_delivery_locality_pb2.DeliveryLocality, _Mapping]] = ...,
        schedule_template_id: _Optional[_Union[_delivery_schedule_pb2.DeliverySchedule, _Mapping]] = ...,
        active: bool = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodCreateRequest(_message.Message):
    __slots__ = [
        "category_template_id",
        "code",
        "context",
        "delivery_location_id",
        "delivery_warehouse_ids",
        "locality_available_id",
        "name",
        "quantity_security",
        "schedule_template_id",
        "transfer_template_id",
        "type_delivery",
        "type_picking_transfer",
        "validate_warehouse_code",
    ]
    CATEGORY_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SECURITY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    TYPE_PICKING_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_WAREHOUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    category_template_id: str
    code: str
    context: _base_pb2.Context
    delivery_location_id: str
    delivery_warehouse_ids: _containers.RepeatedScalarFieldContainer[str]
    locality_available_id: str
    name: str
    quantity_security: float
    schedule_template_id: str
    transfer_template_id: str
    type_delivery: TypeDelivery
    type_picking_transfer: TypePickingTransfer
    validate_warehouse_code: ValidateWarehouseCode
    def __init__(
        self,
        name: _Optional[str] = ...,
        delivery_warehouse_ids: _Optional[_Iterable[str]] = ...,
        type_picking_transfer: _Optional[_Union[TypePickingTransfer, str]] = ...,
        validate_warehouse_code: _Optional[_Union[ValidateWarehouseCode, str]] = ...,
        quantity_security: _Optional[float] = ...,
        code: _Optional[str] = ...,
        type_delivery: _Optional[_Union[TypeDelivery, str]] = ...,
        delivery_location_id: _Optional[str] = ...,
        transfer_template_id: _Optional[str] = ...,
        category_template_id: _Optional[str] = ...,
        locality_available_id: _Optional[str] = ...,
        schedule_template_id: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodCreateResponse(_message.Message):
    __slots__ = ["delivery_method", "response_standard"]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method: DeliveryMethod
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_method: _Optional[_Union[DeliveryMethod, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: str
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

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
    id: str
    paginated: _base_pb2.Paginated
    sort_by: _base_pb2.SortBy
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

class DeliveryMethodReadResponse(_message.Message):
    __slots__ = ["delivery_methods", "meta_data", "response_standard"]
    DELIVERY_METHODS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_methods: _containers.RepeatedCompositeFieldContainer[DeliveryMethod]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_methods: _Optional[_Iterable[_Union[DeliveryMethod, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodUpdateRequest(_message.Message):
    __slots__ = ["context", "delivery_method"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    delivery_method: DeliveryMethod
    def __init__(
        self,
        delivery_method: _Optional[_Union[DeliveryMethod, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodUpdateResponse(_message.Message):
    __slots__ = ["delivery_method", "response_standard"]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    delivery_method: DeliveryMethod
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        delivery_method: _Optional[_Union[DeliveryMethod, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class TypePickingTransfer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ValidateWarehouseCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TypeDelivery(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
