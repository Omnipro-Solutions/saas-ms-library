from google.protobuf import json_format


def MessageToDict(message, **kwargs):
    return json_format.MessageToDict(message, preserving_proto_field_name=True, **kwargs)