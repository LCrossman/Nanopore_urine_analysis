Speedy Urine analysis and antibiotic resistance searches for Nanopore data

For identification of the organism, 

1. urine_search.sh Nanoporefastareadsfile
2. in the same directory as urine_search.sh run Urinereport.py

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
For the use of the nanopore searches only, a dereplicated subset of these genes is provided in this repository.

Disclaimer:
Materials on this site are provided "as is" without warranties or conditions of any kind expressed or implied.
The software is not permitted for use in relation to patient management or in relation to clinical trials.

