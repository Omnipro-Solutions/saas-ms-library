from omni.pro.models.base import BaseModel
from omni.pro.protos.v1.stock.product_pb2 import Product as ProductProto
from peewee import CharField


class Product(BaseModel):
    product_doc_id = CharField()
    template_doc_id = CharField()
    name = CharField()

    class Meta:
        table_name = "product"

    def to_proto(self) -> ProductProto:
        return ProductProto(
            id=self.id,
            product_doc_id=self.product_doc_id,
            template_doc_id=self.template_doc_id,
            name=self.name,
            object_audit=self.get_audit_proto(),
            active=self.active,
        )
