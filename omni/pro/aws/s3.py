from botocore.config import Config
from omni.pro.aws.client import AWSClient


class AWSS3Client(AWSClient):
    def __init__(
        self,
        bucket_name: str,
        region_name: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        allowed_files: list,
        **kwargs,
    ) -> None:
        """
        Initializes a client for interacting with Amazon S3.

        :param bucket_name: str
        The name of the S3 bucket the client will access.

        :param region_name: str
        The region where the S3 bucket is hosted.

        :param aws_access_key_id: str
        The AWS access key ID.

        :param aws_secret_access_key: str
        The AWS secret access key.

        Additional kwargs are passed to the base class AWSClient constructor, allowing further configuration.
        """
        kwargs["config"] = Config(
            region_name=region_name, signature_version="v4", retries={"max_attempts": 10, "mode": "standard"}
        )
        self.bucket_name = bucket_name
        self.allowed_files = allowed_files
        super().__init__("s3", region_name, aws_access_key_id, aws_secret_access_key, **kwargs)

    def download_file(self, object_name: str, file_path: str):
        """
        Downloads a file from an S3 bucket.

        :param object_name: str
        The name of the object in S3 to be downloaded.

        :param file_path: str
        The path of the local file where the downloaded object will be saved.

        :return: None
        """
        result = self.client.download_file(self.bucket_name, object_name, file_path)
        return result

    def upload_file(self, object_name: str, file_path: str):
        """
        Uploads a file to an S3 bucket.

        :param file_path: str
        The path of the local file to be uploaded.

        :param object_name: str
        The name of the object in S3 to be uploaded.

        :return: None
        """
        self.client.upload_file(file_path, self.bucket_name, object_name)
        return object_name

    def generate_presigned_post(self, object_name: str):
        """
        Generate presigned post to upload file to an S3 bucket.

        :param object_name: str
        The name of the object in S3 to be uploaded.

        :return: presigned url
        """
        return self.client.generate_presigned_post(self.bucket_name, object_name, ExpiresIn=3600)

    def generate_presigned_url(self, object_name: str):
        """
        Generate presigned url to download file from an S3 bucket.

        :param object_name: str
        The name of the object in S3 to be uploaded.

        :return: presigned url
        """
        return self.client.generate_presigned_url("get_object", Params={"Bucket": self.bucket_name, "Key": object_name})
