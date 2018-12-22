#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor
Histogram plot for yeast VCF file
Input = BYxRM_segs_saccer3.bam.simplified.vcf
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

vcf_file = open(sys.argv[1])
allele_freq = []

for line in vcf_file:
    if line.startswith("#"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    AF_values = fields[7][3:]
    AF_value = AF_values.split(",")
    AF_value[0]
    for line in AF_value:
        allele_freq.append(float(line))

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(allele_freq, bins=1000, color="purple")
ax.set_title("Yeast Allele Frequency")
ax.set_xlabel("Allele Frequency")
ax.set_ylabel("Frequency")  

fig.savefig("yeast_hist.png")          
plt.close(fig)  
        

