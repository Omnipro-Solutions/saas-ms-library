from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.rules.calendar_pb2 import Calendar as CalendarProto
from peewee import CharField


class Calendar(BaseModel):
    name = CharField()

    class Meta:
        table_name = "calendar"

    def to_proto(self):
        return CalendarProto(
            id=self.id,
            name=self.name,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
