from omni.pro.models.base import BaseModel
from omni.pro.models.rules.delivery_method_warehouse import DeliveryMethodWarehouse
from omni.pro.models.rules.warehouse_hierarchy import WarehouseHierarchy
from omni.pro.protos.v1.rules.delivery_method_warehouse_hierarchy_pb2 import (
    DeliveryMethodWarehouseHierarchy as DeliveryMethodWarehouseHierarchyProto,
)
from peewee import CharField, FloatField, ForeignKeyField

# TODO tabla intermedia entre delivery_method y warehouse_hierarchy


class DeliveryMethodWarehouseHierarchy(BaseModel):
    delivery_method_warehouse_id = ForeignKeyField(DeliveryMethodWarehouse, on_delete="RESTRICT")
    warehouse_hierarchy_id = ForeignKeyField(WarehouseHierarchy, on_delete="RESTRICT")

    def to_proto(self):
        return DeliveryMethodWarehouseHierarchyProto(
            id=self.id,
            delivery_method_warehouse_id=self.delivery_method_warehouse_id.id,
            warehouse_hierarchy_id=self.warehouse_hierarchy_id.id,
            active=self.active,
            object_audit=self.object_audit.to_proto(),
        )
