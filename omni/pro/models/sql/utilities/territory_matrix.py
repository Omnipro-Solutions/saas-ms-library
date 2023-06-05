from omni.pro.models.base import BaseModel
from peewee import CharField, IntegerField


class TerritoryMatrix(BaseModel):
    name = CharField()
    code = CharField()
    sequnce = IntegerField()

    class Meta:
        table_name = "territory_matrix"
