from omni.pro.models.base import BaseModel
from omni.pro.models.rules.delivery_locality import DeliveryLocality
from omni.pro.protos.v1.rules.delivery_locality_matrix_values_pb2 import (
    DeliveryLocalityMatrixValues as DeliveryLocalityMatrixValuesProto,
)
from peewee import CharField, ForeignKeyField


# TODO tabla intermedia entre delivery_locality y territory_matrix_values
class DeliveryLocalityTerritoryMatrixValues(BaseModel):
    delivery_locality_id = ForeignKeyField(DeliveryLocality, on_delete="RESTRICT")
    territory_matrix_values_id = CharField()

    def to_proto(self):
        return DeliveryLocalityMatrixValuesProto(
            id=self.id,
            delivery_locality_id=self.delivery_locality_id.id,
            territory_matrix_values_id=self.territory_matrix_values_id,
            active=self.active,
            object_audit=self.object_audit.to_proto(),
        )
