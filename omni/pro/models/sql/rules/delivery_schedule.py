from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.delivery_schedule import ScheduleWarehouseHierarchy
from omni.pro.models.sql.rules.schedule_work import ScheduleWork
from omni.pro.models.sql.rules.warehouse_hierarchy import WarehouseHierarchy
from omni.pro.protos.v1.rules.delivery_schedule_pb2 import DeliverySchedule as DeliveryScheduleProto
from omni.pro.protos.v1.rules.delivery_schedule_warehouse_hierarchy import (
    DeliveryScheduleWarehouseHierarchy as DeliveryScheduleWarehouseHierarchyProto,
)
from peewee import CharField, ForeignKeyField, ManyToManyField


class DeliverySchedule(BaseModel):
    name = CharField()
    schedule_work_id = ForeignKeyField(ScheduleWork, on_delete="RESTRICT")
    transfer_warehouse_ids = ManyToManyField(
        WarehouseHierarchy, backref="transfer_warehouse_ids", through_model=ScheduleWarehouseHierarchy
    )

    def to_proto(self):
        return DeliveryScheduleProto(
            id=self.id,
            name=self.name,
            schedule_work_id=self.schedule_work_id.id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )


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
            object_audit=self.object_audit.to_proto(),
        )

    class Meta:
        table_name = "delivery_schedule_warehouse_hierarchy"
