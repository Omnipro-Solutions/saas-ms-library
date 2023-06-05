from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.rules.delivery_category_pb2 import DeliveryCategory as DeliveryCategoryProto
from peewee import CharField


class DeliveryCategory(BaseModel):
    name = CharField()

    class Meta:
        table_name = "delivery_category"

    def to_proto(self):
        return DeliveryCategoryProto(
            id=self.id,
            name=self.name,
            active=self.active,
            object_audit=self.object_audit.to_proto(),
        )
