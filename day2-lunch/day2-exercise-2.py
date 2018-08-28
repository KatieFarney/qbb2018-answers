#!/usr/bin/env python3


import sys
sam = open(sys.argv[1])

#with open("/Users/cmdb/qbb2018-answers/day1-homework/SRR072893/SRR072893.sam", "r") as sam:
#f = open("/Users/cmdb/qbb2018-answers/day1-homework/SRR072893/SRR072893.sam", "r")
count = 0        
for i, line in enumerate(sam):
    if line.startswith("@)"):
        continue
    if "XM:i:0" in line:
        count += 1
#    fields = line.rstrip("\r\n").split("\t")
#    for field in fields:
#        if field.startswith("XM:i:0"):
#            count += 1

            #print(len(fields))
#    if i > 200:
#        break
    # if fields[15] == "XM:i:0":
    #     print(fields)

#    else:
#        count += 1
print(count)

