from omni.pro.models.base import BaseModel
from omni.pro.models.rules.delivery_method import DeliveryMethod
from omni.pro.models.rules.delivery_time import DeliveryTime
from peewee import ForeignKeyField


# TODO tabla intermedia entre delivery_method y delivery_time
class DeliveryTimeMethod(BaseModel):
    delivery_method_id = ForeignKeyField(DeliveryMethod, on_delete="RESTRICT")
    delivery_time_id = ForeignKeyField(DeliveryTime, on_delete="RESTRICT")

    # def to_proto(self):
    #     return DeliveryTimeMethodProto(
    #         id=self.id,
    #         delivery_method_id=self.delivery_method_id.id,
    #         delivery_time_id=self.delivery_time_id.id,
    #         active=self.active,
    #         object_audit=self.object_audit.to_proto(),
    #     )
