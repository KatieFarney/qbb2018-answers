#!/usr/bin/env python3

import sys
sam = open(sys.argv[1])

count = 0        
for i, line in enumerate(sam):
    if line.startswith("@)"):
        continue
    if "NH:i:1" in line:
        count += 1

print(count)