#!/usr/bin/bash

# Requires last, blast+, samtools 0.1.18 or samtools 0.1.19

readsfile=$1
databasefile=$2
lastindexfile=$3

lastal -s 2 -T 0 -Q 0 -a 1 $lastindexfile $readsfile > $readsfile.last.txt
maf-convert sam $readsfile.last.txt > $readsfile.sam

samtools view -T $databasefile -bS $readsfile.sam > $readsfile.bam
samtools sort $readsfile.bam $readsfile.bam.sorted
samtools index $readsfile.bam.sorted.bam

samtools mpileup -uf $databasefile $readsfile.bam.sorted.bam | bcftools view -cg - | perl vcfutils.pl vcf2fq > $readsfile.$databasefile.cns.fq

python fastq2fasta.py $readsfile.$databasefile.cns.fq $readsfile.$databasefile.cns.fasta
makeblastdb -in $databasefile -dbtype nucl
blastn -num_threads 8 -query $readsfile.$databasefile.cns.fasta -db $databasefile -max_target_seqs 1 -outfmt 5 > $readsfile.$databasefile.for.xml
blastn -num_threads 8 -query $readsfile -db $databasefile -outfmt 5 -max_target_seqs 1 > $readsfile.full.$databasefile.xml

makeblastdb -in $readsfile.$databasefile.cns.fasta -dbtype nucl
blastn -num_threads 8 -query $databasefile -db $readsfile.$databasefile.cns.fasta -max_target_seqs 1 -outfmt 5 > $readsfile.$databasefile.rev.xml

python tidyblastmin.py $readsfile.$databasefile.for.xml > frontway.txt
python tidyblastmin.py $readsfile.$databasefile.rev.xml > revway.txt
cat frontway.txt | sort -k3,3n > fway.txt
mv fway.txt frontway.txt
python tidyblastmax.py $readsfile.$databasefile.for.xml > totfrontway.txt
python BDBH.py > listofins
while read line; do grep $line totfrontway.txt; done < listofins | awk '{print($NF""$0)}' | sort -k1,1n -t' ' | cut -f1- -d' ' > finreadout.txt
cat finreadout.txt | uniq -c > finalreadout.txt
python tidyfinalout.py > Antibioticresistanceoutputfor.$readsfile.txt
