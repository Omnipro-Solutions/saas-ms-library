from omni.pro.models.base import BaseModel
from omni.pro.models.sql.catalog.category import Category
from omni.pro.models.sql.rules.delivery_category import DeliveryCategoryCategory
from omni.pro.protos.v1.rules.delivery_category_category_pb2 import (
    DeliveryCategoryCategory as DeliveryCategoryCategoryProto,
)
from omni.pro.protos.v1.rules.delivery_category_pb2 import DeliveryCategory as DeliveryCategoryProto
from peewee import CharField, ForeignKeyField, ManyToManyField


class DeliveryCategory(BaseModel):
    name = CharField()
    categ_ids = ManyToManyField(Category, backref="delivery_category_ids", through_model=DeliveryCategoryCategory)

    class Meta:
        table_name = "delivery_category"

    def to_proto(self):
        return DeliveryCategoryProto(
            id=self.id,
            name=self.name,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )


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
            object_audit=self.object_audit.to_proto(),
        )
