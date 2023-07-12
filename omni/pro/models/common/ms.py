from mongoengine import fields
from omni.pro.models.base import BaseDocument


class MicroService(BaseDocument):
    name = fields.StringField()
    code = fields.StringField()
    sumary = fields.StringField()
    description = fields.StringField()
    author = fields.StringField()
    category = fields.StringField()
    version = fields.StringField()
    depends = fields.ListField(fields.StringField())
    data = fields.ListField(fields.DictField())
