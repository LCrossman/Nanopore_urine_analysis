Speedy Urine analysis and antibiotic resistance searches for Nanopore data

For identification of the organism, 

1. urine_search.sh Nanoporefastareadsfile
2. in the same directory as urine_search.sh run Urinereport.py

The following scripts need to be in the path:
blast_separate_taxa.pl
blast_taxonomy_report.pl

To identify genes that encode antibiotic resistance genes,

1. sh consAntifile.sh Nanoporefastareadsfile resistancegenedatabasefile lastindexfile

consAntifile.sh has the dependencies last, blast+, and samtools 0.1.18 or 0.1.19
The following scripts also need to be in the path:
fastq2fasta.py
BDBH.py
tidyblastmin.py
tidyblastmax.py
tidyfinalout.py

1. lastdb -Q 0 resistancegenesdatabasefile
2. sh consAntifile.sh 

A suitable antibiotic resistance database to search would be the Comprehensive Antibiotic Resistance Database
(https://card.mcmaster.ca/about)
For the use of the nanopore searches only, a dereplicated subset of these genes is provided in this repository, 
AR-genes_subset_dereplicated.fa

If there are non-unique filenames in the first id field of the extracted nanopore fasta files, script rename_fasta_fast5.py will rename the first field to create unique names.

Disclaimer:
Materials on this site are provided "as is" without warranties or conditions of any kind expressed or implied.
The software is not permitted for use in relation to patient management or in relation to clinical trials.
The software makes use of the BLAST parameter max_target_seqs which has been described as a parameter of BLAST found within hundreds of papers workflows, however, it can give rise to unexpected results in a situation where the top hit in some circumstances may not specifically be the best hit returned.  This workflow was formulated for use on early MAP MinION data.  These data were specifically not of high accuracy (of the order of 80% accurate).  Therefore the author feels that the use of max_target_seqs was justified in this instance to identify antibiotic resistance genes as well as possible given the data accuracy.  Newer sets of MinION Oxford Nanopore data are of higher accuracy and any author looking to use this workflow should look again at this parameter.  (relating to: Shah et al., 2018, Bioinformatics:  https://doi.org/10.1093/bioinformatics/bty833) 
