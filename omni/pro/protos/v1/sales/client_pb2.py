# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/sales/client.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni.pro.protos.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15v1/sales/client.proto\x12 pro.omni.oms.api.v1.sales.client\x1a\x11\x63ommon/base.proto"\x8a\x01\n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rclient_doc_id\x18\x03 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x04 \x01(\x08\x12?\n\x0cobject_audit\x18\x05 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"r\n\x13\x43lientCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rclient_doc_id\x18\x02 \x01(\t\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9b\x01\n\x14\x43lientCreateResponse\x12\x38\n\x06\x63lient\x18\x01 \x01(\x0b\x32(.pro.omni.oms.api.v1.sales.client.Client\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xef\x02\n\x11\x43lientReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xd5\x01\n\x12\x43lientReadResponse\x12\x39\n\x07\x63lients\x18\x01 \x03(\x0b\x32(.pro.omni.oms.api.v1.sales.client.Client\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard\x12\x39\n\tmeta_data\x18\x03 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData"\x87\x01\n\x13\x43lientUpdateRequest\x12\x38\n\x06\x63lient\x18\x01 \x01(\x0b\x32(.pro.omni.oms.api.v1.sales.client.Client\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9b\x01\n\x14\x43lientUpdateResponse\x12\x38\n\x06\x63lient\x18\x01 \x01(\x0b\x32(.pro.omni.oms.api.v1.sales.client.Client\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"Y\n\x13\x43lientDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"a\n\x14\x43lientDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x8d\x04\n\rClientService\x12\x7f\n\x0c\x43lientCreate\x12\x35.pro.omni.oms.api.v1.sales.client.ClientCreateRequest\x1a\x36.pro.omni.oms.api.v1.sales.client.ClientCreateResponse"\x00\x12y\n\nClientRead\x12\x33.pro.omni.oms.api.v1.sales.client.ClientReadRequest\x1a\x34.pro.omni.oms.api.v1.sales.client.ClientReadResponse"\x00\x12\x7f\n\x0c\x43lientUpdate\x12\x35.pro.omni.oms.api.v1.sales.client.ClientUpdateRequest\x1a\x36.pro.omni.oms.api.v1.sales.client.ClientUpdateResponse"\x00\x12\x7f\n\x0c\x43lientDelete\x12\x35.pro.omni.oms.api.v1.sales.client.ClientDeleteRequest\x1a\x36.pro.omni.oms.api.v1.sales.client.ClientDeleteResponse"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.sales.client_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _CLIENT._serialized_start = 79
    _CLIENT._serialized_end = 217
    _CLIENTCREATEREQUEST._serialized_start = 219
    _CLIENTCREATEREQUEST._serialized_end = 333
    _CLIENTCREATERESPONSE._serialized_start = 336
    _CLIENTCREATERESPONSE._serialized_end = 491
    _CLIENTREADREQUEST._serialized_start = 494
    _CLIENTREADREQUEST._serialized_end = 861
    _CLIENTREADRESPONSE._serialized_start = 864
    _CLIENTREADRESPONSE._serialized_end = 1077
    _CLIENTUPDATEREQUEST._serialized_start = 1080
    _CLIENTUPDATEREQUEST._serialized_end = 1215
    _CLIENTUPDATERESPONSE._serialized_start = 1218
    _CLIENTUPDATERESPONSE._serialized_end = 1373
    _CLIENTDELETEREQUEST._serialized_start = 1375
    _CLIENTDELETEREQUEST._serialized_end = 1464
    _CLIENTDELETERESPONSE._serialized_start = 1466
    _CLIENTDELETERESPONSE._serialized_end = 1563
    _CLIENTSERVICE._serialized_start = 1566
    _CLIENTSERVICE._serialized_end = 2091
# @@protoc_insertion_point(module_scope)