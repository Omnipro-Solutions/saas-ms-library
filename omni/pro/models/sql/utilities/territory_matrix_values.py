from omni.pro.models.base import BaseModel
from peewee import CharField, ForeignKeyField, IntegerField


class TerritoryMatrixValues(BaseModel):
    name = CharField()
    code = CharField()
    values = ForeignKeyField("self", backref="child_values", null=True)

    class Meta:
        table_name = "territory_matrix_values"
