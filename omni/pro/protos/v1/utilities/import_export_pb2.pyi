from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from omni.pro.protos.common import base_pb2 as _base_pb2
from omni.pro.protos.v1.utilities import model_pb2 as _model_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ImportExport(_message.Message):
    __slots__ = [
        "id",
        "type_operation",
        "model",
        "name_file",
        "type_file",
        "date_load",
        "date_process",
        "status",
        "message",
        "required_fields",
        "process_data",
        "skip_error",
        "active",
        "object_audit",
    ]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_OPERATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FILE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FILE_FIELD_NUMBER: _ClassVar[int]
    DATE_LOAD_FIELD_NUMBER: _ClassVar[int]
    DATE_PROCESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PROCESS_DATA_FIELD_NUMBER: _ClassVar[int]
    SKIP_ERROR_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_AUDIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    type_operation: str
    model: _model_pb2.Model
    name_file: str
    type_file: str
    date_load: _timestamp_pb2.Timestamp
    date_process: _timestamp_pb2.Timestamp
    status: str
    message: str
    required_fields: _containers.RepeatedScalarFieldContainer[str]
    process_data: _struct_pb2.Struct
    skip_error: _wrappers_pb2.BoolValue
    active: _wrappers_pb2.BoolValue
    object_audit: _base_pb2.ObjectAudit
    def __init__(
        self,
        id: _Optional[str] = ...,
        type_operation: _Optional[str] = ...,
        model: _Optional[_Union[_model_pb2.Model, _Mapping]] = ...,
        name_file: _Optional[str] = ...,
        type_file: _Optional[str] = ...,
        date_load: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        date_process: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        status: _Optional[str] = ...,
        message: _Optional[str] = ...,
        required_fields: _Optional[_Iterable[str]] = ...,
        process_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...,
        skip_error: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        object_audit: _Optional[_Union[_base_pb2.ObjectAudit, _Mapping]] = ...,
    ) -> None: ...

class ImportExportCreateRequest(_message.Message):
    __slots__ = [
        "type_operation",
        "model_id",
        "name_file",
        "type_file",
        "date_init",
        "date_finish",
        "required_fields",
        "skip_error",
        "context",
    ]
    TYPE_OPERATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FILE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FILE_FIELD_NUMBER: _ClassVar[int]
    DATE_INIT_FIELD_NUMBER: _ClassVar[int]
    DATE_FINISH_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    SKIP_ERROR_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    type_operation: str
    model_id: str
    name_file: str
    type_file: str
    date_init: _timestamp_pb2.Timestamp
    date_finish: _timestamp_pb2.Timestamp
    required_fields: _containers.RepeatedScalarFieldContainer[str]
    skip_error: _wrappers_pb2.BoolValue
    context: _base_pb2.Context
    def __init__(
        self,
        type_operation: _Optional[str] = ...,
        model_id: _Optional[str] = ...,
        name_file: _Optional[str] = ...,
        type_file: _Optional[str] = ...,
        date_init: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        date_finish: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...,
        required_fields: _Optional[_Iterable[str]] = ...,
        skip_error: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ImportExportCreateResponse(_message.Message):
    __slots__ = ["response_standard", "import_export"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    IMPORT_EXPORT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    import_export: ImportExport
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        import_export: _Optional[_Union[ImportExport, _Mapping]] = ...,
    ) -> None: ...

class ImportExportReadRequest(_message.Message):
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

class ImportExportReadResponse(_message.Message):
    __slots__ = ["response_standard", "meta_data", "import_export"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    IMPORT_EXPORT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    meta_data: _base_pb2.MetaData
    import_export: _containers.RepeatedCompositeFieldContainer[ImportExport]
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        meta_data: _Optional[_Union[_base_pb2.MetaData, _Mapping]] = ...,
        import_export: _Optional[_Iterable[_Union[ImportExport, _Mapping]]] = ...,
    ) -> None: ...

class ImportExportUpdateRequest(_message.Message):
    __slots__ = ["import_export", "context"]
    IMPORT_EXPORT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    import_export: ImportExport
    context: _base_pb2.Context
    def __init__(
        self,
        import_export: _Optional[_Union[ImportExport, _Mapping]] = ...,
        context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...,
    ) -> None: ...

class ImportExportUpdateResponse(_message.Message):
    __slots__ = ["response_standard", "import_export"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    IMPORT_EXPORT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    import_export: ImportExport
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        import_export: _Optional[_Union[ImportExport, _Mapping]] = ...,
    ) -> None: ...

class ImportExportDeleteRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ImportExportDeleteResponse(_message.Message):
    __slots__ = ["response_standard", "import_export"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    IMPORT_EXPORT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    import_export: ImportExport
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        import_export: _Optional[_Union[ImportExport, _Mapping]] = ...,
    ) -> None: ...

class ConfirmUploadRequest(_message.Message):
    __slots__ = ["id", "context"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    context: _base_pb2.Context
    def __init__(
        self, id: _Optional[str] = ..., context: _Optional[_Union[_base_pb2.Context, _Mapping]] = ...
    ) -> None: ...

class ConfirmUploadResponse(_message.Message):
    __slots__ = ["response_standard", "import_export"]
    RESPONSE_STANDARD_FIELD_NUMBER: _ClassVar[int]
    IMPORT_EXPORT_FIELD_NUMBER: _ClassVar[int]
    response_standard: _base_pb2.ResponseStandard
    import_export: ImportExport
    def __init__(
        self,
        response_standard: _Optional[_Union[_base_pb2.ResponseStandard, _Mapping]] = ...,
        import_export: _Optional[_Union[ImportExport, _Mapping]] = ...,
    ) -> None: ...
