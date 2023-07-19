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

class Family(_message.Message):
    __slots__ = [
        "id",
        "name",
        "code",
        "attribute_as_label",
        "attribute_as_image",
        "variants",
        "groups",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_LABEL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_IMAGE_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    code: str
    attribute_as_label: Attribute
    attribute_as_image: Attribute
    variants: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    groups: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
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
    __slots__ = ["name", "code", "attribute_as_label", "attribute_as_image", "context"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_LABEL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_AS_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    code: str
    attribute_as_label: str
    attribute_as_image: str
    context: _base_pb2.Context
    def __init__(
        self,
        name: _Optional[str] = ...,
        code: _Optional[str] = ...,
        attribute_as_label: _Optional[str] = ...,
        attribute_as_image: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FamilyCreateResponse(_message.Message):
    __slots__ = ["response_standard", "family"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    family: Family
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        family: _Optional[_Union[Family, _Mapping]] = ...,
    ) -> None: ...

class FamilyReadRequest(_message.Message):
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

class FamilyReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "families", "context"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    FAMILIES_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    families: _containers.RepeatedCompositeFieldContainer[Family]
    context: _base_pb2.Context
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        families: _Optional[_Iterable[_Union[Family, _Mapping]]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FamilyUpdateRequest(_message.Message):
    __slots__ = ["family", "context"]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family: Family
    context: _base_pb2.Context
    def __init__(
        self,
        family: _Optional[_Union[Family, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class FamilyUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "family"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    family: Family
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        family: _Optional[_Union[Family, _Mapping]] = ...,
    ) -> None: ...

class FamilyDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class FamilyDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...

class Attribute(_message.Message):
    __slots__ = ["code", "name", "attribute_type", "is_common", "family", "group", "active", "extra_attribute"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    attribute_type: str
    is_common: bool
    family: _struct_pb2.Struct
    group: _struct_pb2.Struct
    active: _wrappers_pb2.BoolValue
    extra_attribute: _struct_pb2.Struct
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
    __slots__ = ["family_id", "group_code", "code", "name", "attribute_type", "is_common", "extra_attribute", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_COMMON_FIELD_NUMBER: _ClassVar[int]
    EXTRA_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    group_code: str
    code: str
    name: str
    attribute_type: str
    is_common: bool
    extra_attribute: _struct_pb2.Struct
    context: _base_pb2.Context
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
    __slots__ = ["response_standard", "attribute"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    attribute: Attribute
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute: _Optional[_Union[Attribute, _Mapping]] = ...,
    ) -> None: ...

class AttributeReadRequest(_message.Message):
    __slots__ = ["family_id", "group_code", "code", "group_by", "sort_by", "fields", "filter", "paginated", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    group_code: str
    code: str
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    context: _base_pb2.Context
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
    __slots__ = ["response_standard", "meta_data", "attributes"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
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
    __slots__ = ["response_standard", "attribute"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    attribute: Attribute
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute: _Optional[_Union[Attribute, _Mapping]] = ...,
    ) -> None: ...

class AttributeDeleteRequest(_message.Message):
    __slots__ = ["family_id", "group_code", "code", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    group_code: str
    code: str
    context: _base_pb2.Context
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

class Group(_message.Message):
    __slots__ = ["code", "name", "active", "family", "attributes"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    active: _wrappers_pb2.BoolValue
    family: _struct_pb2.Struct
    attributes: _containers.RepeatedCompositeFieldContainer[Attribute]
    def __init__(
        self,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        family: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        attributes: _Optional[_Iterable[_Union[Attribute, _Mapping]]] = ...,
    ) -> None: ...

class GroupCreateRequest(_message.Message):
    __slots__ = ["family_id", "code", "name", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    code: str
    name: str
    context: _base_pb2.Context
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        code: _Optional[str] = ...,
        name: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class GroupCreateResponse(_message.Message):
    __slots__ = ["response_standard", "group"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    group: Group
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        group: _Optional[_Union[Group, _Mapping]] = ...,
    ) -> None: ...

class GroupReadRequest(_message.Message):
    __slots__ = ["family_id", "code", "group_by", "sort_by", "fields", "filter", "paginated", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    code: str
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    context: _base_pb2.Context
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
    __slots__ = ["response_standard", "meta_data", "groups"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    groups: _containers.RepeatedCompositeFieldContainer[Group]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        groups: _Optional[_Iterable[_Union[Group, _Mapping]]] = ...,
    ) -> None: ...

class GroupUpdateRequest(_message.Message):
    __slots__ = ["family_id", "group", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    group: Group
    context: _base_pb2.Context
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        group: _Optional[_Union[Group, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class GroupUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "group"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    group: Group
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        group: _Optional[_Union[Group, _Mapping]] = ...,
    ) -> None: ...

class GroupDeleteRequest(_message.Message):
    __slots__ = ["family_id", "code", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    code: str
    context: _base_pb2.Context
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

class AttributeVariant(_message.Message):
    __slots__ = ["attribute", "sequence", "family_id", "active"]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    attribute: _struct_pb2.Struct
    sequence: int
    family_id: str
    active: _wrappers_pb2.BoolValue
    def __init__(
        self,
        attribute: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        sequence: _Optional[int] = ...,
        family_id: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantCreateRequest(_message.Message):
    __slots__ = ["family_id", "attribute_code", "sequence", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_CODE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    attribute_code: str
    sequence: int
    context: _base_pb2.Context
    def __init__(
        self,
        family_id: _Optional[str] = ...,
        attribute_code: _Optional[str] = ...,
        sequence: _Optional[int] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantCreateResponse(_message.Message):
    __slots__ = ["response_standard", "attribute_variant"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    attribute_variant: AttributeVariant
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute_variant: _Optional[_Union[AttributeVariant, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantReadRequest(_message.Message):
    __slots__ = ["family_id", "attribute_code", "group_by", "sort_by", "fields", "filter", "paginated", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_CODE_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    attribute_code: str
    group_by: _containers.RepeatedCompositeFieldContainer[_base_pb2.GroupBy]
    sort_by: _base_pb2.SortBy
    fields: _base_pb2.Fields
    filter: _base_pb2.Filter
    paginated: _base_pb2.Paginated
    context: _base_pb2.Context
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
    __slots__ = ["response_standard", "meta_data", "attribute_variants"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VARIANTS_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    attribute_variants: _containers.RepeatedCompositeFieldContainer[AttributeVariant]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        attribute_variants: _Optional[_Iterable[_Union[AttributeVariant, _Mapping]]] = ...,
    ) -> None: ...

class AttributeVariantUpdateRequest(_message.Message):
    __slots__ = ["code", "attribute_variant", "context"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    code: str
    attribute_variant: AttributeVariant
    context: _base_pb2.Context
    def __init__(
        self,
        code: _Optional[str] = ...,
        attribute_variant: _Optional[_Union[AttributeVariant, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "attribute_variant"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    attribute_variant: AttributeVariant
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        attribute_variant: _Optional[_Union[AttributeVariant, _Mapping]] = ...,
    ) -> None: ...

class AttributeVariantDeleteRequest(_message.Message):
    __slots__ = ["family_id", "attribute_code", "context"]
    FAMILY_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    family_id: str
    attribute_code: str
    context: _base_pb2.Context
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
