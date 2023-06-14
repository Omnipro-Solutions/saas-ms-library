from omni.pro.models.base import BaseModel
from omni.pro.models.sql.catalog.category import Category
from omni.pro.models.sql.rules.delivery_category import DeliveryCategory
from omni.pro.protos.v1.rules.delivery_category_category_pb2 import (
    DeliveryCategoryCategory as DeliveryCategoryCategoryProto,
)
from peewee import ForeignKeyField

# TODO tabla intermedia entre delivery_category y category


class DeliveryCategoryCategory(BaseModel):
    delivery_category_id = ForeignKeyField(DeliveryCategory, on_delete="RESTRICT")
    category_id = ForeignKeyField(Category, on_delete="RESTRICT")

    def to_proto(self):
        return DeliveryCategoryCategoryProto(
            id=self.id,
            delivery_category_id=self.delivery_category_id.id,
            category_id=self.category_id.id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )

    class Meta:
        table_name = "delivery_category_category"
