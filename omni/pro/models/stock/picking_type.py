from omni.pro.models.base import BaseModel
from omni.pro.models.stock.location import Location
from omni.pro.models.stock.uom import Uom as Uom
from omni.pro.models.stock.warehouse import Warehouse
from omni.pro.protos.v1.stock.picking_type_pb2 import PickingType as PickingTypeProto
from peewee import BooleanField, CharField, ForeignKeyField, IntegerField


class PickingType(BaseModel):
    name = CharField()
    sequence_code = CharField()
    warehouse_id = ForeignKeyField(Warehouse, backref="picking_types")
    code = CharField(unique=True)
    return_picking_type_id = ForeignKeyField("self", backref="children", null=True)
    show_operations = BooleanField(default=False)
    show_reserved = BooleanField(default=False)
    default_location_src_id = ForeignKeyField(Location)
    default_location_dest_id = ForeignKeyField(Location)
    prefix = CharField()
    padding = IntegerField()
    number_increment = IntegerField()
    number_next_actual = IntegerField()

    class Meta:
        table_name = "picking_type"

    def to_proto(self):
        return_picking_type_id = self.return_picking_type_id.id if self.return_picking_type_id else None
        return PickingTypeProto(
            id=self.id,
            name=self.name,
            sequence_code=self.sequence_code,
            warehouse_id=self.warehouse_id.id,
            code=self.code,
            return_picking_type_id=return_picking_type_id,
            show_operations=self.show_operations,
            show_reserved=self.show_reserved,
            default_location_dest_id=self.default_location_dest_id.id,
            default_location_src_id=self.default_location_src_id.id,
            prefix=self.prefix,
            padding=self.padding,
            number_increment=self.number_increment,
            number_next_actual=self.number_next_actual,
            object_audit=self.get_audit_proto(),
            active=self.active,
        )
