#!/usr/bin/python
from __future__ import division
import sys
import re
from Bio import SeqIO
import shutil
import math
import numpy
sizes = []
count = 0

def median(lst):
   return numpy.median(numpy.array(lst))

report = open("UrineAnalysisReport", "w")

infile = sys.argv[1]
ident = sys.argv[2]
hand = open(infile, 'r')

report.write('Report of %s\n'%infile)
report.write('This is the automated report of Urine Bacterial content analysis\n')
report.write('\n\n\n\n')

#for line in hand:
#   if line.startswith('>'):
#      count +=1
#report.write('There are %i 2D reads in the file\n'%count)
l = SeqIO.parse(hand, "fasta")
sortedList = [s for s in sorted(l, key=lambda x : len(x))]
for s in sortedList:
   sizes.append(len(s.seq))
   
report.write('Number of reads: %i\n'%len(sizes))
report.write('Maximum readlength: %i bp\n'%max(sizes))
report.write('Minimum readlength: %i bp\n'%min(sizes))
report.write('Total bp: %i bp\n'%sum(sizes))
report.write('Mean readlength: %.1f\n'%(sum(sizes)/len(sizes)))
med = median(sizes)
report.write('Median readlength: %.1f\n\n'%(med))
with open(ident+'.Proteobacteria.nt') as P:
   hits = sum(1 for elem in P)
print hits
report.write('There are %i total hits to Proteobacteria\n'%hits)
with open(ident+'.Human.nt') as N:
   numbers = sum(1 for el in N)
print numbers
report.write('There are %i total hits to Human\n'%numbers)
with open(ident+'.Firmicutes.nt') as F:
   totals = sum(1 for e in F)
print totals
report.write('There are %i total hits to Firmicutes\n'%totals)
with open(ident+'.Proteobacteria.nt.only') as o:
   nums = sum(1 for item in o)
print nums
report.write('Hitting Proteobacteria better: %i reads\n'%nums)
with open(ident+'.Human.nt.only') as H:
   hums = sum(1 for it in H)
print hums
report.write('Hitting Human better: %i reads\n\n'%hums)
per = (nums/(nums+hums))*100
report.write('There is an approximate percentage of %.1f %% Proteobacterial reads\n'%per)
with open(ident+'.Prot.taxa') as Tax:
    element = Tax.readlines()
    report.write(''.join(element))
#         if int(element[-1][0]) > (int(element[-2][0])+200):
    report.write('the organism is most likely: %s'%element[-1][4:])
with open(ident+'.Proteobacteria.strains') as f:
   lines = f.readlines()
   if lines:
         third = lines[-3]
         second = lines[-2]
         first = lines[-1]
report.write('\n\nThese are the main strains present: \n\n%s\n%s\n%s\n'%(third,second,first))

report.write('\n\n\n\n\n')
report.write('ENDS')
