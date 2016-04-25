#!/usr/bin/bash

readsfile=$1

echo $readsfile

time blastn -num_threads 8 -task megablast -query $readsfile -db nt_Proteobacteria -max_target_seqs 1 -outfmt 6 -out $readsfile.Proteobacteria.nt

echo "completed Proteobacteria searches"

time blastn -num_threads 8 -task megablast -query $readsfile -db nt_Human -max_target_seqs 1 -outfmt 6 -out $readsfile.Human.nt

echo "completed Human searches"

time blastn -num_threads 8 -task megablast -query $readsfile -db nt_Firmicutes -max_target_seqs 1 -outfmt 6 -out $readsfile.Firmicutes.nt

echo "completed Firmicutes searches"

cat $readsfile.Human.nt | awk '{print $2}' | sort | uniq -c | sort -k1n > $readsfile.Human.strains

cat $readsfile.Firmicutes.nt | awk '{print $2}' | sort | uniq -c | sort -k1n > $readsfile.Firmicutes.strains

cat $readsfile.Proteobacteria.nt | awk '{print $2}' | sort | uniq -c | sort -k1n > $readsfile.Proteobacteria.strains

echo "strains files complete"

time perl blast_separate_taxa.pl -d 50 -b1 $readsfile.Proteobacteria.nt -b2 $readsfile.Human.nt

echo "taxa separate files made"

echo "making taxonomy report files"

time perl blast_taxonomy_report.pl -blast $readsfile.Proteobacteria.nt -nodes nodes.dmp -names names.dmp -gi_taxid_file gi_taxid_nucl.dmp.gz > $readsfile.Proteobacteria.nt.taxon

echo "Proteobacteria taxon file ready"

awk '{print $6, $7}' $readsfile.Proteobacteria.nt.taxon | sort | uniq -c | sort -k1n > $readsfile.Prot.taxa

echo "completed counts of taxa file on hand"
