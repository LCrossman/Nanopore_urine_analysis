#!/usr/bin/python

import sys
from Bio import SearchIO

infile = sys.argv[1]
hand = open(infile, "r")

hitname = []
i = 0

blast_qresult = list(SearchIO.parse(hand, "blast-xml"))


for hit in blast_qresult:
   if len(hit) > 0:
      for hsp in hit:
         for h in hsp:
             if h.hit_description not in hitname:
                 if h.bitscore > 500:
                    print "%s\t%s\t%s\t%i\t"%(h.query_id, h.hit_id, h.hit_description, h.bitscore)
                    hitname.append(h.hit_description)
             else:  
               pass




