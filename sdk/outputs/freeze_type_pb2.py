# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: freeze_type.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'freeze_type.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x66reeze_type.proto\x12\x05proto*\x88\x01\n\nFreezeType\x12\x17\n\x13UNKNOWN_FREEZE_TYPE\x10\x00\x12\x0f\n\x0b\x46REEZE_ONLY\x10\x01\x12\x13\n\x0fPREPARE_UPGRADE\x10\x02\x12\x12\n\x0e\x46REEZE_UPGRADE\x10\x03\x12\x10\n\x0c\x46REEZE_ABORT\x10\x04\x12\x15\n\x11TELEMETRY_UPGRADE\x10\x05\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'freeze_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_FREEZETYPE']._serialized_start=29
  _globals['_FREEZETYPE']._serialized_end=165
# @@protoc_insertion_point(module_scope)
