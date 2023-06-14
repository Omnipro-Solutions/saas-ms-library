from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.calendar import Calendar
from omni.pro.models.sql.rules.schedule_work_line import ScheduleWorkLine
from omni.pro.protos.v1.rules.schedule_work_pb2 import ScheduleWork as ScheduleWorkProto
from omni.pro.protos.v1.rules.schedule_work_schedule_work_line_pb2 import (
    ScheduleWorkScheduleWorkLine as ScheduleWorkScheduleWorkLineProto,
)
from peewee import CharField, DeferredThroughModel, ForeignKeyField, ManyToManyField


class ScheduleWork(BaseModel):
    name = CharField()
    calendar_id = ForeignKeyField(Calendar, on_delete="RESTRICT")
    schedule_work_lines_ids = ManyToManyField(
        ScheduleWorkLine, backref="schedule_work_lines_ids", through_model=DeferredThroughModel()
    )

    class Meta:
        table_name = "schedule_work"

    def to_proto(self):
        return ScheduleWorkProto(
            id=self.id,
            name=self.name,
            calendar_id=self.calendar_id.id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
