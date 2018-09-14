#!/usr/bin/env python3

"""
Usage: ./aa_to_nt.py <seqs.fa> <seqs_pep_mafft.fa>

convert aligned amino acids to aligned nucleotide sequences
"""

import sys
import fasta
import itertools
import Bio
from Bio.codonalign import CodonSeq
from Bio.Seq import Seq
from Bio.codonalign import default_codon_alphabet, CodonSeq, CodonAlignment
from Bio import AlignIO
from Bio.codonalign.codonseq import cal_dn_ds
import matplotlib.pyplot as plt

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
        nt = dna[j*3:(j+1)*3]
        if a == "-":
            nuclist.append("---")
        else:
            nuclist.append(nt)
            j += 1
    #dna_seq = "".join(nuclist)
    all_nucs.append(nuclist)
    all_aa.append(aa_list)
    
#print(all_nucs)
#print(all_aa)
# dN, dS = cal_dn_ds(all_aa, all_nucs, method='NG86')
# print(dN, dS)


query_aa = all_aa[0]
query_dna = all_nucs[0]

dS_count = [0] * len(query_aa)
dN_count = [0] * len(query_aa)
count = [0] * len(query_aa)

for codon_list, aa_list in zip(all_nucs[1:], all_aa[1:]):
    for i in range(0, len(codon_list)):
            if codon_list[i] != query_dna[i]:
                count[i] += 1
                if aa_list[i] == query_aa[i]:
                    dS_count[i] += 1
                else:
                    dN_count[i] += 1

differences = []
for i in range(len(dS_count)):
    difference = (dN_count[i] - dS_count[i])
    differences.append(difference)

ratios = []
for i in range(len(dS_count)):
    ratio = (dN_count[i])/(dS_count[i] + 1)
    ratios.append(ratio)
    

print("number of codons = " + str(len(query_dna)))
print("number of AAs = " + str(len(query_aa)))
print("nuc alignments = " + str(len(all_nucs)))
print("aa alignments = " + str(len(all_aa)))
print("dN count = " + str(len(dN_count)))
print("dS count = " + str(len(dS_count)))
print("nonsynonymous muts = " + str(sum(dN_count)))
print("synonymous muts = " + str(sum(dS_count)))
print("synonymous + nonsynonymous = " + str(sum(dS_count) + sum(dN_count)))

fig, ax = plt.subplots(figsize=(20, 8))
ax.scatter(differences, ratios) 

ax.set_xlabel("Difference")
ax.set_ylabel("dN/dS ratio")
ax.set_title("Ratio of Nonsynonymous and Synonymous Mutations")
#ax.legend(bbox_to_anchor=(1.01,0.52), loc=2, borderaxespad=0.)
plt.tight_layout()
fig.savefig("dN_dS.png")
plt.close(fig)





