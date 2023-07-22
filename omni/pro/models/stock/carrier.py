from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.stock.carrier_pb2 import Carrier as CarrierProto
from peewee import CharField


class Carrier(BaseModel):
    name = CharField()
    code = CharField()

    class Meta:
        table_name = "carrier"

    def to_proto(self):
        return CarrierProto(
            id=self.id,
            name=self.name,
            object_audit=self.get_audit_proto(),
            active=self.active,
        )
