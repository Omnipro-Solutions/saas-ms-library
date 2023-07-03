from peewee import CharField

from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.stock.picking_pb2 import ProcurementGroup as ProcurementGroupProto


class ProcurementGroup(BaseModel):
    name = CharField()
    move_type = CharField()

    class Meta:
        table_name = "procurement_group"

    def to_proto(self):
        return ProcurementGroupProto(
            id=self.id,
            name=self.name,
            move_type=self.move_type,
            object_audit=self.get_audit_proto(),
            active=self.active,
        )
