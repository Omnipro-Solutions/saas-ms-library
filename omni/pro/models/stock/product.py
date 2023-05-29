from omni.pro.models.base import BaseModel
from peewee import CharField


class Product(BaseModel):
    product_doc_id = CharField()
    template_doc_id = CharField()
    name = CharField()

    class Meta:
        table_name = "product"

    def to_proto(self, proto_model):
        product_proto = super().to_proto(proto_model)
        product_proto.id = self.id
        product_proto.product_doc_id = self.product_doc_id
        product_proto.template_doc_id = self.template_doc_id
        product_proto.name = self.name
        return product_proto
