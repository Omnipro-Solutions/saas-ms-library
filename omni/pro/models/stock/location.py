from omni.pro.models.base import BaseModel
from omni.pro.models.stock.warehouse import Warehouse
from omni.pro.protos.v1.stock.stock_pb2 import Location as LocationProto
from peewee import BooleanField, CharField, ForeignKeyField


class Location(BaseModel):
    name = CharField()
    code = CharField()
    parent_id = ForeignKeyField("self", backref="children", null=True)
    type_location = CharField()
    barcode = CharField()
    warehouse_id = ForeignKeyField(Warehouse, backref="locations")
    active = BooleanField()

    class Meta:
        table_name = "location"

    def to_proto(self):
        parent_id = self.parent_id.id if self.parent_id else None
        return LocationProto(
            id=self.id,
            name=self.name,
            code=self.code,
            parent_id=parent_id,
            type_location=self.type_location,
            barcode=self.barcode,
            warehouse_id=self.warehouse_id.id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
