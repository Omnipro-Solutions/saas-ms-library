from google.protobuf import struct_pb2
from omni.pro.models.base import BaseModel
from omni.pro.models.sql.utilities.country import Country
from omni.pro.protos.v1.stock.warehouse_pb2 import Warehouse as WarehouseProto
from peewee import CharField, ForeignKeyField
from playhouse.postgres_ext import JSONField


class Warehouse(BaseModel):
    name = CharField()
    code = CharField(unique=True)
    country_id = ForeignKeyField(Country, backref="warehouses", on_delete="RESTRICT")
    territory_matrix_value = JSONField()
    address = CharField()
    complement = CharField()

    class Meta:
        table_name = "warehouse"

    def struct_to_proto(self, data: dict) -> struct_pb2.Struct:
        """
        struct_to_proto [converts a python dict to a google protobuf struct]

        Parameters
        ----------
        struct : dict
            python dict

        Returns
        -------
        struct_pb2.Struct
            Google protobuf struct
        """
        struct = struct_pb2.Struct()
        if data:
            struct.update(data)
        return struct

    def to_proto(self) -> WarehouseProto:
        warehouse_proto = WarehouseProto(
            object_audit=self.get_audit_proto(),
            id=self.id,
            name=self.name,
            code=self.code,
            country_id=self.country_id.id,
            territory_matrix_value=self.struct_to_proto(self.territory_matrix_value),
            address=self.address,
            complement=self.complement,
            active=self.active,
        )
        return warehouse_proto
