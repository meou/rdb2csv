#!/usr/bin/env python

import sys
import getopt
from csv_callback import CsvCallback
from rdbtools import RdbParser

def ok_exit():
  usage()
  sys.exit(0)

def error_exit():
  usage()
  sys.exit(1)

def usage():
  print 'rdb2csv.py -i <input rdb file> -o <output csv file> [-d <column delimiter>]'

def main(argv):

  try:
    opts, args = getopt.getopt(argv,"hi:o:d:")
  except getopt.GetoptError:
    error_exit()

  rdb_file = ""
  csv_file = ""
  delimiter = ';'
  for opt, arg in opts:
    if opt == '-h':
      ok_exit()
    elif opt == '-i':
      rdb_file = arg
    elif opt == '-o':
      csv_file = arg
    elif opt == '-d':
      delimiter = arg
    else:
      error_exit()

  if (rdb_file == "") or (csv_file == ""):
    error_exit()

  callback = CsvCallback(csv_file, delimiter)
  parser = RdbParser(callback)
  parser.parse(rdb_file)

if __name__ == "__main__":
  main(sys.argv[1:])
