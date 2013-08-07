#!/usr/bin/env python

import sys
import optparse
from csv_callback import CsvCallback
from rdbtools import RdbParser

def main():

  parser = optparse.OptionParser()
  parser.add_option('-i', '--input', dest='rdb_file', help="input rdb file [REQUIRED]")
  parser.add_option('-o', '--output', dest='csv_file', help = "output csv file [REQUIRED]")
  parser.add_option('-c', '--column_delimiter', dest='column_delimiter',
                    help="column delimiter. Default is ctrl-A ('\\001')")
  parser.add_option('-l', '--line_delimiter', dest='line_delimiter',
                    help="row delimiter. Default is newline ('\\n')")
  parser.add_option('-p', '--pre_key', dest='pre_key',
                    help="columns before hash key. Default is empty")
  parser.add_option('-P', '--post_key', dest='post_key',
                    help="columns after hash key. Default is 'views clicks'")

  parser.set_defaults(column_delimiter='\001')
  parser.set_defaults(line_delimiter='\n')
  parser.set_defaults(pre_key='')
  parser.set_defaults(post_key='views clicks')
  options, remainder = parser.parse_args()

  if options.csv_file == None or options.rdb_file == None:
    parser.print_help()
    sys.exit(1)

  outf = open(options.csv_file, 'w')
  callback = CsvCallback(outf, options.pre_key.split(), options.post_key.split(),
                         options.column_delimiter, options.line_delimiter)
  parser = RdbParser(callback)
  parser.parse(options.rdb_file)
  outf.close()

if __name__ == "__main__":
  main()
