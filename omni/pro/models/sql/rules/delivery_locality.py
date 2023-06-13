from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.delivery_locality import DeliveryLocalityTerritoryMatrixValues
from omni.pro.models.sql.utilities.country import Country
from omni.pro.models.sql.utilities.territory_matrix import TerritoryMatrix
from omni.pro.models.sql.utilities.territory_matrix_values import TerritoryMatrixValues
from omni.pro.protos.v1.rules.delivery_locality_matrix_values_pb2 import (
    DeliveryLocalityMatrixValues as DeliveryLocalityMatrixValuesProto,
)
from omni.pro.protos.v1.rules.delivery_locality_pb2 import DeliveryLocality as DeliveryLocalityProto
from peewee import CharField, ForeignKeyField, ManyToManyField


class DeliveryLocality(BaseModel):
    name = CharField()
    country_id = ForeignKeyField(Country, on_delete="RESTRICT")
    territory_matrix_id = ForeignKeyField(TerritoryMatrix, on_delete="RESTRICT")
    territory_matrix_values_ids = ManyToManyField(
        TerritoryMatrixValues,
        backref="territory_matrix_values_ids",
        through_model=DeliveryLocalityTerritoryMatrixValues,
    )

    class Meta:
        table_name = "delivery_locality"

    def to_proto(self):
        return DeliveryLocalityProto(
            id=self.id,
            name=self.name,
            country_id=self.country_id.id,
            territory_matrix_id=self.territory_matrix_id.id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )


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
            object_audit=self.object_audit.to_proto(),
        )
