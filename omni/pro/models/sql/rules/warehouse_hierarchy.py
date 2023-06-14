from omni.pro.models.base import BaseModel
from omni.pro.models.stock.location import Location
from omni.pro.models.stock.warehouse import Warehouse
from omni.pro.protos.v1.rules.warehouse_hierarchy_pb2 import WarehouseHierarchy as WarehouseHierarchyProto
from peewee import BooleanField, CharField, FloatField, ForeignKeyField, IntegerField


class WarehouseHierarchy(BaseModel):
    warehouse_id = ForeignKeyField(Warehouse, on_delete="RESTRICT")
    location_id = ForeignKeyField(Location, on_delete="RESTRICT")
    quantity_security = FloatField()
    code = CharField()
    sequence = IntegerField()
    sequence_order = BooleanField()

    class Meta:
        table_name = "warehouse_hierarchy"

    def to_proto(self):
        return WarehouseHierarchyProto(
            id=self.id,
            warehouse_id=self.warehouse_id.id,
            location_id=self.location_id.id,
            quantity_security=self.quantity_security,
            code=self.code,
            sequence=self.sequence,
            sequence_order=self.sequence_order,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
