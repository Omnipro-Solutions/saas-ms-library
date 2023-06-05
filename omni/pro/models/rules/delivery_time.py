from omni.pro.models.base import BaseModel
from omni.pro.models.rules.delivery_locality import DeliveryLocality
from peewee import BooleanField, CharField, ForeignKeyField, IntegerField


class DeliveryTime(BaseModel):
    TIME_TYPE = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
    )
    name = CharField()
    locality_available_id = ForeignKeyField(DeliveryLocality, on_delete="RESTRICT")
    time_type = CharField(choices=TIME_TYPE)
    value_min = IntegerField()
    value_max = IntegerField()
    inversely = BooleanField()

    class Meta:
        table_name = "delivery_time"

    # def to_proto(self):
    #     return DeliveryTimeProto(
    #         id=self.id,
    #         name=self.name,
    #         locality_available_id=self.locality_available_id.id,
    #         time_type=self.time_type,
    #         value_min=self.value_min,
    #         value_max=self.value_max,
    #         inversely=self.inversely,
    #         active=self.active,
    #         object_audit=self.object_audit.to_proto(),
    #     )
