#!/usr/bin/env python3

import sys
import fasta

target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])
#k = 11

reader = fasta.FASTAReader(target)#query
reader2 = fasta.FASTAReader(query)
    
kmers = {}
target_dict = {}

for ident, sequence in reader:
    for pos in range(0, len(sequence) - k):
        kmer = sequence[pos:pos+k]
        if kmer not in target_dict:
            target_dict[kmer] = [(ident, pos)]
        else:    
            target_dict[kmer].append((ident, pos))
for ident, sequence in reader2:
    for pos2 in range(0, len(sequence) - k):
        kmer2 = sequence[pos2:pos2+k]
        if kmer2 in target_dict.keys():
            for hit in target_dict[kmer2]:
                for match in target_dict[kmer2]:
                    print("Gene Name: ", match[0], "Target Start: ", match[1], "Query Start: ", pos2, "Kmer Sequence: ", kmer2) 
        #else:    
            ##continue
            #target_dict[kmer].append((ident, pos))

#for key in target_dict:
#    print(key, target_dict[key])


    


    