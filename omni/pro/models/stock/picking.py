from google.protobuf.timestamp_pb2 import Timestamp
from omni.pro.models.base import BaseModel
from omni.pro.models.stock.attachment import Attachment
from omni.pro.models.stock.carrier import Carrier
from omni.pro.models.stock.location import Location
from omni.pro.models.stock.picking_type import PickingType
from omni.pro.models.stock.procurement_group import ProcurementGroup
from omni.pro.models.stock.user import User
from omni.pro.protos.v1.stock.picking_pb2 import Picking as PickingProto
from peewee import CharField, DateTimeField, DecimalField, ForeignKeyField


class Picking(BaseModel):
    name = CharField()
    picking_type_id = ForeignKeyField(PickingType, on_delete="PROTECT")
    location_id = ForeignKeyField(Location, on_delete="PROTECT")
    location_dest_id = ForeignKeyField(Location, on_delete="PROTECT")
    user_id = ForeignKeyField(User, on_delete="PROTECT")
    attachment_guide_id = ForeignKeyField(Attachment, on_delete="PROTECT")
    attachment_invoice_id = ForeignKeyField(Attachment, on_delete="PROTECT")
    origin = CharField()
    date_done = DateTimeField(null=True, default=None)
    scheduled_date = DateTimeField()
    time_total_preparation = DecimalField()
    time_assigned = DecimalField()
    carrier_id = ForeignKeyField(Carrier, on_delete="PROTECT")
    date_delivery = DateTimeField(null=True, default=None)
    carrier_tracking_ref = CharField()
    group_id = ForeignKeyField(ProcurementGroup, on_delete="PROTECT")
    weight = DecimalField()
    shipping_weight = DecimalField()

    class Meta:
        table_name = "picking"

    def to_proto(self):
        date_done = None
        if self.date_done:
            date_done = Timestamp()
            date_done.FromDatetime(self.date_done)
            self.date_done = date_done
        scheduled_date = Timestamp()
        scheduled_date.FromDatetime(self.scheduled_date)
        date_delivery = Timestamp()
        date_delivery.FromDatetime(self.date_delivery)

        return PickingProto(
            name=self.name,
            picking_type_id=self.picking_type_id.id,
            location_id=self.location_id.id,
            location_dest_id=self.location_dest_id.id,
            user_id=self.user_id.id,
            attachment_guide_id=self.attachment_guide_id.id,
            attachment_invoice_id=self.attachment_invoice_id.id,
            origin=self.origin,
            date_done=self.date_done,
            scheduled_date=scheduled_date,
            time_total_preparation=self.time_total_preparation,
            time_assigned=self.time_assigned,
            carrier_id=self.carrier_id.id,
            date_delivery=date_delivery,
            carrier_tracking_ref=self.carrier_tracking_ref,
            group_id=self.group_id.id,
            weight=self.weight,
            shipping_weight=self.shipping_weight,
            active=self.active,
            object_audit=self.get_audit_proto(),
        )
