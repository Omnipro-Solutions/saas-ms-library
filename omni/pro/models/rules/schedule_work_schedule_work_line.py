from omni.pro.models.base import BaseModel
from omni.pro.models.rules.schedule_work import ScheduleWork
from omni.pro.models.rules.schedule_work_line import ScheduleWorkLine
from omni.pro.protos.v1.rules.schedule_work_schedule_work_line_pb2 import (
    ScheduleRef as ScheduleWorkScheduleWorkLineProto,
)
from peewee import ForeignKeyField


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
            object_audit=self.object_audit.to_proto(),
        )
