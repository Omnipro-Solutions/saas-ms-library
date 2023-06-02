from omni.pro.models.base import BaseModel
from omni.pro.models.rules.delivery_category import DeliveryCategory
from omni.pro.protos.v1.rules.delivery_category_category_pb2 import (
    DeliveryCategoryCategory as DeliveryCategoryCategoryProto,
)
from peewee import CharField, ForeignKeyField


# TODO tabla intermedia entre delivery_category y category
class DeliveryCategoryCategory(BaseModel):
    delivery_category_id = ForeignKeyField(DeliveryCategory, on_delete="RESTRICT")
    # TODO ID del documento de category en mongo
    category_id = CharField()

    def to_proto(self):
        return DeliveryCategoryCategoryProto(
            id=self.id,
            delivery_category_id=self.delivery_category_id.id,
            category_id=self.category_id,
            active=self.active,
            object_audit=self.object_audit.to_proto(),
        )
