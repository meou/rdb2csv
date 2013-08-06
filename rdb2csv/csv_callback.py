#!/usr/bin/env python

import sys
from rdbtools import RdbCallback

class CsvCallback(RdbCallback):
  def __init__(self, outf, pre, post, column_delimiter = ',', line_delimiter = '\n'):
    self.outf = outf
    self.column_delimiter = column_delimiter
    self.line_delimiter = line_delimiter
    self.pre_keys = tuple(pre)
    self.post_keys = tuple(post)
    self.pre_values = {}
    self.post_values = {}

  def set(self, key, value, expiry, info):
    self.outf.write ("%s%s%s%s" % (str(key), self.column_delimiter, str(value), self.line_delimiter))

  def start_hash(self, key, length, expiry, info):
    s_key = str(key)
    self.pre_values[s_key] = {}
    self.post_values[s_key] = {}

  def hset(self, key, field, value):

    s_key = str(key)
    s_field = str(field)
    s_value = str(value)

    if s_field in self.pre_keys:
      self.pre_values[s_key][s_field] = s_value
#      print (self.post_values)
    elif s_field in self.post_keys:
      self.post_values[s_key][s_field] = s_value
#      print (self.post_values)
    else:
      print ("Ignore [key,field,value]=[%s, %s, %s]\n" % (s_key, s_field, s_value))

  def end_hash(self, key):

    s_key = str(key)
    out_list = []

    for pre_key in self.pre_keys:
      if pre_key in self.pre_values[s_key]:
        out_list.append(self.pre_values[s_key][pre_key])
      out_list.append(self.column_delimiter)

    out_list.append(key)
    out_list.append(self.column_delimiter)

    for post_key in self.post_keys:
      if post_key in self.post_values[s_key]:
        out_list.append(self.post_values[s_key][post_key])
      out_list.append(self.column_delimiter)

    out_list.pop()
    out_list.append(self.line_delimiter)
    self.outf.write("".join(out_list))

    del self.pre_values[s_key]
    del self.post_values[s_key]

  def start_set(self, key, cardinality, expiry, info):
    self.outf.write (sys._getframe().f_code.co_name + " has not been unsupported yet\n")

  def sadd(self, key, member):
    self.outf.write (sys._getframe().f_code.co_name + " has not been unsupported yet\n")

  def end_set(self, key):
    self.outf.write (sys._getframe().f_code.co_name + " has not been unsupported yet\n")

  def start_list(self, key, length, expiry, info):
    self.outf.write (sys._getframe().f_code.co_name + " has not been unsupported yet\n")

  def rpush(self, key, value):
    self.outf.write (sys._getframe().f_code.co_name + " has not been unsupported yet\n")

  def end_list(self, key):
    self.outf.write (sys._getframe().f_code.co_name + " has not been unsupported yet\n")

  def start_sorted_set(self, key, length, expiry, info):
    self.outf.write (sys._getframe().f_code.co_name + " has not been unsupported yet\n")

  def zadd(self, key, score, member):
    self.outf.write (sys._getframe().f_code.co_name + " has not been unsupported yet\n")

  def end_sorted_set(self, key):
    self.outf.write (sys._getframe().f_code.co_name + " has not been unsupported yet\n")
