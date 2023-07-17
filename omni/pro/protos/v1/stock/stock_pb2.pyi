from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Location(_message.Message):
    __slots__ = [
        "active",
        "barcode",
        "code",
        "id",
        "name",
        "object_audit",
        "parent_id",
        "type_location",
        "warehouse_id",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    BARCODE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    barcode: str
    code: str
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    parent_id: int
    type_location: str
    warehouse_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        parent_id: _Optional[int] = ...,
        code: _Optional[str] = ...,
        type_location: _Optional[str] = ...,
        barcode: _Optional[str] = ...,
        warehouse_id: _Optional[int] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class LocationCreateRequest(_message.Message):
    __slots__ = ["active", "barcode", "code", "context", "name", "parent_id", "type_location", "warehouse_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    BARCODE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    barcode: str
    code: str
    context: _base_pb2.Context
    name: str
    parent_id: int
    type_location: str
    warehouse_id: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        parent_id: _Optional[int] = ...,
        code: _Optional[str] = ...,
        type_location: _Optional[str] = ...,
        barcode: _Optional[str] = ...,
        warehouse_id: _Optional[int] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class LocationCreateResponse(_message.Message):
    __slots__ = ["location", "response_standard"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    location: Location
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        location: _Optional[_Union[Location, _Mapping]] = ...,
    ) -> None: ...

class LocationDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class LocationDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class LocationReadRequest(_message.Message):
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

class LocationReadResponse(_message.Message):
    __slots__ = ["locations", "meta_data", "response_standard"]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    locations: _containers.RepeatedCompositeFieldContainer[Location]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        locations: _Optional[_Iterable[_Union[Location, _Mapping]]] = ...,
    ) -> None: ...

class LocationUpdateRequest(_message.Message):
    __slots__ = ["context", "location"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    location: Location
    def __init__(
        self,
        location: _Optional[_Union[Location, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class LocationUpdateResponse(_message.Message):
    __slots__ = ["location", "response_standard"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    location: Location
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        location: _Optional[_Union[Location, _Mapping]] = ...,
    ) -> None: ...

class PickingType(_message.Message):
    __slots__ = [
        "active",
        "code",
        "default_location_dest_id",
        "default_location_src_id",
        "id",
        "name",
        "number_increment",
        "number_next_actual",
        "object_audit",
        "padding",
        "prefix",
        "return_picking_type_id",
        "sequence_code",
        "show_operations",
        "show_reserved",
        "warehouse_id",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_DEST_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_SRC_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_NEXT_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    RETURN_PICKING_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_CODE_FIELD_NUMBER: _ClassVar[int]
    SHOW_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOW_RESERVED_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    code: str
    default_location_dest_id: int
    default_location_src_id: int
    id: int
    name: str
    number_increment: int
    number_next_actual: int
    object_audit: _base_pb2.ObjectAudit
    padding: int
    prefix: str
    return_picking_type_id: int
    sequence_code: str
    show_operations: _wrappers_pb2.BoolValue
    show_reserved: _wrappers_pb2.BoolValue
    warehouse_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        sequence_code: _Optional[str] = ...,
        warehouse_id: _Optional[int] = ...,
        code: _Optional[str] = ...,
        return_picking_type_id: _Optional[int] = ...,
        show_operations: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        show_reserved: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        default_location_src_id: _Optional[int] = ...,
        default_location_dest_id: _Optional[int] = ...,
        prefix: _Optional[str] = ...,
        padding: _Optional[int] = ...,
        number_increment: _Optional[int] = ...,
        number_next_actual: _Optional[int] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class PickingTypeCreateRequest(_message.Message):
    __slots__ = [
        "code",
        "context",
        "default_location_dest_id",
        "default_location_src_id",
        "name",
        "number_increment",
        "number_next_actual",
        "padding",
        "prefix",
        "return_picking_type_id",
        "sequence_code",
        "show_operations",
        "show_reserved",
        "warehouse_id",
    ]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_DEST_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_SRC_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_NEXT_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    RETURN_PICKING_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_CODE_FIELD_NUMBER: _ClassVar[int]
    SHOW_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOW_RESERVED_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    default_location_dest_id: int
    default_location_src_id: int
    name: str
    number_increment: int
    number_next_actual: int
    padding: int
    prefix: str
    return_picking_type_id: int
    sequence_code: str
    show_operations: _wrappers_pb2.BoolValue
    show_reserved: _wrappers_pb2.BoolValue
    warehouse_id: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        sequence_code: _Optional[str] = ...,
        warehouse_id: _Optional[int] = ...,
        code: _Optional[str] = ...,
        return_picking_type_id: _Optional[int] = ...,
        show_operations: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        show_reserved: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        default_location_src_id: _Optional[int] = ...,
        default_location_dest_id: _Optional[int] = ...,
        prefix: _Optional[str] = ...,
        padding: _Optional[int] = ...,
        number_increment: _Optional[int] = ...,
        number_next_actual: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingTypeCreateResponse(_message.Message):
    __slots__ = ["picking_type", "response_standard"]
    PICKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    picking_type: PickingType
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        picking_type: _Optional[_Union[PickingType, _Mapping]] = ...,
    ) -> None: ...

class PickingTypeDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class PickingTypeDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class PickingTypeReadRequest(_message.Message):
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

class PickingTypeReadResponse(_message.Message):
    __slots__ = ["meta_data", "picking_types", "response_standard"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    picking_types: _containers.RepeatedCompositeFieldContainer[PickingType]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        picking_types: _Optional[_Iterable[_Union[PickingType, _Mapping]]] = ...,
    ) -> None: ...

class PickingTypeUpdateRequest(_message.Message):
    __slots__ = ["context", "picking_type"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    picking_type: PickingType
    def __init__(
        self,
        picking_type: _Optional[_Union[PickingType, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickingTypeUpdateResponse(_message.Message):
    __slots__ = ["picking_type", "response_standard"]
    PICKING_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    picking_type: PickingType
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        picking_type: _Optional[_Union[PickingType, _Mapping]] = ...,
    ) -> None: ...

class Product(_message.Message):
    __slots__ = ["active", "id", "name", "object_audit", "product_doc_id", "template_doc_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    product_doc_id: str
    template_doc_id: str
    def __init__(
        self,
        id: _Optional[int] = ...,
        product_doc_id: _Optional[str] = ...,
        template_doc_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class ProductCreateRequest(_message.Message):
    __slots__ = ["active", "context", "name", "product_doc_id", "template_doc_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    context: _base_pb2.Context
    name: str
    product_doc_id: str
    template_doc_id: str
    def __init__(
        self,
        product_doc_id: _Optional[str] = ...,
        template_doc_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ProductCreateResponse(_message.Message):
    __slots__ = ["product", "response_standard"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    product: Product
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        product: _Optional[_Union[Product, _Mapping]] = ...,
    ) -> None: ...

class ProductDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ProductDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class ProductReadRequest(_message.Message):
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

class ProductReadResponse(_message.Message):
    __slots__ = ["meta_data", "products", "response_standard"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    products: _containers.RepeatedCompositeFieldContainer[Product]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...,
    ) -> None: ...

class ProductUpdateRequest(_message.Message):
    __slots__ = ["context", "product"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    product: Product
    def __init__(
        self,
        product: _Optional[_Union[Product, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ProductUpdateResponse(_message.Message):
    __slots__ = ["product", "response_standard"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    product: Product
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        product: _Optional[_Union[Product, _Mapping]] = ...,
    ) -> None: ...

class Quant(_message.Message):
    __slots__ = [
        "active",
        "available_quantity",
        "id",
        "location_id",
        "lote",
        "object_audit",
        "product_id",
        "quantity",
        "uom_id",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOTE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UOM_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    available_quantity: float
    id: int
    location_id: int
    lote: str
    object_audit: _base_pb2.ObjectAudit
    product_id: int
    quantity: float
    uom_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        product_id: _Optional[int] = ...,
        location_id: _Optional[int] = ...,
        lote: _Optional[str] = ...,
        available_quantity: _Optional[float] = ...,
        quantity: _Optional[float] = ...,
        uom_id: _Optional[int] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class QuantCreateRequest(_message.Message):
    __slots__ = ["available_quantity", "context", "location_id", "lote", "product_id", "quantity", "uom_id"]
    AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOTE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UOM_ID_FIELD_NUMBER: _ClassVar[int]
    available_quantity: float
    context: _base_pb2.Context
    location_id: int
    lote: str
    product_id: int
    quantity: float
    uom_id: int
    def __init__(
        self,
        product_id: _Optional[int] = ...,
        location_id: _Optional[int] = ...,
        lote: _Optional[str] = ...,
        available_quantity: _Optional[float] = ...,
        quantity: _Optional[float] = ...,
        uom_id: _Optional[int] = ...,
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
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        quant: _Optional[_Union[Quant, _Mapping]] = ...,
    ) -> None: ...

class QuantDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class QuantDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class QuantReadRequest(_message.Message):
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

class QuantReadResponse(_message.Message):
    __slots__ = ["meta_data", "quants", "response_standard"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    QUANTS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    quants: _containers.RepeatedCompositeFieldContainer[Quant]
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        quants: _Optional[_Iterable[_Union[Quant, _Mapping]]] = ...,
    ) -> None: ...

class QuantUpdateRequest(_message.Message):
    __slots__ = ["context", "quant"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    QUANT_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    quant: Quant
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
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        quant: _Optional[_Union[Quant, _Mapping]] = ...,
    ) -> None: ...

class Route(_message.Message):
    __slots__ = [
        "active",
        "id",
        "name",
        "object_audit",
        "packing_selectable",
        "product_categ_selectable",
        "product_selectable",
        "sequence",
        "warehouse_id",
        "warehouse_selectable",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PACKING_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEG_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    packing_selectable: _wrappers_pb2.BoolValue
    product_categ_selectable: _wrappers_pb2.BoolValue
    product_selectable: _wrappers_pb2.BoolValue
    sequence: int
    warehouse_id: int
    warehouse_selectable: _wrappers_pb2.BoolValue
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        sequence: _Optional[int] = ...,
        product_categ_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        product_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        packing_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouse_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouse_id: _Optional[int] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class RouteCreateRequest(_message.Message):
    __slots__ = [
        "context",
        "name",
        "packing_selectable",
        "product_categ_selectable",
        "product_selectable",
        "sequence",
        "warehouse_id",
        "warehouse_selectable",
    ]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PACKING_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_CATEG_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_SELECTABLE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    name: str
    packing_selectable: _wrappers_pb2.BoolValue
    product_categ_selectable: _wrappers_pb2.BoolValue
    product_selectable: _wrappers_pb2.BoolValue
    sequence: int
    warehouse_id: int
    warehouse_selectable: _wrappers_pb2.BoolValue
    def __init__(
        self,
        name: _Optional[str] = ...,
        sequence: _Optional[int] = ...,
        product_categ_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        product_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        packing_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouse_selectable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        warehouse_id: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RouteCreateResponse(_message.Message):
    __slots__ = ["response_standard", "route"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    route: Route
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        route: _Optional[_Union[Route, _Mapping]] = ...,
    ) -> None: ...

class RouteDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class RouteDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class RouteReadRequest(_message.Message):
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

class RouteReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "routes"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    routes: _containers.RepeatedCompositeFieldContainer[Route]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        routes: _Optional[_Iterable[_Union[Route, _Mapping]]] = ...,
    ) -> None: ...

class RouteUpdateRequest(_message.Message):
    __slots__ = ["context", "route"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    route: Route
    def __init__(
        self,
        route: _Optional[_Union[Route, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RouteUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "route"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    route: Route
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        route: _Optional[_Union[Route, _Mapping]] = ...,
    ) -> None: ...

class Rule(_message.Message):
    __slots__ = [
        "action",
        "active",
        "id",
        "location_id",
        "location_src_id",
        "name",
        "object_audit",
        "picking_type_id",
        "procure_method",
        "route_id",
        "sequence",
        "warehouse_id",
    ]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SRC_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    PROCURE_METHOD_FIELD_NUMBER: _ClassVar[int]
    ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    action: str
    active: _wrappers_pb2.BoolValue
    id: int
    location_id: int
    location_src_id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    picking_type_id: int
    procure_method: str
    route_id: int
    sequence: int
    warehouse_id: int
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        action: _Optional[str] = ...,
        picking_type_id: _Optional[int] = ...,
        location_src_id: _Optional[int] = ...,
        location_id: _Optional[int] = ...,
        procure_method: _Optional[str] = ...,
        route_id: _Optional[int] = ...,
        warehouse_id: _Optional[int] = ...,
        sequence: _Optional[int] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class RuleCreateRequest(_message.Message):
    __slots__ = [
        "action",
        "context",
        "location_id",
        "location_src_id",
        "name",
        "picking_type_id",
        "procure_method",
        "route_id",
        "sequence",
        "warehouse_id",
    ]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SRC_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PICKING_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    PROCURE_METHOD_FIELD_NUMBER: _ClassVar[int]
    ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    action: str
    context: _base_pb2.Context
    location_id: int
    location_src_id: int
    name: str
    picking_type_id: int
    procure_method: str
    route_id: int
    sequence: int
    warehouse_id: int
    def __init__(
        self,
        name: _Optional[str] = ...,
        action: _Optional[str] = ...,
        picking_type_id: _Optional[int] = ...,
        location_src_id: _Optional[int] = ...,
        location_id: _Optional[int] = ...,
        procure_method: _Optional[str] = ...,
        route_id: _Optional[int] = ...,
        warehouse_id: _Optional[int] = ...,
        sequence: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RuleCreateResponse(_message.Message):
    __slots__ = ["response_standard", "rule"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    rule: Rule
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        rule: _Optional[_Union[Rule, _Mapping]] = ...,
    ) -> None: ...

class RuleDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class RuleDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class RuleReadRequest(_message.Message):
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

class RuleReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "rules"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        rules: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ...,
    ) -> None: ...

class RuleUpdateRequest(_message.Message):
    __slots__ = ["context", "rule"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    rule: Rule
    def __init__(
        self,
        rule: _Optional[_Union[Rule, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class RuleUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "rule"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    rule: Rule
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        rule: _Optional[_Union[Rule, _Mapping]] = ...,
    ) -> None: ...

class Uom(_message.Message):
    __slots__ = ["active", "code", "id", "name", "object_audit", "uom_doc_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    UOM_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    code: str
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    uom_doc_id: str
    def __init__(
        self,
        id: _Optional[int] = ...,
        uom_doc_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class UomCreateRequest(_message.Message):
    __slots__ = ["active", "code", "context", "name", "uom_doc_id"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UOM_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    code: str
    context: _base_pb2.Context
    name: str
    uom_doc_id: str
    def __init__(
        self,
        uom_doc_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class UomCreateResponse(_message.Message):
    __slots__ = ["response_standard", "uom"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    UOM_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    uom: Uom
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        uom: _Optional[_Union[Uom, _Mapping]] = ...,
    ) -> None: ...

class UomDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class UomDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class UomReadRequest(_message.Message):
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

class UomReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "uoms"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    UOMS_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    uoms: _containers.RepeatedCompositeFieldContainer[Uom]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        uoms: _Optional[_Iterable[_Union[Uom, _Mapping]]] = ...,
    ) -> None: ...

class UomUpdateRequest(_message.Message):
    __slots__ = ["context", "uom"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    UOM_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    uom: Uom
    def __init__(
        self, uom: _Optional[_Union[Uom, _Mapping]] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class UomUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "uom"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    UOM_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    uom: Uom
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        uom: _Optional[_Union[Uom, _Mapping]] = ...,
    ) -> None: ...

class Warehouse(_message.Message):
    __slots__ = [
        "active",
        "address",
        "code",
        "complement",
        "country_id",
        "id",
        "name",
        "object_audit",
        "territory_matrix_value",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_VALUE_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    address: str
    code: str
    complement: str
    country_id: int
    id: int
    name: str
    object_audit: _base_pb2.ObjectAudit
    territory_matrix_value: _struct_pb2.Struct
    def __init__(
        self,
        id: _Optional[int] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        country_id: _Optional[int] = ...,
        territory_matrix_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        address: _Optional[str] = ...,
        complement: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class WarehouseCreateRequest(_message.Message):
    __slots__ = ["active", "address", "code", "complement", "context", "country_id", "name", "territory_matrix_value"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_MATRIX_VALUE_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    address: str
    code: str
    complement: str
    context: _base_pb2.Context
    country_id: int
    name: str
    territory_matrix_value: _struct_pb2.Struct
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        country_id: _Optional[int] = ...,
        territory_matrix_value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        address: _Optional[str] = ...,
        complement: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class WarehouseCreateResponse(_message.Message):
    __slots__ = ["response_standard", "warehouse"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    warehouse: Warehouse
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        warehouse: _Optional[_Union[Warehouse, _Mapping]] = ...,
    ) -> None: ...

class WarehouseDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: int
    def __init__(
        self, id: _Optional[int] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class WarehouseDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class WarehouseReadRequest(_message.Message):
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

class WarehouseReadResponse(_message.Message):
    __slots__ = ["meta_data", "response_standard", "warehouses"]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSES_FIELD_NUMBER: _ClassVar[int]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    warehouses: _containers.RepeatedCompositeFieldContainer[Warehouse]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        warehouses: _Optional[_Iterable[_Union[Warehouse, _Mapping]]] = ...,
    ) -> None: ...

class WarehouseUpdateRequest(_message.Message):
    __slots__ = ["context", "warehouse"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    warehouse: Warehouse
    def __init__(
        self,
        warehouse: _Optional[_Union[Warehouse, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class WarehouseUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "warehouse"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    warehouse: Warehouse
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        warehouse: _Optional[_Union[Warehouse, _Mapping]] = ...,
    ) -> None: ...
