from typing import Optional as _Optional

from omni.pro.protos.common import base_pb2
from omni.pro.util import HTTPStatus


class MessageCode(object):
    INTERNAL_SERVER_ERROR = "SV001"
    INPUT_VALIDATOR_ERROR = "SV002"
    COGNITO_CLIENT_ERROR = "CO001"
    USER_PASSWORD_CHANGED = "US007"
    RESOURCE_CREATED = "RS001"
    RESOURCE_READ = "RS002"
    RESOURCE_FETCHED = "RS002"
    RESOURCE_UPDATED = "RS003"
    RESOURCE_DELETED = "RS004"
    RESOURCE_NOT_FOUND = "RS005"
    RESOURCE_ALREADY_EXISTS = "RS006"


class MessageResponse(object):
    def __init__(self, cls):
        self.cls = cls

    def response(
        self,
        message: str,
        success: bool,
        status_code: int = HTTPStatus.OK,
        message_code: _Optional[str] = ...,
        **kwargs
    ):
        return self.cls(
            response_standard=base_pb2.ResponseStandard(
                success=success, message=message, status_code=status_code, message_code=message_code
            ),
            **kwargs,
        )

    def bad_response(self, message: str, **kwargs):
        return self.response(
            success=False,
            message=message,
            status_code=HTTPStatus.BAD_REQUEST,
            message_code=MessageCode.INPUT_VALIDATOR_ERROR,
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

    def not_found_response(self, message: str, **kwargs):
        return self.response(
            success=False,
            message=message,
            status_code=HTTPStatus.NOT_FOUND,
            message_code=MessageCode.RESOURCE_NOT_FOUND,
            **kwargs,
        )
