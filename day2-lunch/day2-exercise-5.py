#!/usr/bin/env python3

import sys
sam = open(sys.argv[1])

count = 0  
mapq_sums = 0      
for i, line in enumerate(sam):
    if line.startswith("SRR072893"):
        fields = line.rstrip("\r\n").split("\t")
        #print(fields[4])
        mapq = int(fields[4])
        count += 1
        mapq_sums += mapq
        
        average = mapq_sums/count
print(average)