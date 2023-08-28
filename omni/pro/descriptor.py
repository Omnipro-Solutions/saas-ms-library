from mongoengine.fields import EmbeddedDocumentField, ReferenceField
from omni.pro.util import to_camel_case
from sqlalchemy import Enum, inspect
from sqlalchemy.orm.relationships import RelationshipProperty


class Descriptor(object):
    @staticmethod
    def describe_mongo_model(model, prefix_name="", prefix_code=""):
        fields = []

        for field_name, field in model._fields.items():
            current_name = (prefix_name + " " + to_camel_case(field_name)).strip()
            current_code = (prefix_code + "." + field_name).strip(".")

            field_info = {
                "name": current_name,
                "code": current_code,
                "type": field.__class__.__name__,
                "required": field.required,
                "relation": {},
            }
            if hasattr(field, "max_length") and field.max_length:
                field_info["size"] = field.max_length

            # If the field is an EmbeddedDocumentField or ReferenceField, recurse into its fields
            if isinstance(field, EmbeddedDocumentField) or isinstance(field, ReferenceField):
                embedded_model = field.document_type_obj
                embedded_fields = Descriptor.describe_mongo_model(embedded_model, current_name, current_code)
                fields.extend(embedded_fields)  # extend main fields list with the result of recursion
                continue  # we don't add a separate field for the embedded/reference field itself

            # if the field is an Enum, add options values
            if hasattr(field, "choices") and field.choices:
                field_info["options"] = [{"code": x.value, "name": to_camel_case(x.value)} for x in field.choices]

            fields.append(field_info)

        if prefix_name == "" and prefix_code == "":  # This is a top-level call
            return {
                "name": model.__name__,
                "class_name": f"{model.__module__}.{model.__name__}",
                "code": model._meta.get("collection") or model.__name__.lower(),
                "fields": fields,
            }
        else:  # This is a recursive call
            return fields

    @staticmethod
    def describe_sqlalchemy_model(model):
        mapper = inspect(model)

        description = {
            "name": model.__name__,
            "class_name": f"{model.__module__}.{model.__name__}",
            "code": mapper.mapped_table.name,
            "fields": [],
        }

        for column in mapper.columns:
            column_info = {
                "name": to_camel_case(column.name),
                "code": column.name,
                "type": column.type.__class__.__name__,
                "required": not column.nullable,
            }
            if hasattr(column.type, "length") and column.type.length:
                column_info["size"] = column.type.length

            if isinstance(column.type, Enum):
                column_info["options"] = [
                    {"code": x.value, "name": to_camel_case(x.value)} for x in column.type.enum_class
                ]

            if column.foreign_keys:
                # Aquí solo se toma el primer ForeignKey, hay que modificarlo si puede haber múltiples referencias.
                related_model = list(column.foreign_keys)[0].column.table.name
                column_info["relation"] = {"name": related_model}
            # column_info["relation"] = {}

            description["fields"].append(column_info)

        # Verificar relaciones (como many-to-one)
        for name, relation in mapper.relationships.items():
            if isinstance(relation, RelationshipProperty):
                relation_info = {
                    "name": name,
                    "code": name,
                    "type": "RelationshipProperty",
                    "required": not relation.uselist,  # True para many-to-one, False para many-to-many
                    "relation": {"name": relation.entity.class_.__name__},
                }
                description["fields"].append(relation_info)

        return description

    @staticmethod
    def describe_mongo_model_tree(model):
        description = {
            "name": model.__name__,
            "class_name": f"{model.__module__}.{model.__name__}",
            "code": model._meta.get("collection") or model.__name__.lower(),
            "fields": [],
        }
        for field_name, field in model._fields.items():
            field_info = {
                "name": to_camel_case(field_name),
                "code": field_name,
                "type": field.__class__.__name__,
                "required": field.required,
                # "relation": field.document_type.__name__ if isinstance(field, ReferenceField) else {},
                "relation": {},
            }
            if hasattr(field, "max_length") and field.max_length:
                field_info["size"] = field.max_length

            # If the field is an EmbeddedDocumentField, get its fields as well
            if isinstance(field, EmbeddedDocumentField) or isinstance(field, ReferenceField):
                # field_info["fields"] = Descriptor.describe_mongo_model_tree(field.document_type)["fields"]
                embedded_model = field.document_type_obj
                embedded_fields = Descriptor.describe_mongo_model_tree(embedded_model)
                field_info["relation"] = embedded_fields

            # if the field is a Enum, add options values
            if hasattr(field, "choices") and field.choices:
                field_info["options"] = [x.value for x in field.choices]

            description["fields"].append(field_info)

        return description
