READ ME – miRNA and disease look-up database

# Description #

A command line tool for a local look-up database of the association between specified miRNAs and diseases, with the gene also given. Results can be filtered based on miRNA-gene confidence scores and gene-disease confidence scores. Any term searched or confidence filter applied is returned to the user, printed above the output table for readability as follows:


 
# To search up a specific miRNA
python3 database.py -s hsa 
 
# To search up a specific disease/word
python3 database.py -s dystrophy
 

## miRNA search 

Show specified miRNAs associated gene/disease without confidence scores
python3 database.py -m hsa-miR-940 
 
Show specified miRNAs associated gene/disease with miRNA confidence scores
python3 database.py -m hsa-miR-940 -smi 
 
Show specified miRNAs associated gene/disease with miRNA confidence scores > 90
python3 database.py -m hsa-miR-940 -smi 90
 
Show specified miRNAs associated gene/disease with disease confidence scores
python3 database.py -m hsa-miR-940 -sdis
 
Show specified miRNAs associated gene/disease with disease confidence scores > 90
python3 database.py -m hsa-miR-940 -sdis 90
 
Show specified miRNAs associated gene/disease with both miRNA confidence scores and disease confidence scores (x being any value to filter)
python3 database.py -m hsa-miR-940 -smi x -sdis x
 

## Disease search 

Please note: 1 word disease names must be inputted without quotations e.g. deafness; disease names > 1 word must be in quotations e.g. “stargardt disease”.

Show specified diseases associated miRNA/ gene without confidence scores
python3 database.py -d deafness 
 
Show specified diseases associated miRNA/gene with disease confidence scores
python3 database.py -d deafness -sdis
 
Show specified diseases associated miRNA/gene with disease confidence scores > 90
python3 database.py -d deafness -sdis 90
 
Show specified diseases associated miRNA/gene with miRNA confidence scores
python3 database.py -d deafness -smi
 
Show specified diseases associated miRNA/gene with miRNA confidence scores > 90
python3 database.py -d deafness -smi 90
 
Show specified diseases associated miRNA/gene with both miRNA confidence scores and disease confidence scores (x being any value to filter)
python3 database.py -d deafness -sdis x -smi x
 
