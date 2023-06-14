from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.delivery_method import DeliveryMethod
from omni.pro.models.stock.warehouse import Warehouse
from omni.pro.protos.v1.rules.delivery_warehouse_ref_pb2 import DeliveryWarehouseRef as DeliveryWarehouseRefProto
from peewee import DeferredThroughModel, ForeignKeyField


# TODO tabla intermedia entre delivery_method y warehouse
class DeliveryWarehouseRef(BaseModel):
    delivery_method_id = ForeignKeyField(DeliveryMethod, on_delete="RESTRICT")
    warehouse_id = ForeignKeyField(Warehouse, on_delete="RESTRICT")

    def to_proto(self):
        return DeliveryWarehouseRefProto(
            id=self.id,
            delivery_method_id=self.delivery_method_id.id,
            warehouse_id=self.warehouse_id.id,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )

    class Meta:
        table_name = "delivery_warehouse_ref"


DeferredThroughModel.set_model(DeliveryMethod.delivery_warehouse_ids, DeliveryWarehouseRef)
