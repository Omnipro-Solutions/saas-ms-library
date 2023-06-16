from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.delivery_locality import DeliveryLocality
from omni.pro.models.sql.utilities.territory_matrix_values import TerritoryMatrixValues
from omni.pro.protos.v1.rules.delivery_locality_matrix_values_pb2 import (
    DeliveryLocalityMatrixValues as DeliveryLocalityMatrixValuesProto,
)
from peewee import DeferredThroughModel, ForeignKeyField


# TODO tabla intermedia entre delivery_locality y territory_matrix_values
class DeliveryLocalityTerritoryMatrixValues(BaseModel):
    delivery_locality_id = ForeignKeyField(DeliveryLocality, on_delete="RESTRICT")
    territory_matrix_values_id = ForeignKeyField(TerritoryMatrixValues, on_delete="RESTRICT")

    def to_proto(self):
        return DeliveryLocalityMatrixValuesProto(
            id=self.id,
            delivery_locality_id=self.delivery_locality_id.id,
            territory_matrix_values_id=self.territory_matrix_values_id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )

    class Meta:
        table_name = "delivery_locality_territory_matrix_values"


DeferredThroughModel.set_model(DeliveryLocality.territory_matrix_values_ids, DeliveryLocalityTerritoryMatrixValues)
