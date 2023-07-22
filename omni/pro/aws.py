import boto3
from botocore.exceptions import ClientError
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
        self,
        region_name: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        user_pool_id: str,
        client_id: str,
        **kwargs,
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
        self.client_id = client_id

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
        return response

    def delete_user(self, username: str) -> dict:
        return self.client.admin_delete_user(UserPoolId=self.user_pool_id, Username=username)

    def set_user_password(self, username: str, password: str) -> None:
        self.client.admin_set_user_password(
            UserPoolId=self.user_pool_id, Username=username, Password=password, Permanent=True
        )

    def update_user(self, username: str, name: str, language_code: str, timezone_code: str) -> dict:
        return self._update_attributes(
            username=username,
            attributes=[
                {"Name": "name", "Value": name},
                {"Name": "locale", "Value": language_code},
                {"Name": "zoneinfo", "Value": timezone_code},
            ],
        )

    def update_email(self, username, email: str) -> dict:
        return self._update_attributes(username=username, attributes=[{"Name": "email", "Value": email}])

    def _update_attributes(self, username: str, attributes: list) -> dict:
        response = self.client.admin_update_user_attributes(
            UserPoolId=self.user_pool_id,
            Username=username,
            UserAttributes=attributes,
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

    def init_auth(self, username: str, password: str) -> dict:
        auth_result = {}
        status_code = HTTPStatus.BAD_REQUEST
        message = ""
        try:
            result = self.get_client().initiate_auth(
                ClientId=self.client_id,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": username,
                    "PASSWORD": password,
                },
            )
        except ClientError as e:
            if e.response["Error"]["Code"] == "NotAuthorizedException":
                status_code = HTTPStatus.UNAUTHORIZED
                message = "Invalid auth data"
            elif e.response["Error"]["Code"] == "InvalidParameterException":
                status_code = HTTPStatus.BAD_REQUEST
                message = "Missing or empty parameters in request"
            else:
                status_code = HTTPStatus.UNAUTHORIZED
                message = str(e)
        else:
            message = "Success"
            status_code = HTTPStatus.OK
            auth_result = {
                "token": result["AuthenticationResult"]["IdToken"],
                "refresh_token": result["AuthenticationResult"]["RefreshToken"],
                "expires_in": result["AuthenticationResult"]["ExpiresIn"],
            }

        return status_code, auth_result, message

    def refresh_token(self, refresh_token):
        auth_result = {}
        status_code = HTTPStatus.BAD_REQUEST
        message = ""
        try:
            new_tokens_response = self.get_client().initiate_auth(
                ClientId=self.client_id,
                AuthFlow="REFRESH_TOKEN_AUTH",
                AuthParameters={"REFRESH_TOKEN": refresh_token},
            )
        except ClientError as e:
            status_code = HTTPStatus.UNAUTHORIZED
            if e.response["Error"]["Code"] == "NotAuthorizedException":
                message = "Invalid refresh token"
            else:
                message = str(e)
        else:
            status_code = HTTPStatus.OK
            message = "Success"
            auth_result = {
                "token": new_tokens_response["AuthenticationResult"]["IdToken"],
                "expires_in": new_tokens_response["AuthenticationResult"]["ExpiresIn"],
            }
        return status_code, auth_result, message


class S3Client(AWSClient):
    def __init__(
        self, service_name: str, region_name: str, aws_access_key_id: str, aws_secret_access_key: str, **kwargs
    ) -> None:
        super().__init__(service_name, region_name, aws_access_key_id, aws_secret_access_key, **kwargs)


class AWSCloudMap(AWSClient):
    def __init__(
        self,
        region_name: str,
        namespace_name: str,
        service_name: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        **kwargs,
    ):
        super().__init__(
            service_name="servicediscovery",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            **kwargs,
        )
        self.namespace_name = namespace_name
        self.service_name = service_name

    def discover_instances(self):
        response = self.client.discover_instances(
            NamespaceName=self.namespace_name,
            ServiceName=self.service_name,
        )
        if not response.get("Instances"):
            raise Exception("No instances found")

        return response.get("Instances")

    def get_redis_config(self):
        instances = self.discover_instances()
        instance = instances[0]
        return {
            "host": instance.get("Attributes").get("host"),
            "port": int(instance.get("Attributes").get("port") or 6379),
            "db": int(instance.get("Attributes").get("db") or 0),
        }
