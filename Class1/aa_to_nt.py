#!/usr/bin/env python3

"""
Usage: ./aa_to_nt.py <seqs.fa> <seqs_pep_mafft.fa>

convert aligned amino acids to aligned nucleotide sequences
"""

import sys
import fasta
import itertools

dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))

all_nucs = []
all_aa = []
for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader): # zip parses 2 files at once
    nuclist = []
    aa_list = []
    #print(aa)
    j = 0
    for i in range(len(aa)):
        a = aa[i]
        aa_list.append(a)
        nt = dna[j*3:(j*3)+3]
        if a == "-":
            nuclist.append("---")
        else:
            nuclist.append(nt)
            j += 1
    #dna_seq = "".join(nuclist)
    all_nucs.append(nuclist)
    all_aa.append(aa_list)
    
#print(all_nucs)
print(all_aa)
