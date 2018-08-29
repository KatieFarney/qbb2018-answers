#!/usr/bin/env python3
#Requires two arguments to run

import sys

UniProt_FlyBase = {}
fly = set()

#open uniprot_flybase.txt as arg 1  
for line in open(sys.argv[1]):
    fly = line.strip("\r\n").split()
    key = fly[0]
    value = fly[1]
    UniProt_FlyBase[key] = value

#open ~/data/results/stringtie/SRR072893/t_data.ctab as arg 2
for line in open(sys.argv[2]):
    fields = line.strip("\r\n").split("\t")
    Flybase_id = fields[8]
    if Flybase_id in UniProt_FlyBase:
        Uniprot_id = UniProt_FlyBase[Flybase_id]
        print(Uniprot_id + " " + line.rstrip())
#if no matching StringTie entry, UniProt ID will appear as "Unknown"      
    else:
        print("Unknown" + " " + line.rstrip())