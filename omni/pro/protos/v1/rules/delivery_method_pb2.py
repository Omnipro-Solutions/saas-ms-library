# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/rules/delivery_method.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from omni.pro.protos.common import base_pb2 as common_dot_base__pb2
from omni.pro.protos.v1.rules import warehouse_pb2 as v1_dot_rules_dot_warehouse__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1ev1/rules/delivery_method.proto\x12)pro.omni.oms.api.v1.rules.delivery_method\x1a\x11\x63ommon/base.proto\x1a\x18v1/rules/warehouse.proto"\x9a\x05\n\x0e\x44\x65liveryMethod\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12N\n\x16\x64\x65livery_warehouse_ids\x18\x03 \x03(\x0b\x32..pro.omni.oms.api.v1.rules.warehouse.Warehouse\x12]\n\x15type_picking_transfer\x18\x04 \x01(\x0e\x32>.pro.omni.oms.api.v1.rules.delivery_method.TypePickingTransfer\x12\x61\n\x17validate_warehouse_code\x18\x05 \x01(\x0e\x32@.pro.omni.oms.api.v1.rules.delivery_method.ValidateWarehouseCode\x12\x19\n\x11quantity_sequrity\x18\x06 \x01(\x02\x12\x0c\n\x04\x63ode\x18\x07 \x01(\t\x12N\n\rtype_delivery\x18\x08 \x01(\x0e\x32\x37.pro.omni.oms.api.v1.rules.delivery_method.TypeDelivery\x12\x1c\n\x14\x64\x65livery_location_id\x18\t \x01(\x05\x12\x1c\n\x14transfer_template_id\x18\n \x01(\x05\x12\x1c\n\x14\x63\x61tegory_template_id\x18\x0b \x01(\x05\x12\x1a\n\x12local_available_id\x18\x0c \x01(\x05\x12\x1c\n\x14schedule_template_id\x18\r \x01(\x05\x12\x0e\n\x06\x61\x63tive\x18\x0e \x01(\x08\x12?\n\x0cobject_audit\x18\x0f \x01(\x0b\x32).pro.omni.oms.api.common.base.ObjectAudit"\xb2\x04\n\x1b\x44\x65liveryMethodCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12]\n\x15type_picking_transfer\x18\x02 \x01(\x0e\x32>.pro.omni.oms.api.v1.rules.delivery_method.TypePickingTransfer\x12\x61\n\x17validate_warehouse_code\x18\x03 \x01(\x0e\x32@.pro.omni.oms.api.v1.rules.delivery_method.ValidateWarehouseCode\x12\x19\n\x11quantity_sequrity\x18\x04 \x01(\x02\x12\x0c\n\x04\x63ode\x18\x05 \x01(\t\x12N\n\rtype_delivery\x18\x06 \x01(\x0e\x32\x37.pro.omni.oms.api.v1.rules.delivery_method.TypeDelivery\x12\x1c\n\x14\x64\x65livery_location_id\x18\x07 \x01(\x05\x12\x1c\n\x14transfer_template_id\x18\x08 \x01(\x05\x12\x1c\n\x14\x63\x61tegory_template_id\x18\t \x01(\x05\x12\x1a\n\x12local_available_id\x18\n \x01(\x05\x12\x1c\n\x14schedule_template_id\x18\x0b \x01(\x05\x12\x36\n\x07\x63ontext\x18\x0c \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xbd\x01\n\x1c\x44\x65liveryMethodCreateResponse\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xf7\x02\n\x19\x44\x65liveryMethodReadRequest\x12\x37\n\x08group_by\x18\x01 \x03(\x0b\x32%.pro.omni.oms.api.common.base.GroupBy\x12\x35\n\x07sort_by\x18\x02 \x01(\x0b\x32$.pro.omni.oms.api.common.base.SortBy\x12\x34\n\x06\x66ields\x18\x03 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Fields\x12\x34\n\x06\x66ilter\x18\x04 \x01(\x0b\x32$.pro.omni.oms.api.common.base.Filter\x12:\n\tpaginated\x18\x05 \x01(\x0b\x32\'.pro.omni.oms.api.common.base.Paginated\x12\n\n\x02id\x18\x06 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x07 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xf7\x01\n\x1a\x44\x65liveryMethodReadResponse\x12S\n\x10\x64\x65livery_methods\x18\x01 \x03(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12\x39\n\tmeta_data\x18\x02 \x01(\x0b\x32&.pro.omni.oms.api.common.base.MetaData\x12I\n\x11response_standard\x18\x03 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"\xa9\x01\n\x1b\x44\x65liveryMethodUpdateRequest\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"\xbd\x01\n\x1c\x44\x65liveryMethodUpdateResponse\x12R\n\x0f\x64\x65livery_method\x18\x01 \x01(\x0b\x32\x39.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethod\x12I\n\x11response_standard\x18\x02 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard"a\n\x1b\x44\x65liveryMethodDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x36\n\x07\x63ontext\x18\x02 \x01(\x0b\x32%.pro.omni.oms.api.common.base.Context"i\n\x1c\x44\x65liveryMethodDeleteResponse\x12I\n\x11response_standard\x18\x01 \x01(\x0b\x32..pro.omni.oms.api.common.base.ResponseStandard*4\n\x13TypePickingTransfer\x12\x0b\n\x07PARTIAL\x10\x00\x12\x10\n\x0c\x43ONSOLIDATED\x10\x01*D\n\x15ValidateWarehouseCode\x12\x0c\n\x08OPTIONAL\x10\x00\x12\x0c\n\x08REQUIRED\x10\x01\x12\x0f\n\x0bUNNECESSARY\x10\x02*\'\n\x0cTypeDelivery\x12\t\n\x05STORE\x10\x00\x12\x0c\n\x08SHIPPING\x10\x01\x32\xc1\x05\n\x15\x44\x65liveryMethodService\x12\xa9\x01\n\x14\x44\x65liveryMethodCreate\x12\x46.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodCreateRequest\x1aG.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodCreateResponse"\x00\x12\xa3\x01\n\x12\x44\x65liveryMethodRead\x12\x44.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodReadRequest\x1a\x45.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodReadResponse"\x00\x12\xa9\x01\n\x14\x44\x65liveryMethodUpdate\x12\x46.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodUpdateRequest\x1aG.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodUpdateResponse"\x00\x12\xa9\x01\n\x14\x44\x65liveryMethodDelete\x12\x46.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodDeleteRequest\x1aG.pro.omni.oms.api.v1.rules.delivery_method.DeliveryMethodDeleteResponse"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "v1.rules.delivery_method_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TYPEPICKINGTRANSFER._serialized_start = 2746
    _TYPEPICKINGTRANSFER._serialized_end = 2798
    _VALIDATEWAREHOUSECODE._serialized_start = 2800
    _VALIDATEWAREHOUSECODE._serialized_end = 2868
    _TYPEDELIVERY._serialized_start = 2870
    _TYPEDELIVERY._serialized_end = 2909
    _DELIVERYMETHOD._serialized_start = 123
    _DELIVERYMETHOD._serialized_end = 789
    _DELIVERYMETHODCREATEREQUEST._serialized_start = 792
    _DELIVERYMETHODCREATEREQUEST._serialized_end = 1354
    _DELIVERYMETHODCREATERESPONSE._serialized_start = 1357
    _DELIVERYMETHODCREATERESPONSE._serialized_end = 1546
    _DELIVERYMETHODREADREQUEST._serialized_start = 1549
    _DELIVERYMETHODREADREQUEST._serialized_end = 1924
    _DELIVERYMETHODREADRESPONSE._serialized_start = 1927
    _DELIVERYMETHODREADRESPONSE._serialized_end = 2174
    _DELIVERYMETHODUPDATEREQUEST._serialized_start = 2177
    _DELIVERYMETHODUPDATEREQUEST._serialized_end = 2346
    _DELIVERYMETHODUPDATERESPONSE._serialized_start = 2349
    _DELIVERYMETHODUPDATERESPONSE._serialized_end = 2538
    _DELIVERYMETHODDELETEREQUEST._serialized_start = 2540
    _DELIVERYMETHODDELETEREQUEST._serialized_end = 2637
    _DELIVERYMETHODDELETERESPONSE._serialized_start = 2639
    _DELIVERYMETHODDELETERESPONSE._serialized_end = 2744
    _DELIVERYMETHODSERVICE._serialized_start = 2912
    _DELIVERYMETHODSERVICE._serialized_end = 3617
# @@protoc_insertion_point(module_scope)