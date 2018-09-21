#!/usr/bin/env python3

"""
Usage: ./count_contigs.py <contigs.fasta>

"""

import sys
import fasta

contigs_file = fasta.FASTAReader(open(sys.argv[1]))
num_contigs = 0
contig_lengths = []

for ident, sequence in contigs_file:
    num_contigs += 1
    contig_lengths.append(len(sequence))

contig_lengths.sort(reverse=True)
print("Total # of contigs = " + str(num_contigs))
print("Min contig length = " + str(contig_lengths[-1]))
print("Max contig length = " + str(contig_lengths[0]))
print("Avg contig length = " + str(sum(contig_lengths)/num_contigs))

half_length = sum(contig_lengths)/2
counter = 0

for i, length in enumerate(contig_lengths):
    if counter >= half_length:
        print("n50 = " + str(contig_lengths[i-1]))
        break
    else:
        counter += length

