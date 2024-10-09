import unittest
from unittest.mock import patch

from omni.pro.aws.s3 import AWSS3Client


class TestAWSS3Client(unittest.TestCase):

    @patch("boto3.client")
    def test_download_file(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.download_file.return_value = None

        s3_client = AWSS3Client(
            bucket_name="my-bucket",
            region_name="us-east-1",
            aws_access_key_id="fake-access-key",
            aws_secret_access_key="fake-secret-key",
            allowed_files=[".txt", ".png"],
        )

        result = s3_client.download_file("my-object.txt", "/tmp/my-object.txt")

        mock_boto_client_instance.download_file.assert_called_once_with(
            "my-bucket", "my-object.txt", "/tmp/my-object.txt"
        )
        self.assertIsNone(result)

    @patch("boto3.client")
    def test_upload_file(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.upload_file.return_value = None

        s3_client = AWSS3Client(
            bucket_name="my-bucket",
            region_name="us-east-1",
            aws_access_key_id="fake-access-key",
            aws_secret_access_key="fake-secret-key",
            allowed_files=[".txt", ".png"],
        )

        result = s3_client.upload_file("my-object.txt", "/tmp/my-object.txt")

        mock_boto_client_instance.upload_file.assert_called_once_with(
            "/tmp/my-object.txt", "my-bucket", "my-object.txt"
        )
        self.assertEqual(result, "my-object.txt")

    @patch("boto3.client")
    def test_generate_presigned_post(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.generate_presigned_post.return_value = {"url": "http://presigned-url"}

        s3_client = AWSS3Client(
            bucket_name="my-bucket",
            region_name="us-east-1",
            aws_access_key_id="fake-access-key",
            aws_secret_access_key="fake-secret-key",
            allowed_files=[".txt", ".png"],
        )

        presigned_post = s3_client.generate_presigned_post("my-object.txt")

        mock_boto_client_instance.generate_presigned_post.assert_called_once_with(
            "my-bucket", "my-object.txt", ExpiresIn=3600
        )
        self.assertEqual(presigned_post["url"], "http://presigned-url")

    @patch("boto3.client")
    def test_upload_file_to_s3_binary(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.put_object.return_value = None

        s3_client = AWSS3Client(
            bucket_name="my-bucket",
            region_name="us-east-1",
            aws_access_key_id="fake-access-key",
            aws_secret_access_key="fake-secret-key",
            allowed_files=[".txt", ".png"],
        )

        url = s3_client.upload_file_to_s3_binary("my-object.txt", "01101000011001010110110001101100", "text/plain")

        mock_boto_client_instance.put_object.assert_called_once_with(
            Bucket="my-bucket", Key="my-object.txt", Body=b"\x68\x65\x6c\x6c", ContentType="text/plain"
        )

        self.assertEqual(url, "https://my-bucket.s3.amazonaws.com/my-object.txt")

    @patch("boto3.client")
    def test_get_object_metadata(self, mock_boto_client):
        mock_boto_client_instance = mock_boto_client.return_value
        mock_boto_client_instance.head_object.return_value = {
            "ContentLength": 1234,
            "ContentType": "text/plain",
            "ETag": '"etag"',
            "LastModified": "2024-01-01T12:34:56",
        }

        s3_client = AWSS3Client(
            bucket_name="my-bucket",
            region_name="us-east-1",
            aws_access_key_id="fake-access-key",
            aws_secret_access_key="fake-secret-key",
            allowed_files=[".txt", ".png"],
        )

        metadata = s3_client.get_object_metadata("my-object.txt")

        mock_boto_client_instance.head_object.assert_called_once_with(Bucket="my-bucket", Key="my-object.txt")

        self.assertEqual(metadata["ContentLength"], 1234)
        self.assertEqual(metadata["ContentType"], "text/plain")
        self.assertEqual(metadata["ETag"], '"etag"')
        self.assertEqual(metadata["LastModified"], "2024-01-01T12:34:56")


if __name__ == "__main__":
    unittest.main()
