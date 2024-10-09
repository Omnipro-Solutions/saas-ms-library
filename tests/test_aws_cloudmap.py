import unittest
from unittest.mock import patch

from omni.pro.aws.cloudmap import AWSCloudMap


class TestAWSCloudMap(unittest.TestCase):

    @patch("boto3.client")
    def test_discover_instances(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.discover_instances.return_value = {
            "Instances": [{"Attributes": {"host": "127.0.0.1", "port": "6379", "db": "0"}}]
        }

        aws_cloud_map = AWSCloudMap(
            region_name="us-east-1",
            namespace_name="test-namespace",
            service_name="test-service",
            aws_access_key_id="test-key-id",
            aws_secret_access_key="test-secret-key",
        )

        instances = aws_cloud_map.discover_instances()

        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0]["Attributes"]["host"], "127.0.0.1")
        self.assertEqual(instances[0]["Attributes"]["port"], "6379")

        mock_boto_client_instance.discover_instances.assert_called_once_with(
            NamespaceName="test-namespace", ServiceName="test-service"
        )

    @patch("boto3.client")
    def test_get_redis_config(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.discover_instances.return_value = {
            "Instances": [{"Attributes": {"host": "127.0.0.1", "port": "6379", "db": "0"}}]
        }

        aws_cloud_map = AWSCloudMap(
            region_name="us-east-1",
            namespace_name="test-namespace",
            service_name="test-service",
            aws_access_key_id="test-key-id",
            aws_secret_access_key="test-secret-key",
        )

        redis_config = aws_cloud_map.get_redis_config()

        self.assertEqual(redis_config["host"], "127.0.0.1")
        self.assertEqual(redis_config["port"], 6379)
        self.assertEqual(redis_config["db"], 0)

        mock_boto_client_instance.discover_instances.assert_called_once_with(
            NamespaceName="test-namespace", ServiceName="test-service"
        )

    @patch("boto3.client")
    def test_discover_instances_no_instances(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.discover_instances.return_value = {"Instances": []}

        aws_cloud_map = AWSCloudMap(
            region_name="us-east-1",
            namespace_name="test-namespace",
            service_name="test-service",
            aws_access_key_id="test-key-id",
            aws_secret_access_key="test-secret-key",
        )

        with self.assertRaises(Exception) as context:
            aws_cloud_map.discover_instances()

        self.assertEqual(str(context.exception), "No instances found")


if __name__ == "__main__":
    unittest.main()
