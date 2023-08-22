from enum import Enum

from mongoengine.fields import EmbeddedDocumentField, ReferenceField
from sqlalchemy import inspect
from sqlalchemy.orm.relationships import RelationshipProperty


class Descriptor(object):
    @staticmethod
    def describe_mongo_model(model):
        description = {
            "model": model.__name__,
            "class_name": f"{model.__module__}.{model.__name__}",
            "name": model._meta.get("collection"),
            "fields": [],
        }
        for field_name, field in model._fields.items():
            field_info = {
                "name": field_name,
                "code": field_name,
                "type": field.__class__.__name__,
                "size": field.max_length if hasattr(field, "max_length") else None,
                "required": field.required,
                "relation": field.document_type.__name__ if isinstance(field, ReferenceField) else None,
            }

            # If the field is an EmbeddedDocumentField, get its fields as well
            if isinstance(field, EmbeddedDocumentField):
                embedded_model = field.document_type_obj
                embedded_fields = Descriptor.describe_mongo_model(embedded_model)
                field_info["embedded_fields"] = embedded_fields["fields"]

            # if the field is a Enum, add options values
            if hasattr(field, "choices") and field.choices:
                field_info["options"] = [x.value for x in field.choices]

            description["fields"].append(field_info)
        return description

    @staticmethod
    def describe_sqlalchemy_model(model):
        mapper = inspect(model)

        description = {
            "model": model.__name__,
            "class_name": f"{model.__module__}.{model.__name__}",
            "name": model.__name__.lower(),
            "fields": [],
        }

        for column in mapper.columns:
            column_info = {
                "name": column.name,
                "code": column.name,
                "type": column.type.__class__.__name__,
                "size": getattr(column.type, "length", None),
                "required": not column.nullable,
                "relation": None,
            }

            if column.foreign_keys:
                # Aquí solo se toma el primer ForeignKey, hay que modificarlo si puede haber múltiples referencias.
                related_model = list(column.foreign_keys)[0].column.table.name
                column_info["relation"] = related_model

            description["fields"].append(column_info)

        # Verificar relaciones (como many-to-one)
        for name, relation in mapper.relationships.items():
            if isinstance(relation, RelationshipProperty):
                relation_info = {
                    "name": name,
                    "code": name,
                    "type": "RelationshipProperty",
                    "size": None,
                    "required": not relation.uselist,  # True para many-to-one, False para many-to-many
                    "relation": relation.entity.class_.__name__,
                }
                description["fields"].append(relation_info)

        return description
