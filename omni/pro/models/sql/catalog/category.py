from omni.pro.models.base import BaseModel
from peewee import CharField, IntegerField


class Category(BaseModel):
    name = CharField()
    code = CharField()
    category_doc_id = CharField()

    class Meta:
        table_name = "category"
