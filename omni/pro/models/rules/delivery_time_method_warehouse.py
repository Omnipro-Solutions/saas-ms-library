from omni.pro.models.base import BaseModel
from omni.pro.models.rules.delivery_method_warehouse import DeliveryMethodWarehouse
from omni.pro.models.rules.delivery_time import DeliveryTime
from peewee import ForeignKeyField


# TODO tabla intermedia entre delivery_time y delivery_method_warehouse
class DeliveryTimeMethodWarehouse(BaseModel):
    delivery_time_id = ForeignKeyField(DeliveryTime, on_delete="RESTRICT")
    delivery_method_warehouse_id = ForeignKeyField(DeliveryMethodWarehouse, on_delete="RESTRICT")

    # def to_proto(self):
    #     return DeliveryTimeMethodWarehouseProto(
    #         id=self.id,
    #         delivery_time_id=self.delivery_time_id.id,
    #         delivery_method_warehouse_id=self.delivery_method_warehouse_id.id,
    #         active=self.active,
    #         object_audit=self.object_audit.to_proto(),
    #     )
