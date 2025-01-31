from botocore.config import Config
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
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

    def upload_file_to_s3_binary(self, object_name, file_content, content_type):
        """
        Uploads a binary file to an S3 bucket and returns the URL of the object.

        This function uploads a file directly from a binary object, such as a file read into memory or a data stream.
        This is useful for handling files that do not need to be saved to the local filesystem before being uploaded.

        :param object_name: The key under which the file will be stored in S3.
        :param file_content: The binary content of the file to upload.
        :param content_type: The MIME type of the file, which helps the browser to handle the file appropriately.

        :return: A URL to the uploaded file in the format "https://<bucket_name>.s3.amazonaws.com/<object_name>"

        :raises boto3.exceptions.S3UploadFailedError: If the upload to S3 fails.
        """
        try:
            binary_content = int(file_content, 2).to_bytes((len(file_content) + 7) // 8, byteorder="big")
            self._client.put_object(
                Bucket=self.bucket_name, Key=object_name, Body=binary_content, ContentType=content_type
            )
            url = f"https://{self.bucket_name}.s3.amazonaws.com/{object_name}"
            # url = self._client.generate_presigned_url(
            #     "get_object", Params={"Bucket": self.bucket_name, "Key": object_name}
            # )
            return url
        except (NoCredentialsError, PartialCredentialsError) as e:
            raise e

    def get_object_metadata(self, object_name):
        """
        Retrieves metadata for a specific object from the S3 bucket.

        This function fetches metadata for an object using the AWS S3 `head_object` API call,
        which provides information such as the object's size, MIME type, and the last modified timestamp,
        among other headers. This is useful for evaluating properties of the file without downloading it.

        :param object_name: The key of the object in the S3 bucket for which metadata is desired.

        :return: A dictionary containing the headers and metadata of the specified object. This includes,
                 but is not limited to, keys such as 'ContentLength', 'ContentType', 'ETag', and 'LastModified'.

        :raises ClientError: An error thrown by boto3's S3 client if the object is not found or the request fails
                             for some other reason. This could be due to a permissions issue, non-existent bucket or object, etc.
        """
        return self._client.head_object(Bucket=self.bucket_name, Key=object_name)

    def upload_fileobj(self, fileobj, object_name):
        """
        Uploads a file-like object to an S3 bucket.

        :param fileobj: A file-like object to be uploaded.
        :param object_name: The key under which the file will be stored in S3.
        :param content_type: The MIME type of the file, which helps the browser to handle the file appropriately.

        :return: A URL to the uploaded file in the format "https://<bucket_name>.s3.amazonaws.com/<object_name>"

        :raises boto3.exceptions.S3UploadFailedError: If the upload to S3 fails.
        """

        return self._client.upload_fileobj(fileobj, self.bucket_name, object_name)
