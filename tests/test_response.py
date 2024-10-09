import unittest
from http import HTTPStatus
from unittest.mock import MagicMock

from omni.pro.response import MessageCode, MessageResponse
from omni_pro_grpc.common import base_pb2


class TestMessageResponse(unittest.TestCase):

    def setUp(self):
        self.response_class = MagicMock()
        self.message_response = MessageResponse(self.response_class)

    def test_response(self):
        result = self.message_response.response(
            message="Test Message", success=True, status_code=HTTPStatus.OK, message_code=MessageCode.RESOURCE_READ
        )
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=True,
                message="Test Message",
                status_code=HTTPStatus.OK,
                message_code=MessageCode.RESOURCE_READ,
            ),
        )

    def test_input_validator_response(self):
        result = self.message_response.input_validator_response(message="Invalid Input")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=False,
                message="Invalid Input",
                status_code=HTTPStatus.BAD_REQUEST,
                message_code=MessageCode.INPUT_VALIDATOR_ERROR,
            ),
        )

    def test_created_response(self):
        result = self.message_response.created_response(message="Resource Created")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=True,
                message="Resource Created",
                status_code=HTTPStatus.CREATED,
                message_code=MessageCode.RESOURCE_CREATED,
            ),
        )

    def test_deleted_response(self):
        result = self.message_response.deleted_response(message="Resource Deleted")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=True,
                message="Resource Deleted",
                status_code=HTTPStatus.OK,
                message_code=MessageCode.RESOURCE_DELETED,
            ),
        )

    def test_updated_response(self):
        result = self.message_response.updated_response(message="Resource Updated")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=True,
                message="Resource Updated",
                status_code=HTTPStatus.OK,
                message_code=MessageCode.RESOURCE_UPDATED,
            ),
        )

    def test_fetched_response(self):
        paginated = base_pb2.Paginated(limit=10, offset=0)
        result = self.message_response.fetched_response(
            message="Resources Fetched",
            paginated=paginated,
            total=5,
            count=5,
        )
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=True,
                message="Resources Fetched",
                status_code=HTTPStatus.OK,
                message_code=MessageCode.RESOURCE_FETCHED,
            ),
            meta_data=base_pb2.MetaData(limit=10, offset=0, total=5, count=5),
        )

    def test_internal_response(self):
        result = self.message_response.internal_response(message="Internal Server Error")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=False,
                message="Internal Server Error",
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                message_code=MessageCode.INTERNAL_SERVER_ERROR,
            ),
        )

    def test_already_exists_response(self):
        result = self.message_response.already_exists_response(message="Resource Already Exists")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=False,
                message="Resource Already Exists",
                status_code=HTTPStatus.OK,
                message_code=MessageCode.RESOURCE_ALREADY_EXISTS,
            ),
        )

    def test_not_found_response(self):
        result = self.message_response.not_found_response(message="Resource Not Found")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=False,
                message="Resource Not Found",
                status_code=HTTPStatus.NOT_FOUND,
                message_code=MessageCode.RESOURCE_NOT_FOUND,
            ),
        )

    def test_unauthorized_response(self):
        result = self.message_response.unauthorized_response(message="User Unauthorized")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=False,
                message="User Unauthorized",
                status_code=HTTPStatus.UNAUTHORIZED,
                message_code=MessageCode.USER_UNAUTHORIZED,
            ),
        )

    def test_method_not_allowed_response(self):
        result = self.message_response.method_not_allowed_response(message="Method Not Allowed")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=False,
                message="Method Not Allowed",
                status_code=HTTPStatus.METHOD_NOT_ALLOWED,
                message_code=MessageCode.USER_UNAUTHORIZED,
            ),
        )

    def test_success_response(self):
        result = self.message_response.success_response(message="Success")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=True,
                message="Success",
                status_code=HTTPStatus.OK,
                message_code=MessageCode.RESOURCE_READ,
            ),
        )

    def test_import_export_processing_response(self):
        result = self.message_response.import_export_processing_response(message="Processing")
        self.response_class.assert_called_once_with(
            response_standard=base_pb2.ResponseStandard(
                success=True,
                message="Processing",
                status_code=HTTPStatus.CREATED,
                message_code=MessageCode.IMPORT_EXPORT_PROCESSING,
            ),
        )


if __name__ == "__main__":
    unittest.main()
