from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.stock.attachment_pb2 import Attachment as AttachmentProto
from peewee import CharField


class Attachment(BaseModel):
    doc_id = CharField()
    name = CharField()
    type = CharField()

    class Meta:
        table_name = "attachment"

    def to_proto(self) -> AttachmentProto:
        return AttachmentProto(
            id=self.id,
            doc_id=self.doc_id,
            name=self.name,
            type=self.type,
            object_audit=self.get_audit_proto(),
            active=self.active,
        )
