# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: transaction_record.proto
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
    'transaction_record.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import timestamp_pb2 as timestamp__pb2
from . import basic_types_pb2 as basic__types__pb2
from . import custom_fees_pb2 as custom__fees__pb2
from . import transaction_receipt_pb2 as transaction__receipt__pb2
from . import crypto_transfer_pb2 as crypto__transfer__pb2
from . import contract_call_local_pb2 as contract__call__local__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18transaction_record.proto\x12\x05proto\x1a\x0ftimestamp.proto\x1a\x11\x62\x61sic_types.proto\x1a\x11\x63ustom_fees.proto\x1a\x19transaction_receipt.proto\x1a\x15\x63rypto_transfer.proto\x1a\x19\x63ontract_call_local.proto\"\xf5\x06\n\x11TransactionRecord\x12*\n\x07receipt\x18\x01 \x01(\x0b\x32\x19.proto.TransactionReceipt\x12\x17\n\x0ftransactionHash\x18\x02 \x01(\x0c\x12,\n\x12\x63onsensusTimestamp\x18\x03 \x01(\x0b\x32\x10.proto.Timestamp\x12+\n\rtransactionID\x18\x04 \x01(\x0b\x32\x14.proto.TransactionID\x12\x0c\n\x04memo\x18\x05 \x01(\t\x12\x16\n\x0etransactionFee\x18\x06 \x01(\x04\x12;\n\x12\x63ontractCallResult\x18\x07 \x01(\x0b\x32\x1d.proto.ContractFunctionResultH\x00\x12=\n\x14\x63ontractCreateResult\x18\x08 \x01(\x0b\x32\x1d.proto.ContractFunctionResultH\x00\x12)\n\x0ctransferList\x18\n \x01(\x0b\x32\x13.proto.TransferList\x12\x34\n\x12tokenTransferLists\x18\x0b \x03(\x0b\x32\x18.proto.TokenTransferList\x12&\n\x0bscheduleRef\x18\x0c \x01(\x0b\x32\x11.proto.ScheduleID\x12\x36\n\x14\x61ssessed_custom_fees\x18\r \x03(\x0b\x32\x18.proto.AssessedCustomFee\x12=\n\x1c\x61utomatic_token_associations\x18\x0e \x03(\x0b\x32\x17.proto.TokenAssociation\x12\x34\n\x1aparent_consensus_timestamp\x18\x0f \x01(\x0b\x32\x10.proto.Timestamp\x12\r\n\x05\x61lias\x18\x10 \x01(\x0c\x12\x15\n\rethereum_hash\x18\x11 \x01(\x0c\x12\x32\n\x14paid_staking_rewards\x18\x12 \x03(\x0b\x32\x14.proto.AccountAmount\x12\x14\n\nprng_bytes\x18\x13 \x01(\x0cH\x01\x12\x15\n\x0bprng_number\x18\x14 \x01(\x05H\x01\x12\x13\n\x0b\x65vm_address\x18\x15 \x01(\x0c\x12\x39\n\x14new_pending_airdrops\x18\x16 \x03(\x0b\x32\x1b.proto.PendingAirdropRecordB\x06\n\x04\x62odyB\t\n\x07\x65ntropy\"\x86\x01\n\x14PendingAirdropRecord\x12\x33\n\x12pending_airdrop_id\x18\x01 \x01(\x0b\x32\x17.proto.PendingAirdropId\x12\x39\n\x15pending_airdrop_value\x18\x02 \x01(\x0b\x32\x1a.proto.PendingAirdropValueB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transaction_record_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_TRANSACTIONRECORD']._serialized_start=168
  _globals['_TRANSACTIONRECORD']._serialized_end=1053
  _globals['_PENDINGAIRDROPRECORD']._serialized_start=1056
  _globals['_PENDINGAIRDROPRECORD']._serialized_end=1190
# @@protoc_insertion_point(module_scope)
