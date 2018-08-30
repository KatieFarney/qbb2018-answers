#!/usr/bin/env python3

#3R:21,378,950
import sys
        
find_pos = int(21378950)
gene_start = 0
gene_end = 0
my_dist = 0
prot_code = {}
nonprot_code = {}

for i, line in enumerate( open( sys.argv[1] ) ):
    if i <= 5:
        continue
    fields = line.rstrip("\r\n").split("\t")
    read_type = fields[2]
    chrom = fields[0]
    gene_start = int(fields[3])
    gene_end = int(fields[4])
    gene_id = fields[8]
     
    if chrom == "3R" and read_type == "gene":
        if "protein_coding" in fields[8]:
            fields = line.rstrip("\r\n").split()
            gene_biotype = fields[17]
             
            if find_pos < gene_start:
                my_dist = gene_start - find_pos
                 
            elif find_pos > gene_end:
                my_dist = find_pos - gene_end
                prot_code[gene_id] = my_dist 
             
        else:    
            fields = line.rstrip("\r\n").split()
            gene_biotype = fields[17]
            if find_pos < gene_start:
                my_dist = gene_start - find_pos
             
            elif find_pos > gene_end:
                my_dist = find_pos - gene_end
                nonprot_code[gene_id] = my_dist

prot_code_sorted = sorted(prot_code.items(), key=lambda x:x[1])
min_line, min_dist = prot_code_sorted[0]
print("Closest protein-coding gene: " + min_line[9:19], min_dist)

nonprot_code_sorted = sorted(nonprot_code.items(), key=lambda x:x[1])
min_line, min_dist = nonprot_code_sorted[0]
print("Closest non-coding gene: " + min_line[9:19], min_dist)
        