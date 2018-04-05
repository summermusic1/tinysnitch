# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ui.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ui.proto',
  package='ui',
  syntax='proto3',
  serialized_pb=_b('\n\x08ui.proto\x12\x02ui\"\x19\n\x0bPingRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"\x17\n\tPingReply\x12\n\n\x02id\x18\x01 \x01(\x04\"\xb5\x01\n\x0bRuleRequest\x12\x10\n\x08protocol\x18\x01 \x01(\t\x12\x0e\n\x06src_ip\x18\x02 \x01(\t\x12\x10\n\x08src_port\x18\x03 \x01(\r\x12\x0e\n\x06\x64st_ip\x18\x04 \x01(\t\x12\x10\n\x08\x64st_host\x18\x05 \x01(\t\x12\x10\n\x08\x64st_port\x18\x06 \x01(\r\x12\x12\n\nprocess_id\x18\x07 \x01(\r\x12\x14\n\x0cprocess_path\x18\x08 \x01(\t\x12\x14\n\x0cprocess_args\x18\t \x03(\t\"X\n\tRuleReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x10\n\x08\x64uration\x18\x03 \x01(\t\x12\x0c\n\x04what\x18\x04 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\t2[\n\x02UI\x12(\n\x04Ping\x12\x0f.ui.PingRequest\x1a\r.ui.PingReply\"\x00\x12+\n\x07\x41skRule\x12\x0f.ui.RuleRequest\x1a\r.ui.RuleReply\"\x00\x62\x06proto3')
)




_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='ui.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ui.PingRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=41,
)


_PINGREPLY = _descriptor.Descriptor(
  name='PingReply',
  full_name='ui.PingReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ui.PingReply.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=66,
)


_RULEREQUEST = _descriptor.Descriptor(
  name='RuleRequest',
  full_name='ui.RuleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol', full_name='ui.RuleRequest.protocol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_ip', full_name='ui.RuleRequest.src_ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_port', full_name='ui.RuleRequest.src_port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_ip', full_name='ui.RuleRequest.dst_ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_host', full_name='ui.RuleRequest.dst_host', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_port', full_name='ui.RuleRequest.dst_port', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process_id', full_name='ui.RuleRequest.process_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process_path', full_name='ui.RuleRequest.process_path', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process_args', full_name='ui.RuleRequest.process_args', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=250,
)


_RULEREPLY = _descriptor.Descriptor(
  name='RuleReply',
  full_name='ui.RuleReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ui.RuleReply.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='ui.RuleReply.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='ui.RuleReply.duration', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='what', full_name='ui.RuleReply.what', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ui.RuleReply.value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=340,
)

DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingReply'] = _PINGREPLY
DESCRIPTOR.message_types_by_name['RuleRequest'] = _RULEREQUEST
DESCRIPTOR.message_types_by_name['RuleReply'] = _RULEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:ui.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingReply = _reflection.GeneratedProtocolMessageType('PingReply', (_message.Message,), dict(
  DESCRIPTOR = _PINGREPLY,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:ui.PingReply)
  ))
_sym_db.RegisterMessage(PingReply)

RuleRequest = _reflection.GeneratedProtocolMessageType('RuleRequest', (_message.Message,), dict(
  DESCRIPTOR = _RULEREQUEST,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:ui.RuleRequest)
  ))
_sym_db.RegisterMessage(RuleRequest)

RuleReply = _reflection.GeneratedProtocolMessageType('RuleReply', (_message.Message,), dict(
  DESCRIPTOR = _RULEREPLY,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:ui.RuleReply)
  ))
_sym_db.RegisterMessage(RuleReply)



_UI = _descriptor.ServiceDescriptor(
  name='UI',
  full_name='ui.UI',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=342,
  serialized_end=433,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='ui.UI.Ping',
    index=0,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AskRule',
    full_name='ui.UI.AskRule',
    index=1,
    containing_service=None,
    input_type=_RULEREQUEST,
    output_type=_RULEREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_UI)

DESCRIPTOR.services_by_name['UI'] = _UI

# @@protoc_insertion_point(module_scope)