# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: product.proto
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
    'product.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproduct.proto\x12\x07product\"\x07\n\x05\x45mpty\"\x17\n\tProductId\x12\n\n\x02id\x18\x01 \x01(\t\"m\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x01\x12\x11\n\timage_url\x18\x05 \x01(\t\x12\x11\n\tavailable\x18\x06 \x01(\x08\"1\n\x0bProductList\x12\"\n\x08products\x18\x01 \x03(\x0b\x32\x10.product.Product2\xa2\x02\n\x0eProductService\x12\x35\n\x0bGetProducts\x12\x0e.product.Empty\x1a\x14.product.ProductList\"\x00\x12\x34\n\nGetProduct\x12\x12.product.ProductId\x1a\x10.product.Product\"\x00\x12\x35\n\rCreateProduct\x12\x10.product.Product\x1a\x10.product.Product\"\x00\x12\x35\n\rUpdateProduct\x12\x10.product.Product\x1a\x10.product.Product\"\x00\x12\x35\n\rDeleteProduct\x12\x12.product.ProductId\x1a\x0e.product.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'product_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=26
  _globals['_EMPTY']._serialized_end=33
  _globals['_PRODUCTID']._serialized_start=35
  _globals['_PRODUCTID']._serialized_end=58
  _globals['_PRODUCT']._serialized_start=60
  _globals['_PRODUCT']._serialized_end=169
  _globals['_PRODUCTLIST']._serialized_start=171
  _globals['_PRODUCTLIST']._serialized_end=220
  _globals['_PRODUCTSERVICE']._serialized_start=223
  _globals['_PRODUCTSERVICE']._serialized_end=513
# @@protoc_insertion_point(module_scope)
