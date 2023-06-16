from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.schedule_work import ScheduleWork
from omni.pro.models.sql.rules.schedule_work_line import ScheduleWorkLine
from omni.pro.protos.v1.rules.schedule_work_schedule_work_line_pb2 import (
    ScheduleWorkScheduleWorkLine as ScheduleWorkScheduleWorkLineProto,
)
from peewee import DeferredThroughModel, ForeignKeyField


# TODO tabla intermedia entre schedule_work y schedule_work_line
class ScheduleWorkScheduleWorkLine(BaseModel):
    schedule_work_id = ForeignKeyField(ScheduleWork, on_delete="RESTRICT")
    schedule_work_line_id = ForeignKeyField(ScheduleWorkLine, on_delete="RESTRICT")

    def to_proto(self):
        return ScheduleWorkScheduleWorkLineProto(
            id=self.id,
            schedule_work_id=self.schedule_work_id.id,
            schedule_work_line_id=self.schedule_work_line_id.id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )

    class Meta:
        table_name = "schedule_work_schedule_work_line"


DeferredThroughModel.set_model(ScheduleWork.schedule_work_lines_ids, ScheduleWorkScheduleWorkLine)
