from peewee import CharField

from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.stock.stock_pb2 import Warehouse as WarehouseProto


class Warehouse(BaseModel):
    name = CharField()
    code = CharField(unique=True)
    territory_matrix = CharField()
    address = CharField()
    complement = CharField()

    class Meta:
        table_name = "warehouse"

    def to_proto(self) -> WarehouseProto:
        warehouse_proto = WarehouseProto(
            object_audit=self.get_audit_proto(),
            id=self.id,
            name=self.name,
            code=self.code,
            territory_matrix=self.territory_matrix,
            address=self.address,
            complement=self.complement,
            active=self.active,
        )
        return warehouse_proto
