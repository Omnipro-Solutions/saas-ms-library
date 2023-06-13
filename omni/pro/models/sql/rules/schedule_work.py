from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.calendar import Calendar
from omni.pro.models.sql.rules.schedule_work import ScheduleWorkScheduleWorkLine
from omni.pro.models.sql.rules.schedule_work_line import ScheduleWorkLine
from omni.pro.protos.v1.rules.schedule_work_pb2 import ScheduleWork as ScheduleWorkProto
from omni.pro.protos.v1.rules.schedule_work_schedule_work_line_pb2 import (
    ScheduleRef as ScheduleWorkScheduleWorkLineProto,
)
from peewee import CharField, ForeignKeyField, ManyToManyField


class ScheduleWork(BaseModel):
    name = CharField()
    calendar_id = ForeignKeyField(Calendar, on_delete="RESTRICT")
    schedule_work_lines_ids = ManyToManyField(
        ScheduleWorkLine, backref="schedule_work_lines_ids", through_model=ScheduleWorkScheduleWorkLine
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
