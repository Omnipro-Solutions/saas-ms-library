from peewee import CharField

from omni.pro.models.base import BaseModel
from omni.pro.protos.common.country_pb2 import Country as CountryProto


class Country(BaseModel):
    country_doc_id = CharField()
    name = CharField(max_length=100)
    code = CharField(unique=True)

    class Meta:
        table_name = "country"

    def to_proto(self) -> CountryProto:
        return CountryProto(
            id=self.id,
            country_doc_id=self.country_doc_id,
            name=self.name,
            code=self.code,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
