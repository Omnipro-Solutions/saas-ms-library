from google.protobuf import json_format


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


def format_request(data, request, proto) -> object:
    return json_format.ParseDict(data, getattr(proto, request)())
