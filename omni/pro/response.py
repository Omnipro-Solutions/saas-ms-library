from typing import Optional as _Optional

from omni_pro_base.logger import configure_logger
from omni_pro_base.util import HTTPStatus
from omni_pro_grpc.common import base_pb2

logger = configure_logger(name=__name__)


class MessageCode(object):
    INTERNAL_SERVER_ERROR = "SV001"
    INPUT_VALIDATOR_ERROR = "SV002"
    COGNITO_CLIENT_ERROR = "CO001"
    USER_PASSWORD_CHANGED = "US007"
    USER_EMAIL_CHANGED = "US008"
    USER_UNAUTHORIZED = "US009"
    RESOURCE_CREATED = "RS001"
    RESOURCE_READ = "RS002"
    RESOURCE_FETCHED = "RS002"
    RESOURCE_UPDATED = "RS003"
    RESOURCE_DELETED = "RS004"
    RESOURCE_NOT_FOUND = "RS005"
    RESOURCE_ALREADY_EXISTS = "RS006"
    IMPORT_SUCCESS = "IM001"
    IMPORT_ERROR = "IM002"
    EXPORT_SUCCESS = "EX001"
    EXPORT_ERROR = "EX002"
    IMPORT_EXPORT_PROCESSING = "IM003"
    OPERATION_ERROR = "OE001"


class MessageResponse(object):
    def __init__(self, cls):
        self.cls = cls

    def response(
        self,
        message: str,
        success: bool,
        status_code: int = HTTPStatus.OK,
        message_code: _Optional[str] = ...,
        **kwargs,
    ):
        return self.cls(
            response_standard=base_pb2.ResponseStandard(
                success=success, message=message, status_code=status_code, message_code=message_code
            ),
            **kwargs,
        )

    # FIXME: This is a bad name for this method
    def bad_response(self, message: str, **kwargs):
        return self.input_validator_response(message, **kwargs)

    def input_validator_response(self, message: str, **kwargs):
        return self.response(
            success=False,
            message=message,
            status_code=HTTPStatus.BAD_REQUEST,
            message_code=MessageCode.INPUT_VALIDATOR_ERROR,
            **kwargs,
        )

    def created_response(self, message: str, **kwargs):
        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.CREATED,
            message_code=MessageCode.RESOURCE_CREATED,
            **kwargs,
        )

    def deleted_response(self, message: str, **kwargs):
        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.OK,
            message_code=MessageCode.RESOURCE_DELETED,
            **kwargs,
        )

    def updated_response(self, message: str, **kwargs):
        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.OK,
            message_code=MessageCode.RESOURCE_UPDATED,
            **kwargs,
        )

    def fetched_response(
        self, message: str, paginated: base_pb2.Paginated, total: int, count=0, message_not_found="", **kwargs
    ):
        if kwargs.pop("id", False) and total == 0:
            return self.not_found_response(message_not_found, **kwargs)

        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.OK,
            message_code=MessageCode.RESOURCE_FETCHED,
            meta_data=base_pb2.MetaData(
                limit=paginated.limit,
                offset=paginated.offset,
                total=total,
                count=count or total,
            ),
            **kwargs,
        )

    def internal_response(self, message: str, message_code: str = MessageCode.INTERNAL_SERVER_ERROR, **kwargs):
        return self.response(
            message=message,
            success=False,
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            message_code=message_code,
            **kwargs,
        )

    def already_exists_response(self, message: str, **kwargs):
        return self.response(
            success=False,
            message=message,
            status_code=HTTPStatus.OK,
            message_code=MessageCode.RESOURCE_ALREADY_EXISTS,
            **kwargs,
        )

    def not_found_response(self, message: str, **kwargs):
        return self.response(
            success=False,
            message=message,
            status_code=HTTPStatus.NOT_FOUND,
            message_code=MessageCode.RESOURCE_NOT_FOUND,
            **kwargs,
        )

    def unauthorized_response(self, message: str = "User Unauthorized", **kwargs):
        return self.response(
            success=False,
            message=message,
            status_code=HTTPStatus.UNAUTHORIZED,
            message_code=MessageCode.USER_UNAUTHORIZED,
            **kwargs,
        )

    def method_not_allowed_response(self, message: str = "Method Not Allowed", **kwargs):
        return self.response(
            success=False,
            message=message,
            status_code=HTTPStatus.METHOD_NOT_ALLOWED,
            message_code=MessageCode.USER_UNAUTHORIZED,
            **kwargs,
        )

    def success_response(self, message: str, **kwargs):
        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.OK,
            message_code=MessageCode.RESOURCE_READ,
            **kwargs,
        )

    def success_import_response(self, message: str, **kwargs):
        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.OK,
            message_code=MessageCode.IMPORT_SUCCESS,
            **kwargs,
        )

    def success_export_response(self, message: str, **kwargs):
        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.OK,
            message_code=MessageCode.EXPORT_SUCCESS,
            **kwargs,
        )

    def import_export_processing_response(self, message: str, **kwargs):
        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.CREATED,
            message_code=MessageCode.IMPORT_EXPORT_PROCESSING,
            **kwargs,
        )

    def import_error_response(self, message: str, **kwargs):
        return self.response(
            success=False,
            message=message,
            status_code=HTTPStatus.BAD_REQUEST,
            message_code=MessageCode.IMPORT_ERROR,
            **kwargs,
        )

    def export_error_response(self, message: str, **kwargs):
        return self.response(
            success=False,
            message=message,
            status_code=HTTPStatus.BAD_REQUEST,
            message_code=MessageCode.EXPORT_ERROR,
            **kwargs,
        )

    def operation_error(self, message: str, **kwargs):
        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.OK,
            message_code=MessageCode.OPERATION_ERROR,
            **kwargs,
        )

    def no_content_error(self, message: str, **kwargs):
        return self.response(
            success=True,
            message=message,
            status_code=HTTPStatus.NO_CONTENT,
            message_code=MessageCode.RESOURCE_NOT_FOUND,
            **kwargs,
        )
