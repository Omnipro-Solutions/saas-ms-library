from omni.pro.models.base import BaseModel
from peewee import CharField


class Country(BaseModel):
    country_doc_id = CharField()
    name = CharField()
    code = CharField()

    class Meta:
        table_name = "country"
