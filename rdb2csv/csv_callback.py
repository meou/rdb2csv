#!/usr/bin/env python

import sys
from rdbtools import RdbCallback

class CsvCallback(RdbCallback):
  def __init__(self, out_filename, delimiter = ','):
    self.delimiter = delimiter
    self.outf = open(out_filename, 'w')

  def set(self, key, value, expiry, info):
    self.outf.write ("%s%s%s\n" % (str(key), self.delimiter, str(value)))

  def start_hash(self, key, length, expiry, info):
#    self.outf.write ("Hash %s has %s elements\n" % (str(key), str(length)))
    pass

  def hset(self, key, field, value):
    self.outf.write ("%s%s%s\n" % (str(key), self.delimiter, str(field)))

  def end_hash(self, key):
#    self.outf.write ("Hash %s finish\n" % (str(key)))
    pass

  def start_set(self, key, cardinality, expiry, info):
#    self.outf.write ("Set %s has %s elements\n" % (str(key), str(cardinality)))
    pass

  def sadd(self, key, member):
    self.outf.write ("%s%s%s\n" % (str(key), self.delimiter, str(member)))

  def end_set(self, key):
#    self.outf.write ("Set %s finish\n" % (str(key)))
    pass

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
