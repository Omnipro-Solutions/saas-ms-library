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
from omni.pro.protos.v1.rules import delivery_category_pb2 as _delivery_category_pb2
from omni.pro.protos.v1.rules import delivery_locality_pb2 as _delivery_locality_pb2
from omni.pro.protos.v1.rules import delivery_schedule_pb2 as _delivery_schedule_pb2
from omni.pro.protos.v1.rules import delivery_warehouse_pb2 as _delivery_warehouse_pb2
from omni.pro.protos.v1.rules import location_pb2 as _location_pb2
from omni.pro.protos.v1.rules import stock_security_product_pb2 as _stock_security_product_pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryMethod(_message.Message):
    __slots__ = [
        "id",
        "name",
        "delivery_warehouses",
        "type_picking_transfer",
        "validate_warehouse_code",
        "quantity_security",
        "code",
        "type_delivery",
        "delivery_location",
        "transfer_template",
        "category_template",
        "locality_available",
        "schedule_template",
        "stock_security_product",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_WAREHOUSES_FIELD_NUMBER: _ClassVar[int]
    TYPE_PICKING_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_WAREHOUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SECURITY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    STOCK_SECURITY_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    delivery_warehouses: _containers.RepeatedCompositeFieldContainer[_warehouse_pb2.Warehouse]
    type_picking_transfer: str
    validate_warehouse_code: str
    quantity_security: float
    code: str
    type_delivery: str
    delivery_location: _location_pb2.Location
    transfer_template: _delivery_warehouse_pb2.DeliveryWarehouse
    category_template: _delivery_category_pb2.DeliveryCategory
    locality_available: _delivery_locality_pb2.DeliveryLocality
    schedule_template: _delivery_schedule_pb2.DeliverySchedule
    stock_security_product: _stock_security_product_pb2.StockSecurityProduct
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        delivery_warehouses: _Optional[_Iterable[_Union[_warehouse_pb2.Warehouse, _Mapping]]] = ...,
        type_picking_transfer: _Optional[str] = ...,
        validate_warehouse_code: _Optional[str] = ...,
        quantity_security: _Optional[float] = ...,
        code: _Optional[str] = ...,
        type_delivery: _Optional[str] = ...,
        delivery_location: _Optional[_Union[_location_pb2.Location, _Mapping]] = ...,
        transfer_template: _Optional[_Union[_delivery_warehouse_pb2.DeliveryWarehouse, _Mapping]] = ...,
        category_template: _Optional[_Union[_delivery_category_pb2.DeliveryCategory, _Mapping]] = ...,
        locality_available: _Optional[_Union[_delivery_locality_pb2.DeliveryLocality, _Mapping]] = ...,
        schedule_template: _Optional[_Union[_delivery_schedule_pb2.DeliverySchedule, _Mapping]] = ...,
        stock_security_product: _Optional[_Union[_stock_security_product_pb2.StockSecurityProduct, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class DeliveryMethodCreateRequest(_message.Message):
    __slots__ = [
        "name",
        "type_picking_transfer",
        "validate_warehouse_code",
        "quantity_security",
        "code",
        "type_delivery",
        "delivery_location_id",
        "transfer_template_id",
        "category_template_id",
        "locality_available_id",
        "schedule_template_id",
        "stock_security_product_id",
        "delivery_warehouse_ids",
        "context",
    ]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_PICKING_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_WAREHOUSE_CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_SECURITY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALITY_AVAILABLE_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    STOCK_SECURITY_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    type_picking_transfer: str
    validate_warehouse_code: str
    quantity_security: float
    code: str
    type_delivery: str
    delivery_location_id: int
    transfer_template_id: str
    category_template_id: str
    locality_available_id: str
    schedule_template_id: str
    stock_security_product_id: str
    delivery_warehouse_ids: _containers.RepeatedScalarFieldContainer[int]
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        type_picking_transfer: _Optional[str] = ...,
        validate_warehouse_code: _Optional[str] = ...,
        quantity_security: _Optional[float] = ...,
        code: _Optional[str] = ...,
        type_delivery: _Optional[str] = ...,
        delivery_location_id: _Optional[int] = ...,
        transfer_template_id: _Optional[str] = ...,
        category_template_id: _Optional[str] = ...,
        locality_available_id: _Optional[str] = ...,
        schedule_template_id: _Optional[str] = ...,
        stock_security_product_id: _Optional[str] = ...,
        delivery_warehouse_ids: _Optional[_Iterable[int]] = ...,
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

class DeliveryMethodReadRequest(_message.Message):
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
    __slots__ = ["delivery_method", "context"]
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_method: DeliveryMethod
    context: _base_pb2.Context
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

class DeliveryMethodDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class DeliveryMethodDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class AddDeliveryWarehouseRequest(_message.Message):
    __slots__ = ["delivery_method_id", "delivery_warehouse_ids", "context"]
    DELIVERY_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_method_id: str
    delivery_warehouse_ids: _containers.RepeatedScalarFieldContainer[int]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_method_id: _Optional[str] = ...,
        delivery_warehouse_ids: _Optional[_Iterable[int]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AddDeliveryWarehouseResponse(_message.Message):
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

class RemoveDeliveryWarehouseRequest(_message.Message):
    __slots__ = ["delivery_method_id", "delivery_warehouse_ids", "context"]
    DELIVERY_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_WAREHOUSE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    delivery_method_id: str
    delivery_warehouse_ids: _containers.RepeatedScalarFieldContainer[int]
    context: _base_pb2.Context
    def __init__(
        self,
        delivery_method_id: _Optional[str] = ...,
        delivery_warehouse_ids: _Optional[_Iterable[int]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RemoveDeliveryWarehouseResponse(_message.Message):
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
