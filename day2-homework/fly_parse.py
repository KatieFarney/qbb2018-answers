#!/usr/bin/env python3

import sys

#input = UniProt fly.txt

for line in open(sys.argv[1]):
    if "DROME" in line:
        fields = line.strip("\r\n").split()
        if len(fields) == 4:
            print(fields[3], fields[2])