from mongoengine import DynamicEmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField, ReferenceField
from omni.pro.models.base import BaseModel
from omni.pro.util import to_camel_case
from sqlalchemy import Enum, inspect
from sqlalchemy.orm.relationships import RelationshipProperty


class Descriptor(object):
    @staticmethod
    def describe_mongo_model(model, prefix_name="", prefix_code="", depth=0, max_depth=2):
        """
        Describe the structure of a MongoDB model using its fields.

        Describir la estructura de un modelo de MongoDB usando sus campos.

        Parameters:
        ----------
        model : object
            MongoDB model to be described.
            Modelo de MongoDB a describir.

        prefix_name : str, optional
            Prefix for the field's display name.
            Prefijo para el nombre de visualización del campo. (default is "")

        prefix_code : str, optional
            Prefix for the field's code reference.
            Prefijo para la referencia de código del campo. (default is "")

        Returns:
        -------
        dict or list
            If it's a top-level call, returns a dictionary describing the main model.
            If it's a recursive call, returns a list describing the fields of an embedded or referenced model.

            Si es una llamada de nivel superior, devuelve un diccionario que describe el modelo principal.
            Si es una llamada recursiva, devuelve una lista que describe los campos de un modelo incrustado o referenciado.

        Usage:
        -----
        descriptor = Descriptor()
        description = descriptor.describe_mongo_model(SomeMongoModel)

        Uso:
        -----
        descriptor = Descriptor()
        descripcion = descriptor.describe_mongo_model(AlgúnModeloMongo)
        """
        fields = []

        for field_name, field in model._fields.items():
            current_name = (prefix_name + " " + to_camel_case(field_name)).strip()
            current_code = (prefix_code + "." + field_name).strip(".")

            field_info = {
                "name": current_name,
                "code": current_code,
                "type": Descriptor.get_equivalent_field(field.__class__.__name__),
                "class_type": field.__class__.__name__,
                "required": field.required,
                "is_filterable": field.is_filterable if hasattr(field, "is_filterable") else True,
                "is_exportable": field.is_exportable if hasattr(field, "is_exportable") else True,
                "is_importable": field.is_importable if hasattr(field, "is_importable") else True,
                "relation": {},
            }
            if hasattr(field, "max_length") and field.max_length:
                field_info["size"] = field.max_length

            # If the field is an EmbeddedDocumentField or ReferenceField, recurse into its fields
            if isinstance(field, EmbeddedDocumentField) or isinstance(field, ReferenceField):
                if depth < max_depth:
                    embedded_model = field.document_type_obj
                    try:
                        embedded_fields = Descriptor.describe_mongo_model(
                            embedded_model, current_name, current_code, depth=depth + 1, max_depth=max_depth
                        )
                    except RecursionError as e:
                        print(f"Model: {model.__name__} RecursionError: {e}")
                        continue
                    fields.extend(embedded_fields)  # extend main fields list with the result of recursion
                    continue  # we don't add a separate field for the embedded/reference field itself

            # if the field is an Enum, add options values
            if hasattr(field, "choices") and field.choices:
                field_info["options"] = [{"code": x.value, "name": to_camel_case(x.value)} for x in field.choices]

            fields.append(field_info)

        if model._dynamic:
            return [
                {
                    "name": prefix_name,
                    "code": prefix_code,
                    "type": Descriptor.get_equivalent_field("DynamicField"),
                    "class_type": "DynamicField",
                    "required": False,
                    "relation": {},
                }
            ] + fields

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
        """
        Describe the structure of an SQLAlchemy model using its columns and relationships.

        Describir la estructura de un modelo SQLAlchemy usando sus columnas y relaciones.

        Parameters:
        ----------
        model : object
            SQLAlchemy model to be described.
            Modelo SQLAlchemy a describir.

        Returns:
        -------
        dict
            Dictionary describing the given SQLAlchemy model including its fields and relationships.

            Diccionario que describe el modelo SQLAlchemy dado incluyendo sus campos y relaciones.

        Usage:
        -----
        descriptor = Descriptor()
        description = descriptor.describe_sqlalchemy_model(SomeSQLAlchemyModel)

        Uso:
        -----
        descriptor = Descriptor()
        descripcion = descriptor.describe_sqlalchemy_model(AlgúnModeloSQLAlchemy)
        """
        mapper = inspect(model)

        description = {
            "name": model.__name__,
            "class_name": f"{model.__module__}.{model.__name__}",
            "code": mapper.mapped_table.name,
            "fields": [],
            "is_replic": model.__is_replic_table__,
        }

        for column in mapper.columns:
            Descriptor.set_extra_attribute(column, "is_filterable")
            Descriptor.set_extra_attribute(column, "is_exportable")
            Descriptor.set_extra_attribute(column, "is_importable")

            column_info = {
                "name": to_camel_case(column.name),
                "code": column.name,
                "type": Descriptor.get_equivalent_field(column.type.__class__.__name__),
                "class_type": column.type.__class__.__name__,
                "required": not column.nullable,
                "is_filterable": column.is_filterable,
                "is_exportable": column.is_exportable,
                "is_importable": column.is_importable,
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
                    "class_type": Descriptor.get_equivalent_field("RelationshipProperty"),
                    "required": not relation.uselist,  # True para many-to-one, False para many-to-many
                    "relation": {"name": relation.entity.class_.__name__},
                    "is_exportable": False,
                    "is_importable": False,
                }
                description["fields"].append(relation_info)

        return description

    @staticmethod
    def describe_mongo_model_tree(model):
        """
        Describe the hierarchical structure of a MongoDB model, including embedded or referenced models.

        Describir la estructura jerárquica de un modelo MongoDB, incluyendo modelos incrustados o referenciados.

        Parameters:
        ----------
        model : object
            MongoDB model to be described hierarchically.
            Modelo de MongoDB a describir jerárquicamente.

        Returns:
        -------
        dict
            Dictionary describing the given MongoDB model in a hierarchical manner including its fields,
            relations, and embedded/referenced models.

            Diccionario que describe el modelo MongoDB dado de manera jerárquica, incluyendo sus campos,
            relaciones y modelos incrustados/referenciados.

        Usage:
        -----
        descriptor = Descriptor()
        description = descriptor.describe_mongo_model_tree(SomeMongoModel)

        Uso:
        -----
        descriptor = Descriptor()
        descripcion = descriptor.describe_mongo_model_tree(AlgúnModeloMongo)
        """
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
                "type": Descriptor.get_equivalent_field(field.__class__.__name__),
                "class_type": field.__class__.__name__,
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

    @staticmethod
    def get_equivalent_field(field: str) -> str:
        field_names = {
            # mongo field name
            "StringField": "string",
            "URLField": "url",
            "EmailField": "email",
            "IntField": "integer",
            "LongField": "integer",
            "FloatField": "float",
            "DecimalField": "decimal",
            "BooleanField": "boolean",
            "DateTimeField": "datetime",
            "DateField": "date",
            "ComplexDateTimeField": "complex_datetime",
            "EmbeddedDocumentField": "embedded_document",
            "ObjectIdField": "object_id",
            "GenericEmbeddedDocumentField": "generic_embedded_document",
            "DynamicField": "dynamic",
            "ListField": "list",
            "SortedListField": "sorted_list",
            "EmbeddedDocumentListField": "embedded_document_list",
            "DictField": "json",
            "MapField": "json",
            "ReferenceField": "reference",
            "CachedReferenceField": "cached_reference",
            "LazyReferenceField": "lazy_reference",
            "GenericLazyReferenceField": "genericlazy_reference",
            "GenericReferenceField": "generic_reference",
            "BinaryField": "binary",
            "FileField": "file",
            "ImageField": "image",
            "GeoPointField": "geo_point",
            "PointField": "point",
            "LineStringField": "line_string",
            "PolygonField": "polygon",
            "SequenceField": "sequence",
            "UUIDField": "uuid",
            "EnumField": "enum",
            "MultiPointField": "multi_point",
            "MultiLineStringField": "multi_line_string",
            "MultiPolygonField": "multi_polygon",
            "GeoJsonBaseField": "geo_json_base",
            "Decimal128Field": "decimal128",
            # mongo relationship name
            "RelationshipProperty": "relationship",
            # sqlalchemy field name
            "String": "string",
            "Text": "text",
            "Unicode": "unicode",
            "UnicodeText": "unicode",
            "Integer": "integer",
            "SmallInteger": "integer",
            "BigInteger": "integer",
            "Numeric": "numeric",
            "Float": "float",
            "Double": "double",
            "DateTime": "datetime",
            "Date": "date",
            "Time": "time",
            "LargeBinary": "binary",
            "Enum": "enum",
            "Boolean": "boolean",
            "Interval": "interval",
            "JSON": "json",
            "ARRAY": "array",
            "REAL": "float",
            "FLOAT": "float",
            "DOUBLE": "double",
            "DOUBLE_PRECISION": "double",
            "NUMERIC": "decimal",
            "DECIMAL": "decimal",
            "INTEGER": "integer",
            "SMALLINT": "integer",
            "BIGINT": "integer",
            "TIMESTAMP": "timestamp",
            "DATETIME": "datetime",
            "DATE": "date",
            "TIME": "time",
            "TEXT": "text",
            "CLOB": "text",
            "VARCHAR": "string",
            "NVARCHAR": "string",
            "CHAR": "string",
            "NCHAR": "string",
            "BLOB": "binary",
            "BINARY": "binary",
            "VARBINARY": "binary",
            "BOOLEAN": "boolean",
            "Uuid": "uuid",
            "UUID": "uuid",
        }
        return field_names[field]

    @staticmethod
    def set_extra_attribute(column, attribute, default=True):
        if not hasattr(column, attribute):
            if column.name in BaseModel.__annotations__.keys():
                default = getattr(getattr(BaseModel, column.name).column, attribute)
            setattr(column, attribute, default)
