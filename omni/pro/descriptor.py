from enum import Enum

from mongoengine.fields import EmbeddedDocumentField, ReferenceField
from peewee import ForeignKeyField


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
    def describe_peewee_model(model):
        description = {
            "model": model.__name__,
            "class_name": f"{model.__module__}.{model.__name__}",
            "name": model.__name__.lower(),
            "fields": [],
        }
        for field_name, field in model._meta.fields.items():
            field_info = {
                "name": field_name,
                "code": field_name,
                "type": field.__class__.__name__,
                "size": field.max_length if hasattr(field, "max_length") else None,
                "required": not field.null,
                "relation": field.rel_model.__name__ if isinstance(field, ForeignKeyField) else None,
            }
            if hasattr(field, "choices") and field.choices:
                field_info["options"] = [option[0] for option in field.choices]
            description["fields"].append(field_info)
        return description
