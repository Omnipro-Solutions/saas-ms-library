from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.delivery_schedule import DeliverySchedule
from omni.pro.models.sql.rules.warehouse_hierarchy import WarehouseHierarchy
from omni.pro.protos.v1.rules.delivery_schedule_warehouse_hierarchy_pb2 import (
    DeliveryScheduleWarehouseHierarchy as DeliveryScheduleWarehouseHierarchyProto,
)
from peewee import CharField, DeferredThroughModel, ForeignKeyField, ManyToManyField


# TODO tabla intermedia entre delivery_schedule y warehouse_hierarchy
class ScheduleWarehouseHierarchy(BaseModel):
    delivery_schedule_id = ForeignKeyField(DeliverySchedule, on_delete="RESTRICT")
    warehouse_hierarchy_id = ForeignKeyField(WarehouseHierarchy, on_delete="RESTRICT")

    def to_proto(self):
        return DeliveryScheduleWarehouseHierarchyProto(
            id=self.id,
            delivery_schedule_id=self.delivery_schedule_id.id,
            warehouse_hierarchy_id=self.warehouse_hierarchy_id.id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )

    class Meta:
        table_name = "delivery_schedule_warehouse_hierarchy"


DeferredThroughModel.set_model(DeliverySchedule.transfer_warehouse_ids, ScheduleWarehouseHierarchy)
