# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gacha.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gacha.proto',
  package='gacha',
  syntax='proto3',
  serialized_options=b'Z\010../gacha',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bgacha.proto\x12\x05gacha\"\x18\n\x07Request\x12\r\n\x05\x63ount\x18\x01 \x01(\t\"\x1a\n\x08Response\x12\x0e\n\x06result\x18\x01 \x03(\t2k\n\x05Gacha\x12\x30\n\x0bGachaResult\x12\x0e.gacha.Request\x1a\x0f.gacha.Response\"\x00\x12\x30\n\x0bTotalResult\x12\x0e.gacha.Request\x1a\x0f.gacha.Response\"\x00\x42\nZ\x08../gachab\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='gacha.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='gacha.Request.count', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=46,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='gacha.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='gacha.Response.result', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'gacha_pb2'
  # @@protoc_insertion_point(class_scope:gacha.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'gacha_pb2'
  # @@protoc_insertion_point(class_scope:gacha.Response)
  })
_sym_db.RegisterMessage(Response)


DESCRIPTOR._options = None

_GACHA = _descriptor.ServiceDescriptor(
  name='Gacha',
  full_name='gacha.Gacha',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=76,
  serialized_end=183,
  methods=[
  _descriptor.MethodDescriptor(
    name='GachaResult',
    full_name='gacha.Gacha.GachaResult',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TotalResult',
    full_name='gacha.Gacha.TotalResult',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GACHA)

DESCRIPTOR.services_by_name['Gacha'] = _GACHA

# @@protoc_insertion_point(module_scope)
