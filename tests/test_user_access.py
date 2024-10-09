import unittest
from unittest.mock import MagicMock, patch

from omni.pro.models.base import BaseModel
from omni.pro.user.access import Permission, permission_required
from omni_pro_grpc.v1.users import user_pb2


class MockResponseClass:
    def __init__(self, cls):
        self.cls = cls

    def unauthorized_response(self):
        return {"status_code": 401}

    def internal_response(self, message):
        return {"status_code": 500, "message": message}


class TestPermissionRequiredDecorator(unittest.TestCase):

    def setUp(self):
        self.request = MagicMock()
        self.request.context.user = "test_user"
        self.request.context.tenant = "test_tenant"
        self.context = MagicMock()

        self.grpc_response = user_pb2.HasPermissionResponse(has_permission=True)
        self.success_response = (self.grpc_response, True)

    @patch("omni.pro.user.access.GRPClient.call_rpc_fuction")
    @patch("omni.pro.response.MessageResponse", return_value=MockResponseClass(BaseModel))
    def test_permission_granted(self, mock_message_response, mock_grpc_call):
        mock_grpc_call.return_value = self.success_response

        @permission_required(Permission.CAN_CREATE_USER, BaseModel)
        def sample_function(instance, request, context):
            return "Access Granted"

        result = sample_function(self, self.request, self.context)

        self.assertEqual(result, "Access Granted")
        mock_grpc_call.assert_called_once()


if __name__ == "__main__":
    unittest.main()
