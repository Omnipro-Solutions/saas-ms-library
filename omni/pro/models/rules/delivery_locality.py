from omni.pro.models.base import BaseModel
from omni.pro.models.utilities.country import Country
from omni.pro.protos.v1.rules.delivery_locality_pb2 import DeliveryLocality as DeliveryLocalityProto
from peewee import CharField, ForeignKeyField


class DeliveryLocality(BaseModel):
    name = CharField()
    # TODO ID del documento de country en mongo
    country_id = CharField()
    territory_matrix_id = ForeignKeyField("self", on_delete="RESTRICT")

    class Meta:
        table_name = "delivery_locality"

    def to_proto(self):
        return DeliveryLocalityProto(
            id=self.id,
            name=self.name,
            country_id=self.country_id,
            territory_matrix_id=self.territory_matrix_id.id,
            active=self.active,
            object_audit=self.object_audit.to_proto(),
        )
