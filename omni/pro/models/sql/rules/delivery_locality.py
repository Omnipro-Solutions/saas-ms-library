from omni.pro.models.base import BaseModel

# from omni.pro.models.sql.rules.delivery_locality_territory_matrix_values import DeliveryLocalityTerritoryMatrixValues
from omni.pro.models.sql.utilities.country import Country
from omni.pro.models.sql.utilities.territory_matrix import TerritoryMatrix
from omni.pro.models.sql.utilities.territory_matrix_values import TerritoryMatrixValues
from omni.pro.protos.v1.rules.delivery_locality_pb2 import DeliveryLocality as DeliveryLocalityProto
from peewee import CharField, DeferredThroughModel, ForeignKeyField, ManyToManyField


class DeliveryLocality(BaseModel):
    name = CharField()
    country_id = ForeignKeyField(Country, on_delete="RESTRICT")
    territory_matrix_id = ForeignKeyField(TerritoryMatrix, on_delete="RESTRICT")
    territory_matrix_values_ids = ManyToManyField(
        TerritoryMatrixValues,
        backref="territory_matrix_values_ids",
        through_model=DeferredThroughModel(),
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
