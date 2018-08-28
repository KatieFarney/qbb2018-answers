#!/usr/bin/env python3

import sys
sam = open(sys.argv[1])

count = 0        
for i, line in enumerate(sam):
    if line.startswith("SRR072893"):
        fields = line.rstrip("\r\n").split("\t")
        #print(fields[2])
        count += 1
        if count <= 10:
            print(fields[2])
        else:
            break    
        
        #if fields[1] == "4":

##    if "NH:i:1" in line:
#        count += 1

##print(count)