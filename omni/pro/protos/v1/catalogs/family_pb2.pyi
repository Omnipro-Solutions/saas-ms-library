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

class Attribute(_message.Message):
    __slots__ = ["active", "attribute_type", "code", "extra_attribute", "family", "group", "is_common", "name"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    attribute_type: str
    code: str
    extra_attribute: _struct_pb2.Struct
    family: _struct_pb2.Struct
    group: _struct_pb2.Struct
    is_common: bool
    name: str
    def __init__(
        self,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        attribute_type: _Optional[str] = ...,
        is_common: bool = ...,
        family: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        group: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        extra_attribute: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
    ) -> None: ...

class AttributeCreateRequest(_message.Message):
    __slots__ = ["attribute_type", "code", "context", "extra_attribute", "family_id", "group_code", "is_common", "name"]
    ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_CODE_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    attribute_type: str
    code: str
    context: _base_pb2.Context
    extra_attribute: _struct_pb2.Struct
    family_id: str
    group_code: str
    is_common: bool
    name: str
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        group_code: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        attribute_type: _Optional[str] = ...,
        is_common: bool = ...,
        extra_attribute: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeCreateResponse(_message.Message):
    __slots__ = ["attribute", "response_standard"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    attribute: Attribute
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute: _Optional[_Union[Attribute, _Mapping]] = ...,
    ) -> None: ...

class AttributeDeleteRequest(_message.Message):
    __slots__ = ["code", "context", "family_id", "group_code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    family_id: str
    group_code: str
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        group_code: _Optional[str] = ...,
        code: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class AttributeReadRequest(_message.Message):
    __slots__ = ["code", "context", "family_id", "fields", "filter", "group_by", "group_code", "paginated", "sort_by"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    GROUP_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    family_id: str
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    group_code: str
    paginated: _base_pb2.Paginated
    sort_by: _base_pb2.SortBy
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        group_code: _Optional[str] = ...,
        code: _Optional[str] = ...,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeReadResponse(_message.Message):
    __slots__ = ["attributes", "meta_data", "response_standard"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...,
    ) -> None: ...

class AttributeUpdateRequest(_message.Message):
    __slots__ = ["attribute", "context"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    attribute: Attribute
    context: _base_pb2.Context
    def __init__(
        self,
        attribute: _Optional[_Union[Attribute, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeUpdateResponse(_message.Message):
    __slots__ = ["attribute", "response_standard"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    attribute: Attribute
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute: _Optional[_Union[Attribute, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariant(_message.Message):
    __slots__ = ["active", "attribute", "family_id", "sequence"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    attribute: _struct_pb2.Struct
    family_id: str
    sequence: int
    def __init__(
        self,
        attribute: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        sequence: _Optional[int] = ...,
        family_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantCreateRequest(_message.Message):
    __slots__ = ["attribute_code", "context", "family_id", "sequence"]
    ATTRIBUTE_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    attribute_code: str
    context: _base_pb2.Context
    family_id: str
    sequence: int
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        attribute_code: _Optional[str] = ...,
        sequence: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantCreateResponse(_message.Message):
    __slots__ = ["attribute_variant", "response_standard"]
    ATTRIBUTE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    attribute_variant: AttributeVariant
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute_variant: _Optional[_Union[AttributeVariant, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantDeleteRequest(_message.Message):
    __slots__ = ["attribute_code", "context", "family_id"]
    ATTRIBUTE_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    attribute_code: str
    context: _base_pb2.Context
    family_id: str
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        attribute_code: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class AttributeVariantReadRequest(_message.Message):
    __slots__ = ["attribute_code", "context", "family_id", "fields", "filter", "group_by", "paginated", "sort_by"]
    ATTRIBUTE_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    attribute_code: str
    context: _base_pb2.Context
    family_id: str
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    paginated: _base_pb2.Paginated
    sort_by: _base_pb2.SortBy
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        attribute_code: _Optional[str] = ...,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantReadResponse(_message.Message):
    __slots__ = ["attribute_variants", "meta_data", "response_standard"]
    ATTRIBUTE_VARIANTS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    attribute_variants: _containers.RepeatedCompositeFieldContainer[AttributeVariant]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        attribute_variants: _Optional[_Iterable[_Union[AttributeVariant, _Mapping]]] = ...,
    ) -> None: ...

class AttributeVariantUpdateRequest(_message.Message):
    __slots__ = ["attribute_variant", "code", "context"]
    ATTRIBUTE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    attribute_variant: AttributeVariant
    code: str
    context: _base_pb2.Context
    def __init__(
        self,
        code: _Optional[str] = ...,
        attribute_variant: _Optional[_Union[AttributeVariant, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantUpdateResponse(_message.Message):
    __slots__ = ["attribute_variant", "response_standard"]
    ATTRIBUTE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    attribute_variant: AttributeVariant
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute_variant: _Optional[_Union[AttributeVariant, _Mapping]] = ...,
    ) -> None: ...

class Family(_message.Message):
    __slots__ = [
        "active",
        "attribute_as_image",
        "attribute_as_label",
        "code",
        "groups",
        "id",
        "name",
        "object_audit",
        "variants",
    ]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_IMAGE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_LABEL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    attribute_as_image: Attribute
    attribute_as_label: Attribute
    code: str
    groups: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    id: str
    name: str
    object_audit: _base_pb2.ObjectAudit
    variants: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        attribute_as_label: _Optional[_Union[Attribute, _Mapping]] = ...,
        attribute_as_image: _Optional[_Union[Attribute, _Mapping]] = ...,
        variants: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        groups: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class FamilyCreateRequest(_message.Message):
    __slots__ = ["attribute_as_image", "attribute_as_label", "code", "context", "name"]
    ATTRIBUTE_AS_IMAGE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_LABEL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    attribute_as_image: str
    attribute_as_label: str
    code: str
    context: _base_pb2.Context
    name: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        attribute_as_label: _Optional[str] = ...,
        attribute_as_image: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FamilyCreateResponse(_message.Message):
    __slots__ = ["family", "response_standard"]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    family: Family
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        family: _Optional[_Union[Family, _Mapping]] = ...,
    ) -> None: ...

class FamilyDeleteRequest(_message.Message):
    __slots__ = ["context", "id"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    id: str
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class FamilyDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class FamilyReadRequest(_message.Message):
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

class FamilyReadResponse(_message.Message):
    __slots__ = ["context", "families", "meta_data", "response_standard"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    families: _containers.RepeatedCompositeFieldContainer[Family]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        families: _Optional[_Iterable[_Union[Family, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FamilyUpdateRequest(_message.Message):
    __slots__ = ["context", "family"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    family: Family
    def __init__(
        self,
        family: _Optional[_Union[Family, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FamilyUpdateResponse(_message.Message):
    __slots__ = ["family", "response_standard"]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    family: Family
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        family: _Optional[_Union[Family, _Mapping]] = ...,
    ) -> None: ...

class Group(_message.Message):
    __slots__ = ["active", "attributes", "code", "family", "name"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    active: _wrappers_pb2.BoolValue
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    code: str
    family: _struct_pb2.Struct
    name: str
    def __init__(
        self,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        family: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...,
    ) -> None: ...

class GroupCreateRequest(_message.Message):
    __slots__ = ["code", "context", "family_id", "name"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    family_id: str
    name: str
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class GroupCreateResponse(_message.Message):
    __slots__ = ["group", "response_standard"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    group: Group
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        group: _Optional[_Union[Group, _Mapping]] = ...,
    ) -> None: ...

class GroupDeleteRequest(_message.Message):
    __slots__ = ["code", "context", "family_id"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    family_id: str
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class GroupDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class GroupReadRequest(_message.Message):
    __slots__ = ["code", "context", "family_id", "fields", "filter", "group_by", "paginated", "sort_by"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    code: str
    context: _base_pb2.Context
    family_id: str
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    paginated: _base_pb2.Paginated
    sort_by: _base_pb2.SortBy
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        group_by: _Optional[_Iterable[_Union[_base_pb2.GroupBy, _Mapping]]] = ...,
        sort_by: _Optional[_Union[_base_pb2.SortBy, _Mapping]] = ...,
        fields: _Optional[_Union[_base_pb2.Fields, _Mapping]] = ...,
        filter: _Optional[_Union[_base_pb2.Filter, _Mapping]] = ...,
        paginated: _Optional[_Union[_base_pb2.Paginated, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class GroupReadResponse(_message.Message):
    __slots__ = ["groups", "meta_data", "response_standard"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        groups: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...,
    ) -> None: ...

class GroupUpdateRequest(_message.Message):
    __slots__ = ["context", "family_id", "group"]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    context: _base_pb2.Context
    family_id: str
    group: Group
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        group: _Optional[_Union[Group, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class GroupUpdateResponse(_message.Message):
    __slots__ = ["group", "response_standard"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    group: Group
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        group: _Optional[_Union[Group, _Mapping]] = ...,
    ) -> None: ...
