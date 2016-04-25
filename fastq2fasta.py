#!/usr/bin/python

from Bio import SeqIO
import sys

infile = sys.argv[1]
inf = open(infile, "r")
outfile = sys.argv[2]
outf = open(outfile, "w")

SeqIO.convert(inf, 'fastq', outf, 'fasta')

inf.close()
outf.close()
