from omni.pro.models.base import BaseModel
from omni.pro.models.sql.catalog.category import Category
from omni.pro.protos.v1.rules.delivery_category_pb2 import DeliveryCategory as DeliveryCategoryProto
from peewee import CharField, DeferredThroughModel, ManyToManyField


class DeliveryCategory(BaseModel):
    name = CharField()
    categ_ids = ManyToManyField(Category, backref="delivery_category_ids", through_model=DeferredThroughModel())

    class Meta:
        table_name = "delivery_category"

    def to_proto(self):
        return DeliveryCategoryProto(
            id=self.id,
            name=self.name,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
