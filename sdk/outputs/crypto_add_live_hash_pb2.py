# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: crypto_add_live_hash.proto
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
    'crypto_add_live_hash.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2
from . import duration_pb2 as duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63rypto_add_live_hash.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0e\x64uration.proto\"~\n\x08LiveHash\x12#\n\taccountId\x18\x01 \x01(\x0b\x32\x10.proto.AccountID\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x1c\n\x04keys\x18\x03 \x01(\x0b\x32\x0e.proto.KeyList\x12!\n\x08\x64uration\x18\x05 \x01(\x0b\x32\x0f.proto.Duration\"E\n CryptoAddLiveHashTransactionBody\x12!\n\x08liveHash\x18\x03 \x01(\x0b\x32\x0f.proto.LiveHashB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crypto_add_live_hash_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_LIVEHASH']._serialized_start=72
  _globals['_LIVEHASH']._serialized_end=198
  _globals['_CRYPTOADDLIVEHASHTRANSACTIONBODY']._serialized_start=200
  _globals['_CRYPTOADDLIVEHASHTRANSACTIONBODY']._serialized_end=269
# @@protoc_insertion_point(module_scope)
