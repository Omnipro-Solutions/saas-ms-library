# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/schedule_work_schedule_work_line.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni.pro.protos.common import base_pb2 as common_dot_base__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n/v1/rules/schedule_work_schedule_work_line.proto\x12:pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line\x1a\x11\x63ommon/base.proto"\xb4\x01\n\x1cScheduleWorkScheduleWorkLine\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x18\n\x10schedule_work_id\x18\x02 \x01(\x05\x12\x1d\n\x15schedule_work_line_id\x18\x03 \x01(\x05\x12\x0e\n\x06\x61\x63tive\x18\x04 \x01(\x08\x12?\n\x0cobject_audit\x18\x05 \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\x9c\x01\n)ScheduleWorkScheduleWorkLineCreateRequest\x12\x18\n\x10schedule_work_id\x18\x01 \x01(\x05\x12\x1d\n\x15schedule_work_line_id\x18\x02 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x03 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xfc\x01\n*ScheduleWorkScheduleWorkLineCreateResponse\x12\x82\x01\n schedule_work_schedule_work_line\x18\x01 \x01(\x0b\x32X.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLine\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\x85\x03\n\'ScheduleWorkScheduleWorkLineReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xb5\x02\n(ScheduleWorkScheduleWorkLineReadResponse\x12\x82\x01\n schedule_work_schedule_work_line\x18\x01 \x03(\x0b\x32X.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLine\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xe8\x01\n)ScheduleWorkScheduleWorkLineUpdateRequest\x12\x82\x01\n schedule_work_schedule_work_line\x18\x01 \x01(\x0b\x32X.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLine\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xfc\x01\n*ScheduleWorkScheduleWorkLineUpdateResponse\x12\x82\x01\n schedule_work_schedule_work_line\x18\x01 \x01(\x0b\x32X.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLine\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"o\n)ScheduleWorkScheduleWorkLineDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"w\n*ScheduleWorkScheduleWorkLineDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard2\xff\x07\n#ScheduleWorkScheduleWorkLineService\x12\xf5\x01\n"ScheduleWorkScheduleWorkLineCreate\x12\x65.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineCreateRequest\x1a\x66.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineCreateResponse"\x00\x12\xef\x01\n ScheduleWorkScheduleWorkLineRead\x12\x63.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineReadRequest\x1a\x64.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineReadResponse"\x00\x12\xf5\x01\n"ScheduleWorkScheduleWorkLineUpdate\x12\x65.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineUpdateRequest\x1a\x66.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineUpdateResponse"\x00\x12\xf5\x01\n"ScheduleWorkScheduleWorkLineDelete\x12\x65.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineDeleteRequest\x1a\x66.pro.omni.oms.api.v1.rules.schedule_work_schedule_work_line.ScheduleWorkScheduleWorkLineDeleteResponse"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.schedule_work_schedule_work_line_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SCHEDULEWORKSCHEDULEWORKLINE._serialized_start = 131
    _SCHEDULEWORKSCHEDULEWORKLINE._serialized_end = 311
    _SCHEDULEWORKSCHEDULEWORKLINECREATEREQUEST._serialized_start = 314
    _SCHEDULEWORKSCHEDULEWORKLINECREATEREQUEST._serialized_end = 470
    _SCHEDULEWORKSCHEDULEWORKLINECREATERESPONSE._serialized_start = 473
    _SCHEDULEWORKSCHEDULEWORKLINECREATERESPONSE._serialized_end = 725
    _SCHEDULEWORKSCHEDULEWORKLINEREADREQUEST._serialized_start = 728
    _SCHEDULEWORKSCHEDULEWORKLINEREADREQUEST._serialized_end = 1117
    _SCHEDULEWORKSCHEDULEWORKLINEREADRESPONSE._serialized_start = 1120
    _SCHEDULEWORKSCHEDULEWORKLINEREADRESPONSE._serialized_end = 1429
    _SCHEDULEWORKSCHEDULEWORKLINEUPDATEREQUEST._serialized_start = 1432
    _SCHEDULEWORKSCHEDULEWORKLINEUPDATEREQUEST._serialized_end = 1664
    _SCHEDULEWORKSCHEDULEWORKLINEUPDATERESPONSE._serialized_start = 1667
    _SCHEDULEWORKSCHEDULEWORKLINEUPDATERESPONSE._serialized_end = 1919
    _SCHEDULEWORKSCHEDULEWORKLINEDELETEREQUEST._serialized_start = 1921
    _SCHEDULEWORKSCHEDULEWORKLINEDELETEREQUEST._serialized_end = 2032
    _SCHEDULEWORKSCHEDULEWORKLINEDELETERESPONSE._serialized_start = 2034
    _SCHEDULEWORKSCHEDULEWORKLINEDELETERESPONSE._serialized_end = 2153
    _SCHEDULEWORKSCHEDULEWORKLINESERVICE._serialized_start = 2156
    _SCHEDULEWORKSCHEDULEWORKLINESERVICE._serialized_end = 3179
# @@protoc_insertion_point(module_scope)