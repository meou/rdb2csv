#!/usr/bin/env python

import sys
from rdbtools import RdbParser, RdbCallback

class CsvCallback(RdbCallback):
  def __init__(self, delimiter = ','):
    self.delimiter = delimiter

  def unsupported():
    print ("unsupported")

  def set(self, key, value, expiry, info):
    print ("%s%s%s" % (str(key), self.delimiter, str(value)))

  def start_hash(self, key, length, expiry, info):
    unsupported()
    
  def hset(self, key, field, value):
    unsupported()
    
  def hset(self, key, field, value):
    unsupported()
    
  def end_hash(self, key):
    unsupported()
    
  def start_set(self, key, cardinality, expiry, info):
    unsupported()
    
  def sadd(self, key, member):
    unsupported()
    
  def end_set(self, key):
    unsupported()

  def start_list(self, key, length, expiry, info):
    unsupported()

  def rpush(self, key, value):
    unsupported()
  
  def end_list(self, key):
    unsupported()
  
  def start_sorted_set(self, key, length, expiry, info):
    unsupported()  

  def zadd(self, key, score, member):
    unsupported()

  def end_sorted_set(self, key):
    unsupported()

callback = CsvCallback(';')
parser = RdbParser(callback)
parser.parse('/Users/jscw/Yahoo/dump.rdb')

