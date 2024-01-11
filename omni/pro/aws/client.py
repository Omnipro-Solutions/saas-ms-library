import boto3


class AWSClient(object):
    def __init__(
        self, service_name: str, region_name: str, aws_access_key_id: str, aws_secret_access_key: str, **kwargs
    ) -> None:
        """
        :type service_name: str
        :param service_name: AWS service name
        :type region_name: str
        :param region_name: AWS region name
        :type aws_access_key_id: str
        :param aws_access_key_id: AWS access key id
        :type aws_secret_access_key: str
        :param aws_secret_access_key: AWS secret access key
        Example:
            service_name = "service_name"
            region_name = "us-east-1"
            aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"
            aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        """
        self._client = boto3.client(
            service_name=service_name,
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            **kwargs,
        )

    def get_client(self):
        return self._client

    client = property(get_client)
