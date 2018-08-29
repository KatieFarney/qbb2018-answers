#!/usr/bin/env python3

import sys

count = 0
for line in open(sys.argv[1]):
    if line.startswith("#!"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    #count += 1
    if fields[2] == "gene":
        if "protein_coding" in line:
            count += 1
        
print(count)
