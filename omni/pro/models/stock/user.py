import grpc
from omni.pro.config import Config
from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.stock.user_pb2 import User as UserProto
from omni.pro.protos.v1.users import user_pb2, user_pb2_grpc
from peewee import CharField


class User(BaseModel):
    user_doc_id = CharField(unique=True)
    name = CharField()

    class Meta:
        table_name = "user"

    def to_proto(self):
        return UserProto(
            id=self.id,
            user_doc_id=self.user_doc_id,
            name=self.name,
            object_audit=self.get_audit_proto(),
            active=self.active,
        )

    def get_document_info(self, *args, **kwargs):
        with grpc.insecure_channel(f"{Config.USER_MS_HOST}:{Config.USER_MS_PORT}") as channel:
            stub = user_pb2_grpc.UsersServiceStub(channel)
            response = stub.UserRead(user_pb2.UserReadRequest(id=self.user_doc_id, **kwargs))
            return response.users[0] if response.users else None
