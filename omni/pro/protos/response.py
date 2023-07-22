from typing import Optional as _Optional

from omni.pro.database import DBUtil
from omni.pro.logger import LoggerTraceback, configure_logger
from omni.pro.protos.common import base_pb2
from omni.pro.stack import ExitStackDocument
from omni.pro.util import HTTPStatus

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

    def fetched_response(self, message: str, paginated: base_pb2.Paginated, total: int, count=0, **kwargs):
        if kwargs.pop("id", False) and total == 0:
            return self.not_found_response(message, **kwargs)

        return self.response(
            success=total > 0,
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


def read_response(
    request,
    context,
    document_class,
    reference_list: list,
    message_response: MessageResponse,
    msg_success: str,
    msg_exception: str,
    entry_field_name: str,
    **kwargs,
):
    """
    :param request: request is a Message grpc\n
    :param context: context is a Message grpc with db_manager, db_name field\n
    :param document_class: document_class is a Document class\n
    :param reference_list: reference_list is a list of Document class\n
    :param message_response: message_response is a MessageResponse instance\n
    :param msg_success: msg_success is a success message\n
    :param msg_exception: msg_exception is a exception message\n
    :return: MessageResponse cls param
    """
    try:
        with ExitStackDocument(document_classes=reference_list, db_alias=context.db_name):
            data = DBUtil.db_prepared_statement(
                request.id,
                request.fields,
                request.filter,
                request.paginated,
                None,
                request.sort_by,
            )
            list_docs, total = context.db_manager.list_documents(
                context.db_name,
                request.context.tenant,
                document_class,
                **data,
            )
            kwargs_return = {
                f"{entry_field_name}": [doc.to_proto() for doc in list_docs],
            } | kwargs
            return message_response.fetched_response(
                message=msg_success,
                total=total,
                count=len(list_docs),
                id=request.id,
                paginated=request.paginated,
                **kwargs_return,
            )
    except Exception as e:
        LoggerTraceback.error(msg_exception, e, logger)
        return message_response.internal_response(message=msg_exception)
