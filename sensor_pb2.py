# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: sensor.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'sensor.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csensor.proto\"Z\n\nSensorData\x12\x11\n\tsensor_id\x18\x01 \x01(\t\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\x12\x10\n\x08humidity\x18\x03 \x01(\x01\x12\x12\n\nluminosity\x18\x04 \x01(\x01\"{\n\x0f\x44\x61shboardUpdate\x12\x11\n\tsensor_id\x18\x01 \x01(\t\x12\x17\n\x0f\x61vg_temperature\x18\x02 \x01(\x01\x12\x14\n\x0c\x61vg_humidity\x18\x03 \x01(\x01\x12\x16\n\x0e\x61vg_luminosity\x18\x04 \x01(\x01\x12\x0e\n\x06status\x18\x05 \x01(\t2F\n\rSensorService\x12\x35\n\x10StreamSensorData\x12\x0b.SensorData\x1a\x10.DashboardUpdate(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sensor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SENSORDATA']._serialized_start=16
  _globals['_SENSORDATA']._serialized_end=106
  _globals['_DASHBOARDUPDATE']._serialized_start=108
  _globals['_DASHBOARDUPDATE']._serialized_end=231
  _globals['_SENSORSERVICE']._serialized_start=233
  _globals['_SENSORSERVICE']._serialized_end=303
# @@protoc_insertion_point(module_scope)
