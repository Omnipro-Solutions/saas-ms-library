from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.schedule_work import ScheduleWork
from omni.pro.models.sql.rules.warehouse_hierarchy import WarehouseHierarchy
from omni.pro.protos.v1.rules.delivery_schedule_pb2 import DeliverySchedule as DeliveryScheduleProto
from omni.pro.protos.v1.rules.delivery_schedule_warehouse_hierarchy_pb2 import (
    DeliveryScheduleWarehouseHierarchy as DeliveryScheduleWarehouseHierarchyProto,
)
from peewee import CharField, DeferredThroughModel, ForeignKeyField, ManyToManyField


class DeliverySchedule(BaseModel):
    name = CharField()
    schedule_work_id = ForeignKeyField(ScheduleWork, on_delete="RESTRICT")
    transfer_warehouse_ids = ManyToManyField(
        WarehouseHierarchy, backref="transfer_warehouse_ids", through_model=DeferredThroughModel()
    )

    def to_proto(self):
        return DeliveryScheduleProto(
            id=self.id,
            name=self.name,
            schedule_work_id=self.schedule_work_id.id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
