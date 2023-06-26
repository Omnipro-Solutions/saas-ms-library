from peewee import CharField

from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.stock.picking_pb2 import User as UserProto


class User(BaseModel):
    user_doc_id = CharField()
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
