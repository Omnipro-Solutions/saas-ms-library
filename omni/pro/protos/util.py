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
