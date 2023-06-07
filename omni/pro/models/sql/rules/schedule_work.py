from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.calendar import Calendar
from omni.pro.protos.v1.rules.schedule_work_pb2 import ScheduleWork as ScheduleWorkProto
from peewee import CharField, ForeignKeyField


class ScheduleWork(BaseModel):
    name = CharField()
    calendar_id = ForeignKeyField(Calendar, on_delete="RESTRICT")

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
