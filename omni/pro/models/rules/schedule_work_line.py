from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.rules.schedule_work_line_pb2 import ScheduleWorkLine as ScheduleWorkLineProto
from peewee import CharField, DateTimeField


class ScheduleWorkLine(BaseModel):
    DAY = (
        ("0", "monday"),
        ("1", "tuesday"),
        ("2", "wednesday"),
        ("3", "thursday"),
        ("4", "friday"),
        ("5", "saturday"),
        ("6", "sunday"),
    )
    day = CharField(choices=DAY)
    opening_time = DateTimeField()
    closing_time = DateTimeField()

    class Meta:
        table_name = "schedule_work_line"

    def to_proto(self):
        return ScheduleWorkLineProto(
            id=self.id,
            day=self.day,
            opening_time=self.opening_time,
            closing_time=self.closing_time,
            active=self.active,
            object_audit=self.object_audit.to_proto(),
        )
