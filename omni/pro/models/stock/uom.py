from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.stock.uom_pb2 import Uom as UomProto
from peewee import CharField


class Uom(BaseModel):
    uom_doc_id = CharField()
    code = CharField(unique=True)
    name = CharField()

    class Meta:
        table_name = "uom"

    def to_proto(self) -> UomProto:
        return UomProto(
            id=self.id,
            uom_doc_id=self.uom_doc_id,
            code=self.code,
            name=self.name,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
