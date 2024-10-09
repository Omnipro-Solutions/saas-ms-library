import unittest
from unittest.mock import MagicMock, patch

from omni.pro.aws.client import AWSClient


class TestAWSClient(unittest.TestCase):

    @patch("boto3.client")
    def test_aws_client_initialization(self, mock_boto_client):
        mock_service_model = MagicMock()
        mock_service_model.service_name = "s3"

        mock_boto_client.return_value._service_model = mock_service_model

        service_name = "s3"
        region_name = "us-east-1"
        aws_access_key_id = "AKIAIOS"
        aws_secret_access_key = "wJal"

        aws_client = AWSClient(service_name, region_name, aws_access_key_id, aws_secret_access_key)

        mock_boto_client.assert_called_once_with(
            service_name=service_name,
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

        self.assertEqual(aws_client._client._service_model.service_name, service_name)


if __name__ == "__main__":
    unittest.main()
