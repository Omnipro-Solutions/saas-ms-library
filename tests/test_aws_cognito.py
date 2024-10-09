import unittest
from http import HTTPStatus
from unittest.mock import patch

from botocore.exceptions import ClientError
from omni.pro.aws.cognito import AWSCognitoClient


class TestAWSCognitoClient(unittest.TestCase):

    @patch("boto3.client")
    def test_get_user(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.admin_get_user.return_value = {
            "Username": "test_user",
            "UserAttributes": [
                {"Name": "email", "Value": "user@example.com"},
            ],
        }

        cognito_client = AWSCognitoClient(
            region_name="us-east-1",
            aws_access_key_id="test-key-id",
            aws_secret_access_key="test-secret-key",
            user_pool_id="us-east-1_123456789",
            client_id="1234567890123456789012",
        )

        user_info = cognito_client.get_user(username="test_user")

        mock_boto_client_instance.admin_get_user.assert_called_once_with(
            UserPoolId="us-east-1_123456789", Username="test_user"
        )

        self.assertEqual(user_info["Username"], "test_user")

    @patch("omni.pro.aws.cognito.generate_strong_password", return_value="temporary_password")
    @patch("boto3.client")
    def test_create_user(self, mock_boto_client, mock_generate_password):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.admin_create_user.return_value = {"User": "created"}

        cognito_client = AWSCognitoClient(
            region_name="us-east-1",
            aws_access_key_id="test-key-id",
            aws_secret_access_key="test-secret-key",
            user_pool_id="us-east-1_123456789",
            client_id="1234567890123456789012",
        )

        response = cognito_client.create_user(
            username="test_user",
            password="Password123!",
            name="John Doe",
            email="john.doe@example.com",
            tenant="tenant1",
            language_code="en-US",
            timezone_code="UTC",
        )

        mock_boto_client_instance.admin_create_user.assert_called_once_with(
            UserPoolId="us-east-1_123456789",
            Username="test_user",
            TemporaryPassword="temporary_password",
            UserAttributes=[
                {"Name": "name", "Value": "John Doe"},
                {"Name": "email", "Value": "john.doe@example.com"},
                {"Name": "custom:tenant", "Value": "tenant1"},
                {"Name": "locale", "Value": "en-US"},
                {"Name": "zoneinfo", "Value": "UTC"},
            ],
        )

        self.assertEqual(response["User"], "created")

    @patch("boto3.client")
    def test_delete_user(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.admin_delete_user.return_value = {"Response": "deleted"}

        cognito_client = AWSCognitoClient(
            region_name="us-east-1",
            aws_access_key_id="test-key-id",
            aws_secret_access_key="test-secret-key",
            user_pool_id="us-east-1_123456789",
            client_id="1234567890123456789012",
        )

        response = cognito_client.delete_user(username="test_user")

        mock_boto_client_instance.admin_delete_user.assert_called_once_with(
            UserPoolId="us-east-1_123456789", Username="test_user"
        )

        self.assertEqual(response["Response"], "deleted")

    @patch("boto3.client")
    def test_init_auth_success(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.initiate_auth.return_value = {
            "AuthenticationResult": {"IdToken": "id_token", "RefreshToken": "refresh_token", "ExpiresIn": 3600}
        }

        cognito_client = AWSCognitoClient(
            region_name="us-east-1",
            aws_access_key_id="test-key-id",
            aws_secret_access_key="test-secret-key",
            user_pool_id="us-east-1_123456789",
            client_id="1234567890123456789012",
        )

        status_code, auth_result, message = cognito_client.init_auth(username="test_user", password="Password123!")

        mock_boto_client_instance.initiate_auth.assert_called_once_with(
            ClientId="1234567890123456789012",
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": "test_user", "PASSWORD": "Password123!"},
        )

        self.assertEqual(status_code, HTTPStatus.OK)
        self.assertEqual(auth_result["token"], "id_token")
        self.assertEqual(auth_result["refresh_token"], "refresh_token")
        self.assertEqual(message, "Success")

    @patch("boto3.client")
    def test_init_auth_failure(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.initiate_auth.side_effect = ClientError(
            error_response={"Error": {"Code": "NotAuthorizedException", "Message": "User is not authorized"}},
            operation_name="initiate_auth",
        )

        cognito_client = AWSCognitoClient(
            region_name="us-east-1",
            aws_access_key_id="test-key-id",
            aws_secret_access_key="test-secret-key",
            user_pool_id="us-east-1_123456789",
            client_id="1234567890123456789012",
        )

        status_code, auth_result, message = cognito_client.init_auth(username="test_user", password="Password123!")

        self.assertEqual(status_code, HTTPStatus.UNAUTHORIZED)
        self.assertEqual(message, "Invalid auth data")


if __name__ == "__main__":
    unittest.main()
