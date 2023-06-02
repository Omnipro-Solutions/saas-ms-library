from omni.pro.models.base import BaseModel
from omni.pro.models.rules.delivery_time import DeliveryTime
from omni.pro.models.stock.warehouse import Warehouse
from peewee import ForeignKeyField


# TODO tabla intermedia entre delivery_time y warehouse
class DeliveryTimeWarehouse(BaseModel):
    delivery_time_id = ForeignKeyField(DeliveryTime, on_delete="RESTRICT")
    warehouse_id = ForeignKeyField(Warehouse, on_delete="RESTRICT")

    # def to_proto(self):
    #     return DeliveryTimeWarehouseProto(
    #         id=self.id,
    #         delivery_time_id=self.delivery_time_id.id,
    #         warehouse_id=self.warehouse_id.id,
    #         active=self.active,
    #         object_audit=self.object_audit.to_proto(),
    #     )
