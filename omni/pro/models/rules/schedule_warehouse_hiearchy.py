from omni.pro.models.base import BaseModel
from omni.pro.models.rules.delivery_schedule import DeliverySchedule
from omni.pro.models.rules.warehouse_hierarchy import WarehouseHierarchy
from omni.pro.protos.v1.rules.schedule_warehouse_hiearchy_pb2 import (
    ScheduleWarehouseHierarchy as ScheduleWarehouseHierarchyProto,
)
from peewee import CharField, FloatField, ForeignKeyField


# TODO tabla intermedia entre delivery_schedule y warehouse_hierarchy
class ScheduleWarehouseHierarchy(BaseModel):
    delivery_schedule_id = ForeignKeyField(DeliverySchedule, on_delete="RESTRICT")
    warehouse_hierarchy_id = ForeignKeyField(WarehouseHierarchy, on_delete="RESTRICT")

    def to_proto(self):
        return ScheduleWarehouseHierarchyProto(
            id=self.id,
            delivery_schedule_id=self.delivery_schedule_id.id,
            warehouse_hierarchy_id=self.warehouse_hierarchy_id.id,
            active=self.active,
            object_audit=self.object_audit.to_proto(),
        )
