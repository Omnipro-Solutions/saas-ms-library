## Saas MS Library

Saas MS Library is a Python library designed to be a utility for OMS microservices. This library provides an easy-to-use and highly customizable solution for reusing application utilities and clients, allowing developers to focus on creating the most efficient and scalable microservice.

With Saas MS Library, you will be able to handle AWS databases and clients. Our library is compatible with Python 3.10 and later versions, and is under constant development to improve its performance and extend its functionality.

#### Features
1. Database Handler (MongoDB, Redis, PostgreSQL, etc.)
2. AWS Client Handler (Cognito, S3, etc.)
3. Decorators

#### Installation
To install saas-ms-library, simply run the following command:
```
pip install saas-ms-library

```

#### Examples of use
Here are some examples of how to use saas-ms-library in your projects:

Create environment variables
```
GRPC_PORT=50051
GRPC_MAX_WORKERS=10
SERVICE_ID=saas-ms-user
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0
```
Use
```
from protos.v1.users import user_pb2, user_pb2_grpc
from omni.pro.decorators import resources_decorator
from omni.pro.util import HTTPStatus, Resource, deep_search, nested


class  UserService(user_pb2_grpc.UsersServiceServicer):
    @resources_decorator([Resource.AWS_COGNITO, Resource.MONGODB])
    def  UserCreate(
        self, request: user_pb2.UserCreateRequest, context
        ) -> user_pb2.UserCreateResponse:
            response = context.cognito_client.create_user(
                username=data["username"],
                password=data["password"],
                name=data["name"],
                email=data["email"],
                tenant=data["tenant"],
                language_code=data["language"]["code"],
                timezone_code=data["timezone"]["code"],
            )
            att_list = nested(response, "User.Attributes") or  nested(response, "UserAttributes", default=[])
            sub_dict = deep_search(att_list, key, value)
            user = context.db_manager.get_document(
                context.db_name, UserDocument, sub=sub_dict.get("Value")
            )
            return  user_pb2.UserCreateResponse(
                response_standard=base_pb2.ResponseStandard(
                    success=True,
                    message="User created",
                    status_code=HTTPStatus.CREATED
                ),
                user=user.to_proto(),
            )
```

#### License
Saas MS Library is licensed under the modified MIT License.


