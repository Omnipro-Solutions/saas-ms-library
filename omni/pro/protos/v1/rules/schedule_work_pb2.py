# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/schedule_work.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni.pro.protos.common import base_pb2 as common_dot_base__pb2
from omni.pro.protos.v1.rules import schedule_work_line_pb2 as v1_dot_rules_dot_schedule__work__line__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cv1/rules/schedule_work.proto\x12\'pro.omni.oms.api.v1.rules.schedule_work\x1a\x11\x63ommon/base.proto\x1a!v1/rules/schedule_work_line.proto"\xee\x01\n\x0cScheduleWork\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61lendar_id\x18\x03 \x01(\x05\x12^\n\x16schedule_work_line_ids\x18\x04 \x03(\x0b\x32>.pro.omni.oms.api.v1.rules.schedule_work_line.ScheduleWorkLine\x12\x0e\n\x06\x61\x63tive\x18\x05 \x01(\x08\x12?\n\x0cobject_audit\x18\x06 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"v\n\x19ScheduleWorkCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61lendar_id\x18\x02 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb5\x01\n\x1aScheduleWorkCreateResponse\x12L\n\rschedule_work\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWork\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf5\x02\n\x17ScheduleWorkReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xef\x01\n\x18ScheduleWorkReadResponse\x12M\n\x0eschedules_work\x18\x01 \x03(\x0b\x32\x35.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWork\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xa1\x01\n\x19ScheduleWorkUpdateRequest\x12L\n\rschedule_work\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWork\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb5\x01\n\x1aScheduleWorkUpdateResponse\x12L\n\rschedule_work\x18\x01 \x01(\x0b\x32\x35.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWork\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"_\n\x19ScheduleWorkDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"g\n\x1aScheduleWorkDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\x97\x05\n\x13ScheduleWorkService\x12\x9f\x01\n\x12ScheduleWorkCreate\x12\x42.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkCreateRequest\x1a\x43.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkCreateResponse"\x00\x12\x99\x01\n\x10ScheduleWorkRead\x12@.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkReadRequest\x1a\x41.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkReadResponse"\x00\x12\x9f\x01\n\x12ScheduleWorkUpdate\x12\x42.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkUpdateRequest\x1a\x43.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkUpdateResponse"\x00\x12\x9f\x01\n\x12ScheduleWorkDelete\x12\x42.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkDeleteRequest\x1a\x43.pro.omni.oms.api.v1.rules.schedule_work.ScheduleWorkDeleteResponse"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.schedule_work_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCHEDULEWORK._serialized_start = 128
    _SCHEDULEWORK._serialized_end = 366
    _SCHEDULEWORKCREATEREQUEST._serialized_start = 368
    _SCHEDULEWORKCREATEREQUEST._serialized_end = 486
    _SCHEDULEWORKCREATERESPONSE._serialized_start = 489
    _SCHEDULEWORKCREATERESPONSE._serialized_end = 670
    _SCHEDULEWORKREADREQUEST._serialized_start = 673
    _SCHEDULEWORKREADREQUEST._serialized_end = 1046
    _SCHEDULEWORKREADRESPONSE._serialized_start = 1049
    _SCHEDULEWORKREADRESPONSE._serialized_end = 1288
    _SCHEDULEWORKUPDATEREQUEST._serialized_start = 1291
    _SCHEDULEWORKUPDATEREQUEST._serialized_end = 1452
    _SCHEDULEWORKUPDATERESPONSE._serialized_start = 1455
    _SCHEDULEWORKUPDATERESPONSE._serialized_end = 1636
    _SCHEDULEWORKDELETEREQUEST._serialized_start = 1638
    _SCHEDULEWORKDELETEREQUEST._serialized_end = 1733
    _SCHEDULEWORKDELETERESPONSE._serialized_start = 1735
    _SCHEDULEWORKDELETERESPONSE._serialized_end = 1838
    _SCHEDULEWORKSERVICE._serialized_start = 1841
    _SCHEDULEWORKSERVICE._serialized_end = 2504
# @@protoc_insertion_point(module_scope)