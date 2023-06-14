from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.warehouse_hierarchy import WarehouseHierarchy
from omni.pro.protos.v1.rules.delivery_method_warehouse_pb2 import (
    DeliveryMethodWarehouse as DeliveryMethodWarehouseProto,
)
from peewee import CharField, DeferredThroughModel, ManyToManyField


class DeliveryMethodWarehouse(BaseModel):
    HIERARCHY_WAREHOUSE_SORT = (
        ("0", "asc"),
        ("1", "desc"),
    )
    name = CharField()
    hierarchy_warehouse_sort = CharField(choices=HIERARCHY_WAREHOUSE_SORT)
    transfer_warehouse_ids = ManyToManyField(
        WarehouseHierarchy, backref="transfer_warehouse_ids", through_model=DeferredThroughModel()
    )

    class Meta:
        table_name = "delivery_method_warehouse"

    def to_proto(self):
        return DeliveryMethodWarehouseProto(
            id=self.id,
            name=self.name,
            hierarchy_warehouse_sort=self.hierarchy_warehouse_sort,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
