# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/country.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni.pro.protos.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x14\x63ommon/country.proto\x12!pro.omni.oms.api.v1.stock.country\x1a\x11\x63ommon/base.proto"\x9a\x01\n\x07\x43ountry\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x16\n\x0e\x63ountry_doc_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x05 \x01(\x08\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x82\x01\n\x14\x43ountryCreateRequest\x12\x16\n\x0e\x63ountry_doc_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x36\n\x07\x63ontext\x18\x04 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15\x43ountryCreateResponse\x12;\n\x07\x63ountry\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.country.Country\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf0\x02\n\x12\x43ountryReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xda\x01\n\x13\x43ountryReadResponse\x12=\n\tcountries\x18\x01 \x03(\x0b\x32*.pro.omni.oms.api.v1.stock.country.Country\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x8b\x01\n\x14\x43ountryUpdateRequest\x12;\n\x07\x63ountry\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.country.Country\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\x9f\x01\n\x15\x43ountryUpdateResponse\x12;\n\x07\x63ountry\x18\x01 \x01(\x0b\x32*.pro.omni.oms.api.v1.stock.country.Country\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"Z\n\x14\x43ountryDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"b\n\x15\x43ountryDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xa5\x04\n\x0e\x43ountryService\x12\x84\x01\n\rCountryCreate\x12\x37.pro.omni.oms.api.v1.stock.country.CountryCreateRequest\x1a\x38.pro.omni.oms.api.v1.stock.country.CountryCreateResponse"\x00\x12~\n\x0b\x43ountryRead\x12\x35.pro.omni.oms.api.v1.stock.country.CountryReadRequest\x1a\x36.pro.omni.oms.api.v1.stock.country.CountryReadResponse"\x00\x12\x84\x01\n\rCountryUpdate\x12\x37.pro.omni.oms.api.v1.stock.country.CountryUpdateRequest\x1a\x38.pro.omni.oms.api.v1.stock.country.CountryUpdateResponse"\x00\x12\x84\x01\n\rCountryDelete\x12\x37.pro.omni.oms.api.v1.stock.country.CountryDeleteRequest\x1a\x38.pro.omni.oms.api.v1.stock.country.CountryDeleteResponse"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "common.country_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _COUNTRY._serialized_start = 79
    _COUNTRY._serialized_end = 233
    _COUNTRYCREATEREQUEST._serialized_start = 236
    _COUNTRYCREATEREQUEST._serialized_end = 366
    _COUNTRYCREATERESPONSE._serialized_start = 369
    _COUNTRYCREATERESPONSE._serialized_end = 528
    _COUNTRYREADREQUEST._serialized_start = 531
    _COUNTRYREADREQUEST._serialized_end = 899
    _COUNTRYREADRESPONSE._serialized_start = 902
    _COUNTRYREADRESPONSE._serialized_end = 1120
    _COUNTRYUPDATEREQUEST._serialized_start = 1123
    _COUNTRYUPDATEREQUEST._serialized_end = 1262
    _COUNTRYUPDATERESPONSE._serialized_start = 1265
    _COUNTRYUPDATERESPONSE._serialized_end = 1424
    _COUNTRYDELETEREQUEST._serialized_start = 1426
    _COUNTRYDELETEREQUEST._serialized_end = 1516
    _COUNTRYDELETERESPONSE._serialized_start = 1518
    _COUNTRYDELETERESPONSE._serialized_end = 1616
    _COUNTRYSERVICE._serialized_start = 1619
    _COUNTRYSERVICE._serialized_end = 2168
# @@protoc_insertion_point(module_scope)