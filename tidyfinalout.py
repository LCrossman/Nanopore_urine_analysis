#!/usr/bin/python

import sys
import math
import operator
d = {}
e = {}
ctx = {}
def keywithmaxval(dict):
    return max(dict.iterkeys(), key=lambda k: dict[k])

infile = open("finalreadout.txt", "r")

for line in infile:
    elements = line.split("\t")
    print "%s: %s, bitscore = %i"%(elements[1], elements[2], int(elements[3]))
    if 'TEM' in elements[2]:
      try:
         d[elements[2]]=[int(elements[3])]
      except:
         print "whoops"
    if 'NDM' in elements[2]:
      try:
         e[elements[2]]=[int(elements[3])]
      except:
         print "e error"
    if 'CTX' in elements[2]:
       try:
         ctx[elements[2]]=[int(elements[3])]
       except:
         print "ctx error"

TEM = '\n'.join([key for key,value in d.iteritems() if value == max(d.values())])
if TEM:
   print "highest scoring TEM (or two TEMs if the score is identical):\n%s"%TEM
NDM = '\n'.join([key for key, value in e.iteritems() if value == max(e.values())])
if NDM:
   print "highest scoring NDM:\n%s"%NDM
CTX = '\n'.join([key for key, value in ctx.iteritems() if value == max(ctx.values())])
if CTX:
   print "highest scoring CTX:\n%s"%CTX




    
