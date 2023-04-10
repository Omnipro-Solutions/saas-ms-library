import boto3
from omni.pro.util import HTTPStatus, generate_strong_password, nested


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


class AWSCognitoClient(AWSClient):
    def __init__(
        self, region_name: str, aws_access_key_id: str, aws_secret_access_key: str, user_pool_id: str, **kwargs
    ) -> None:
        """
        :type user_pool_id: str
        :param user_pool_id: AWS user pool id
        :type client_id: str
        :param client_id: AWS client id
        Example:
            service_name = "cognito-idp"
            region_name = "us-east-1"
            user_pool_id = "us-east-1_123456789"
            client_id = "1234567890123456789012"
        """
        super().__init__(
            service_name="cognito-idp",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            **kwargs,
        )
        self.user_pool_id = user_pool_id

    def get_user(self, username: str) -> dict:
        return self.client.admin_get_user(UserPoolId=self.user_pool_id, Username=username)

    def create_user(
        self, username: str, password: str, name: str, email: str, tenant: str, language_code: str, timezone_code: str
    ) -> dict:
        response = self.client.admin_create_user(
            UserPoolId=self.user_pool_id,
            Username=username,
            TemporaryPassword=generate_strong_password(),
            UserAttributes=[
                {"Name": "name", "Value": name},
                {"Name": "email", "Value": email},
                {"Name": "custom:tenant", "Value": tenant},
                {"Name": "locale", "Value": language_code},
                {"Name": "zoneinfo", "Value": timezone_code},
            ],
        )
        self.set_user_password(username=username, password=password)
        return True, response

    def delete_user(self, username: str) -> dict:
        return self.client.admin_delete_user(UserPoolId=self.user_pool_id, Username=username)

    def set_user_password(self, username: str, password: str) -> None:
        self.client.admin_set_user_password(
            UserPoolId=self.user_pool_id, Username=username, Password=password, Permanent=True
        )

    def update_user(self, username: str, name: str, language_code: str, timezone_code: str) -> dict:
        response = self.client.admin_update_user_attributes(
            UserPoolId=self.user_pool_id,
            Username=username,
            UserAttributes=[
                {"Name": "name", "Value": name},
                {"Name": "locale", "Value": language_code},
                {"Name": "zoneinfo", "Value": timezone_code},
            ],
        )
        return nested(response, "ResponseMetadata.HTTPStatusCode") == HTTPStatus.OK, response

    def list_users(self, filter: str, limit: int, offset: int, pagination_token: str = None) -> dict:
        paginator = self.client.get_paginator("list_users")
        pag_config = {"MaxItems": int(limit), "PageSize": int(offset)}
        if pagination_token:
            pag_config["StartingToken"] = pagination_token
        page_iterator = paginator.paginate(
            UserPoolId=self.user_pool_id,
            Filter=f'name ^= "{filter}"',
            PaginationConfig=pag_config,
        )
        starting_token = None
        first_page = True
        list_user = []
        for page in page_iterator:
            users = page["Users"]
            if first_page:
                first_page = False
            else:
                if not starting_token:
                    starting_token = page.get("PaginationToken")

            for user in users:
                list_user.append(user)
        return list_user, starting_token


class S3Client(AWSClient):
    def __init__(
        self, service_name: str, region_name: str, aws_access_key_id: str, aws_secret_access_key: str, **kwargs
    ) -> None:
        super().__init__(service_name, region_name, aws_access_key_id, aws_secret_access_key, **kwargs)
