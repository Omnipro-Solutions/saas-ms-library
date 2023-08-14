import json
import typing
from collections import Counter

from bson.errors import InvalidId
from bson.objectid import ObjectId
from marshmallow import Schema, ValidationError, fields, missing, validates_schema
from marshmallow.exceptions import ValidationError


class ContextSchema(Schema):
    tenant = fields.String(required=True)
    user = fields.String(required=True)


class Context(Schema):
    context = fields.Nested(ContextSchema, required=True)


class BaseSchema(Context, Schema):
    active = fields.Boolean()


class PostgresBaseSchema(BaseSchema):
    def load(self, data, *args, **kwargs):
        data = super().load(data, *args, **kwargs)
        context = data.pop("context", {})
        data["tenant"] = context.get("tenant")
        data["updated_by"] = context.get("user")
        return data


class BaseObjectSchema(Schema):
    code = fields.String(required=True)
    code_name = fields.String(required=True)


def oid_isval(val: typing.Any) -> bool:
    """
    oid_isval [summary]

    Parameters
    ----------
    val : {Any}
        Value to be assessed if its an ObjectId

    Returns
    ----------
    val : bool
        True if val is an ObjectId, otherwise false
    """
    if ObjectId.is_valid(val):
        return val


def ensure_objid_type(val: typing.Union[bytes, str, ObjectId]) -> ObjectId:
    """
    Ensures that the value being passed is return as an ObjectId and is a valid ObjectId

    Parameters
    ----------
    val : Union[bytes, str, ObjectId]
        The value to be ensured or converted into an ObjectId and is a valid ObjectId

    Returns
    ----------
    val : ObjectId
        Value of type ObjectId

    Raises
    ----------
    ValidationError: Exception
        If it's not an ObjectId or can't be converted into an ObjectId, raise an error.

    """
    try:
        # If it's already an ObjectId and it's a valid ObjectId, return it
        if isinstance(val, ObjectId) and oid_isval(val):
            return val

        # Otherwise, if it's a bytes object, decode it and turn it into a string
        elif isinstance(val, bytes):
            val = ObjectId(str(val.decode("utf-8")))

        # Otherwise, if it's a string, turn it into an ObjectId and check that it's valid
        elif isinstance(val, str):
            val = ObjectId(val)

        # Check to see if the converted value is a valid objectId
        if oid_isval(val):
            return val
    except InvalidId as error:
        raise ValidationError(json.loads(json.dumps(f"{error}")))


class ObjectIdField(fields.Field):
    """Custom field for ObjectIds."""

    # Default error messages
    default_error_messages = {"invalid_ObjectId": "Not a valid ObjectId."}

    def _serialize(self, value, attr, obj, **kwargs) -> typing.Optional[ObjectId]:
        if value is None:
            return None
        return ensure_objid_type(value)

    def _deserialize(self, value, attr, data, **kwargs):
        if value is None:
            return missing
        if not isinstance(value, (ObjectId, str, bytes)):
            raise self.make_error("_deserialize: Not a invalid ObjectId")
        try:
            return ensure_objid_type(value)
        except UnicodeDecodeError as error:
            raise self.make_error("invalid_utf8") from error
        except (ValueError, AttributeError, TypeError) as error:
            raise ValidationError("ObjectIds must be a 12-byte input or a 24-character hex string") from error


class MicroServiceValidator(Context, Schema):
    name = fields.String(required=True)
    code = fields.String(required=True)
    tenant_code = fields.String(required=True)
    description = fields.String(required=True)
    version = fields.String(required=True)
    author = fields.String(required=True)
    summary = fields.String(required=True)
    category = fields.String(required=True)
    depends = fields.List(fields.String())
    data = fields.List(fields.String())

    def __init__(self, base_app, micro_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_app = base_app
        self.micro_data = micro_data

    @validates_schema
    def validate_data(self, data, *args, **kwargs):
        if elt := self._duplicate_elements(data.get("data", [])):
            raise ValidationError(f"Duplicate elements in data {elt}")
        list_path = []
        for path in data.get("data", []):
            file = self.base_app / path
            if not file.exists():
                list_path.append(path)
        if list_path:
            raise ValidationError(f"File not found {list_path}")

    def _duplicate_elements(self, data):
        return [item for item, count in Counter(data).items() if count > 1]

    def load(self, data, *args, **kwargs):
        data = super().load(data, *args, **kwargs)
        list_dict = []
        for path in data.get("data", []):
            md = next((x for x in self.micro_data if x.get("path") == path), None)
            if not md:
                list_dict.append({"path": path, "load": False})
        data["data"] = self.micro_data + list_dict
        return data
