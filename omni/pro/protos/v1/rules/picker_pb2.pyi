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
from omni.pro.protos.v1.rules import category_pb2 as _category_pb2
from omni.pro.protos.v1.rules import user_pb2 as _user_pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as _warehouse_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CategoryValues(_message.Message):
    __slots__ = ["family_doc_id", "group_code", "attribute_code", "code"]
    FAMILY_DOC_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_CODE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    family_doc_id: str
    group_code: str
    attribute_code: str
    code: str
    def __init__(
        self,
        family_doc_id: _Optional[str] = ...,
        group_code: _Optional[str] = ...,
        attribute_code: _Optional[str] = ...,
        code: _Optional[str] = ...,
    ) -> None: ...

class Picker(_message.Message):
    __slots__ = [
        "id",
        "user",
        "warehouse",
        "categories",
        "can_pick",
        "can_pack",
        "can_out",
        "can_int",
        "can_in",
        "can_return",
        "status",
        "active",
        "external_id",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CAN_PICK_FIELD_NUMBER: _ClassVar[int]
    CAN_PACK_FIELD_NUMBER: _ClassVar[int]
    CAN_OUT_FIELD_NUMBER: _ClassVar[int]
    CAN_INT_FIELD_NUMBER: _ClassVar[int]
    CAN_IN_FIELD_NUMBER: _ClassVar[int]
    CAN_RETURN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user: _user_pb2.User
    warehouse: _warehouse_pb2.Warehouse
    categories: _containers.RepeatedCompositeFieldContainer[_category_pb2.Category]
    can_pick: _wrappers_pb2.BoolValue
    can_pack: _wrappers_pb2.BoolValue
    can_out: _wrappers_pb2.BoolValue
    can_int: _wrappers_pb2.BoolValue
    can_in: _wrappers_pb2.BoolValue
    can_return: _wrappers_pb2.BoolValue
    status: str
    active: _wrappers_pb2.BoolValue
    external_id: str
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...,
        warehouse: _Optional[_Union[_warehouse_pb2.Warehouse, _Mapping]] = ...,
        categories: _Optional[_Iterable[_Union[_category_pb2.Category, _Mapping]]] = ...,
        can_pick: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_pack: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_out: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_int: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_in: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_return: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        status: _Optional[str] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        external_id: _Optional[str] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class PickerCreateRequest(_message.Message):
    __slots__ = [
        "user_id",
        "warehouse_id",
        "category_values",
        "can_pick",
        "can_pack",
        "can_out",
        "can_int",
        "can_in",
        "can_return",
        "status",
        "context",
    ]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_VALUES_FIELD_NUMBER: _ClassVar[int]
    CAN_PICK_FIELD_NUMBER: _ClassVar[int]
    CAN_PACK_FIELD_NUMBER: _ClassVar[int]
    CAN_OUT_FIELD_NUMBER: _ClassVar[int]
    CAN_INT_FIELD_NUMBER: _ClassVar[int]
    CAN_IN_FIELD_NUMBER: _ClassVar[int]
    CAN_RETURN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    warehouse_id: int
    category_values: _containers.RepeatedCompositeFieldContainer[CategoryValues]
    can_pick: _wrappers_pb2.BoolValue
    can_pack: _wrappers_pb2.BoolValue
    can_out: _wrappers_pb2.BoolValue
    can_int: _wrappers_pb2.BoolValue
    can_in: _wrappers_pb2.BoolValue
    can_return: _wrappers_pb2.BoolValue
    status: str
    context: _base_pb2.Context
    def __init__(
        self,
        user_id: _Optional[str] = ...,
        warehouse_id: _Optional[int] = ...,
        category_values: _Optional[_Iterable[_Union[CategoryValues, _Mapping]]] = ...,
        can_pick: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_pack: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_out: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_int: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_in: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        can_return: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        status: _Optional[str] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickerCreateResponse(_message.Message):
    __slots__ = ["picker", "response_standard"]
    PICKER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    picker: Picker
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        picker: _Optional[_Union[Picker, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class PickerReadRequest(_message.Message):
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

class PickerReadResponse(_message.Message):
    __slots__ = ["pickers", "meta_data", "response_standard"]
    PICKERS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    pickers: _containers.RepeatedCompositeFieldContainer[Picker]
    meta_data: _base_pb2.MetaData
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        pickers: _Optional[_Iterable[_Union[Picker, _Mapping]]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class PickerUpdateRequest(_message.Message):
    __slots__ = ["picker", "context"]
    PICKER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    picker: Picker
    context: _base_pb2.Context
    def __init__(
        self,
        picker: _Optional[_Union[Picker, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class PickerUpdateResponse(_message.Message):
    __slots__ = ["picker", "response_standard"]
    PICKER_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    picker: Picker
    response_standard: _base_pb2.ResponseStandard
    def __init__(
        self,
        picker: _Optional[_Union[Picker, _Mapping]] = ...,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
    ) -> None: ...

class PickerDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class PickerDeleteResponse(_message.Message):
    __slots__ = ["response_standard"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    def __init__(self, response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...) -> None: ...
