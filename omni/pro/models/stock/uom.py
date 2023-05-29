from omni.pro.models.base import BaseModel
from peewee import CharField


class Uom(BaseModel):
    uom_doc_id = CharField()
    code = CharField(unique=True)
    name = CharField()

    class Meta:
        table_name = "uom"

    def to_proto(self, proto_model):
        uom_proto = super().to_proto(proto_model)
        uom_proto.id = self.id
        uom_proto.uom_doc_id = self.uom_doc_id
        uom_proto.code = self.code
        uom_proto.name = self.name
        return uom_proto
