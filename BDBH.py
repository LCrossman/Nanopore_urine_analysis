#!/usr/bin/python

import sys
import operator
d = {}
e = {}
def keywithmaxval(d):
    v=list(d.values()[1])
    k=list(d.keys())
    return k[v.index(max(v))]

def searchFor(dict, val):
   for k,v in dict.items():
      vl = ''.join(val)
      if vl in k:
         return ''.join(vl)


revfile = open("revway.txt", "r")
forfile = open("frontway.txt", "r")

for line in revfile:
    rev = line.split("\t")
    try:
      d[rev[0]]=[rev[1]]
    except:
       print "error"

for elem in forfile:
    fors = elem.split("\t")
    try:
      e[fors[0]] = [fors[1]]
    except:
      print "incorrect"

for key, value in d.items():
    ans = searchFor(e,value)
    try:
       if key in ans:
          print key
    except:
       pass


