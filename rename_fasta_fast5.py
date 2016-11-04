#!/usr/bin/python

#From poretools output alter the fasta id name to longer name - required if the fasta id names are not unique


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

sequences = []
handle = open(sys.argv[1], 'r')
outfile = open(sys.argv[1]+".out", 'w')

records = list(SeqIO.parse(handle,"fasta"))

for rec in records:
    newid = rec.description.split('/')
    nid = newid[-1]
    passid = nid[:-6]
    rec.id = passid
    print rec.id
    sequences.append(rec)

SeqIO.write(sequences, outfile, "fasta")
