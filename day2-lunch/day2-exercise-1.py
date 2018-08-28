#!/usr/bin/env python3


import sys
sam = open(sys.argv[1])

#with open("/Users/cmdb/qbb2018-answers/day1-homework/SRR072893/SRR072893.sam", "r") as sam:
#f = open("/Users/cmdb/qbb2018-answers/day1-homework/SRR072893/SRR072893.sam", "r")
count = 0        
for i, line in enumerate(sam):
    if line.startswith("@)"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    ##print(fields)
    if fields[1] == "4":
        continue
    else:
        count += 1
print(count)

