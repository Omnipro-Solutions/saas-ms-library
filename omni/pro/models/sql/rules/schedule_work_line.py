from google.protobuf.timestamp_pb2 import Timestamp
from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.rules.schedule_work_line_pb2 import ScheduleWorkLine as ScheduleWorkLineProto
from peewee import CharField, DateTimeField


class ScheduleWorkLine(BaseModel):
    DAY = (
        (0, "monday"),
        (1, "tuesday"),
        (2, "wednesday"),
        (3, "thursday"),
        (4, "friday"),
        (5, "saturday"),
        (6, "sunday"),
    )
    day = CharField(choices=DAY)
    opening_time = DateTimeField()
    closing_time = DateTimeField()

    class Meta:
        table_name = "schedule_work_line"

    def to_proto(self):
        opening_time = Timestamp()
        opening_time.FromDatetime(self.opening_time)
        closing_time = Timestamp()
        closing_time.FromDatetime(self.closing_time)

        return ScheduleWorkLineProto(
            id=self.id,
            day=self.day,
            opening_time=opening_time,
            closing_time=closing_time,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
