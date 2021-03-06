# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: drone.proto

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
  name='drone.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x64rone.proto\"\x15\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\x05\"\x08\n\x06Regist\")\n\x06\x44\x61ncer\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\t\n\x01z\x18\x04 \x01(\x05\"\x1a\n\x0cRegistResult\x12\n\n\x02id\x18\x01 \x01(\x05\",\n\x11StartDancerResult\x12\x17\n\x06\x64\x61ncer\x18\x01 \x01(\x0b\x32\x07.Dancer\"+\n\x10PeerDancerResult\x12\x17\n\x06\x64\x61ncer\x18\x01 \x01(\x0b\x32\x07.Dancer2W\n\nCoordinate\x12!\n\x05setup\x12\x07.Regist\x1a\r.RegistResult\"\x00\x12&\n\x03get\x12\x08.Request\x1a\x11.PeerDancerResult\"\x00\x30\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Request.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=15,
  serialized_end=36,
)


_REGIST = _descriptor.Descriptor(
  name='Regist',
  full_name='Regist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=38,
  serialized_end=46,
)


_DANCER = _descriptor.Descriptor(
  name='Dancer',
  full_name='Dancer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Dancer.x', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='Dancer.y', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='Dancer.z', index=2,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=48,
  serialized_end=89,
)


_REGISTRESULT = _descriptor.Descriptor(
  name='RegistResult',
  full_name='RegistResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RegistResult.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=91,
  serialized_end=117,
)


_STARTDANCERRESULT = _descriptor.Descriptor(
  name='StartDancerResult',
  full_name='StartDancerResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dancer', full_name='StartDancerResult.dancer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=119,
  serialized_end=163,
)


_PEERDANCERRESULT = _descriptor.Descriptor(
  name='PeerDancerResult',
  full_name='PeerDancerResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dancer', full_name='PeerDancerResult.dancer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=165,
  serialized_end=208,
)

_STARTDANCERRESULT.fields_by_name['dancer'].message_type = _DANCER
_PEERDANCERRESULT.fields_by_name['dancer'].message_type = _DANCER
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Regist'] = _REGIST
DESCRIPTOR.message_types_by_name['Dancer'] = _DANCER
DESCRIPTOR.message_types_by_name['RegistResult'] = _REGISTRESULT
DESCRIPTOR.message_types_by_name['StartDancerResult'] = _STARTDANCERRESULT
DESCRIPTOR.message_types_by_name['PeerDancerResult'] = _PEERDANCERRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'drone_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Regist = _reflection.GeneratedProtocolMessageType('Regist', (_message.Message,), dict(
  DESCRIPTOR = _REGIST,
  __module__ = 'drone_pb2'
  # @@protoc_insertion_point(class_scope:Regist)
  ))
_sym_db.RegisterMessage(Regist)

Dancer = _reflection.GeneratedProtocolMessageType('Dancer', (_message.Message,), dict(
  DESCRIPTOR = _DANCER,
  __module__ = 'drone_pb2'
  # @@protoc_insertion_point(class_scope:Dancer)
  ))
_sym_db.RegisterMessage(Dancer)

RegistResult = _reflection.GeneratedProtocolMessageType('RegistResult', (_message.Message,), dict(
  DESCRIPTOR = _REGISTRESULT,
  __module__ = 'drone_pb2'
  # @@protoc_insertion_point(class_scope:RegistResult)
  ))
_sym_db.RegisterMessage(RegistResult)

StartDancerResult = _reflection.GeneratedProtocolMessageType('StartDancerResult', (_message.Message,), dict(
  DESCRIPTOR = _STARTDANCERRESULT,
  __module__ = 'drone_pb2'
  # @@protoc_insertion_point(class_scope:StartDancerResult)
  ))
_sym_db.RegisterMessage(StartDancerResult)

PeerDancerResult = _reflection.GeneratedProtocolMessageType('PeerDancerResult', (_message.Message,), dict(
  DESCRIPTOR = _PEERDANCERRESULT,
  __module__ = 'drone_pb2'
  # @@protoc_insertion_point(class_scope:PeerDancerResult)
  ))
_sym_db.RegisterMessage(PeerDancerResult)



_COORDINATE = _descriptor.ServiceDescriptor(
  name='Coordinate',
  full_name='Coordinate',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=210,
  serialized_end=297,
  methods=[
  _descriptor.MethodDescriptor(
    name='setup',
    full_name='Coordinate.setup',
    index=0,
    containing_service=None,
    input_type=_REGIST,
    output_type=_REGISTRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='Coordinate.get',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_PEERDANCERRESULT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COORDINATE)

DESCRIPTOR.services_by_name['Coordinate'] = _COORDINATE

# @@protoc_insertion_point(module_scope)
