from botocore.exceptions import ClientError
from omni.pro.aws.client import AWSClient
from omni.pro.util import HTTPStatus, generate_strong_password, nested


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

    def sign_out(self, access_token):
        try:
            result = self.get_client().global_sign_out(
                AccessToken=access_token,
            )
            return HTTPStatus.OK, result
        except ClientError as e:
            if e.response["Error"]["Code"] == "NotAuthorizedException":
                return HTTPStatus.UNAUTHORIZED, "Invalid access token"
        except Exception as e:
            return HTTPStatus.INTERNAL_SERVER_ERROR, str(e)

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
