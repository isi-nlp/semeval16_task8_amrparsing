#! /usr/bin/env python
import argparse
import sys
import codecs
from itertools import izip
from collections import defaultdict as dd
import re
import os.path
scriptdir = os.path.dirname(os.path.abspath(__file__))


def main():
  parser = argparse.ArgumentParser(description="Deterministic, input-agnostic baseline parser based on a perl version by Ulf Hermjakob. Assumes one-input-per-line. Prints smatch-scorable results",
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--infile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input file")
  parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output file")



  try:
    args = parser.parse_args()
  except IOError, msg:
    parser.error(str(msg))

  reader = codecs.getreader('utf8')
  writer = codecs.getwriter('utf8')
  infile = reader(args.infile)
  outfile = writer(args.outfile)


  for line in infile:
    outfile.write("# ::snt %s" % line)
    outfile.write("(s / state-01 :ARG0 (p / person :ARG0-of (h / have-org-role-91 :ARG1 (c / country :name (n / name)) :ARG2 president) :name (n2 / name)) :ARG1 (a / and :op1 (w / want-01 :ARG0 (p2 / person) :ARG1 (d / do-02 :ARG0 p2)) :op2 (p3 / person :mod (c2 / country :name (n3 / name)))) :time (d2 / date-entity :year 2007))\n\n")

if __name__ == '__main__':
  main()

