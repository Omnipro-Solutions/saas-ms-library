import datetime
import importlib
from datetime import datetime

from google.protobuf import json_format, struct_pb2
from pymongo.cursor import Cursor


# FIXME: change param including_default_value_fields to default_values when invoking util.MessageToDict
def MessageToDict(message, default_values=False, including_default_value_fields=False, **kwargs):
    """
    Converts protobuf message to a JSON dictionary considering the preserving proto field names.
    @param message: The protobuf message to convert.
    @param default_values: If True, fields with default values will be included in the dictionary.
    @param kwargs: Additional arguments to pass to json_format.MessageToDict.
    @return: The JSON dictionary.
    """
    return json_format.MessageToDict(
        message,
        preserving_proto_field_name=True,
        including_default_value_fields=default_values or including_default_value_fields,
        **kwargs,
    )


def format_request(data, request, proto, **kwargs) -> object:
    return json_format.ParseDict(data, getattr(proto, request)(), **kwargs)


def to_value(obj):
    """
    Use condictional expression to convert a object to a `Value`.
    """
    if isinstance(obj, dict):
        if "_id" in obj:
            obj["id"] = obj.pop("_id")
        return struct_pb2.Value(struct_value=to_struct(obj))
    elif isinstance(obj, list) or isinstance(obj, Cursor):
        return struct_pb2.Value(list_value=to_list_value(obj))
    elif isinstance(obj, bool):
        return struct_pb2.Value(bool_value=obj)
    elif isinstance(obj, int) or isinstance(obj, float):
        return struct_pb2.Value(number_value=obj)
    elif obj is None:
        return struct_pb2.Value(null_value=struct_pb2.NullValue.NULL_VALUE)
    else:
        return struct_pb2.Value(string_value=str(obj))


def to_struct(d):
    return struct_pb2.Struct(fields={k: to_value(v) for k, v in d.items()})


def to_list_value(lst):
    """Converts a list of dictionaries to a `ListValue`.

    Args:
      lst: A list of dictionaries.

    Returns:
      A `ListValue`.
    """
    return struct_pb2.ListValue(values=[to_value(x) for x in lst])


def format_datetime_to_iso(datetime_obj: datetime):
    """
    Convert a datetime object to ISO 8601 format ('YYYY-MM-DDTHH:MM:SSZ').

    Args:
        datetime_obj (datetime.datetime): The datetime object to be formatted.

    Returns:
        str:
            A string representing the datetime in ISO 8601 format.

    Example:
        # Convert a datetime object to ISO 8601 format
        dt = datetime.datetime(2023, 8, 22, 14, 30, 0)
        formatted_datetime = format_datetime_to_iso(dt)
        print(formatted_datetime)
    """
    formatted_datetime = datetime_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
    return formatted_datetime


def model_to_proto(model, fields, serialize_proto=None, **kwargs):
    """
    Converts a model instance to its corresponding protocol buffer (protobuf) representation.

    This function takes an instance of a model and a list of field names, and uses a serialization
    prototype (serialize_proto) to generate a corresponding protobuf object. The prototype is dynamically
    imported based on the provided name.

    Args:
        model (BaseModel):
            The model instance to be converted. This can be any object with accessible attributes.
        fields (list of str):
            A list of field names (strings) that will be copied from the model to the protobuf object.
        serialize_proto (str):
            The full name of the protobuf prototype to be used for serialization. This name is used
            to dynamically import the corresponding protobuf class.
        **kwargs:
            Additional arguments that can be passed to handle specific cases or advanced configurations
            in the serialization process.

    Returns:
        An instance of the protobuf prototype with the model fields assigned.

    Example:
        # Example of converting a model to a protobuf object
        class MyModel:
            name = "test"
            age = 25

        model_instance = MyModel()
        proto_obj = model_to_proto(model_instance, ["name", "age"], "my_package.MyProto")
        print(proto_obj)
    """
    proto_class_name = serialize_proto.split(".")[-1]
    serialize_proto = getattr(
        importlib.import_module("omni.pro.protos.{0}".format(serialize_proto.split(f".{proto_class_name}")[0])),
        proto_class_name,
    )
    if model:
        return serialize_proto(**{key: getattr(model, key) for key in fields})
