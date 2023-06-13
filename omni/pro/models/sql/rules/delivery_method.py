from omni.pro.models.base import BaseModel
from omni.pro.models.sql.rules.delivery_category import DeliveryCategory
from omni.pro.models.sql.rules.delivery_locality import DeliveryLocality
from omni.pro.models.sql.rules.delivery_method_warehouse import DeliveryMethodWarehouse
from omni.pro.models.sql.rules.delivery_schedule import DeliverySchedule
from omni.pro.models.stock.location import Location
from omni.pro.models.stock.warehouse import Warehouse
from omni.pro.protos.v1.rules.delivery_method_pb2 import DeliveryMethod as DeliveryMethodProto
from peewee import CharField, DeferredThroughModel, FloatField, ForeignKeyField, ManyToManyField


class DeliveryMethod(BaseModel):
    TYPE_PICKING_TRANSFER = (
        (0, "PARTIAL"),
        (1, "CONSOLIDATED"),
    )
    VALIDATED_PICKING_CODE = (
        (0, "OPTIONAL"),
        (1, "REQUIRED"),
        (2, "UNNECESSARY"),
    )
    TYPE_DELIVERY = (
        (0, "STORE"),
        (1, "SHIPPING"),
    )
    name = CharField()
    type_picking_transfer = CharField(choices=TYPE_PICKING_TRANSFER)
    validate_warehouse_code = CharField(choices=VALIDATED_PICKING_CODE)
    quantity_security = FloatField()
    code = CharField()
    type_delivery = CharField(choices=TYPE_DELIVERY)
    delivery_location_id = ForeignKeyField(Location, on_delete="RESTRICT")
    transfer_template_id = ForeignKeyField(DeliveryMethodWarehouse, on_delete="RESTRICT")
    category_template_id = ForeignKeyField(DeliveryCategory, on_delete="RESTRICT")
    local_available_id = ForeignKeyField(DeliveryLocality, on_delete="RESTRICT")
    schedule_template_id = ForeignKeyField(DeliverySchedule, on_delete="RESTRICT")
    delivery_warehouse_ids = ManyToManyField(
        Warehouse, backref="delivery_warehouse_ids", through_model=DeferredThroughModel()
    )

    class Meta:
        table_name = "delivery_method"

    def to_proto(self):
        return DeliveryMethodProto(
            id=self.id,
            name=self.name,
            type_picking_transfer=self.type_picking_transfer,
            validate_warehouse_code=self.validate_warehouse_code,
            quantity_security=self.quantity_security,
            code=self.code,
            type_delivery=self.type_delivery,
            delivery_location_id=self.delivery_location_id.id,
            transfer_template_id=self.transfer_template_id.id,
            category_template_id=self.category_template_id.id,
            locality_available_id=self.locality_available_id.id,
            schedule_template_id=self.schedule_template_id.id,
            delivery_warehouse_ids=[warehouse.id for warehouse in self.delivery_warehouse_ids],
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
