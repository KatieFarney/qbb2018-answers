#!/usr/bin/env python3

import sys

gene_types = {}
biotype = {}
            
for i, line in enumerate(open(sys.argv[1])):
    if line.startswith("#!"):
        continue
    fields = line.rstrip("\r\n").split()
    #print(fields)
    #break
    for columns in range(8,len(fields)):
        if fields[columns] == "gene_biotype":
            #print(fields[columns])
            #break
            gene_types = fields[columns + 1]
            if gene_types in biotype:
                biotype[gene_types] += 1
            else:
                biotype[gene_types] = 1


##for name in gene_name_counts:
 #   print(name, gene_name_counts[name])
 
for name, value in biotype.items():
     print(name, value)