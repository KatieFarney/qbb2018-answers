#!/usr/bin/env python3

"""
./motif_intersect_all.py meme_parsed.txt

"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

meme_dict = {}

for line in open(sys.argv[1]):
    fields = line.rstrip("\t").split()
    offset = float(fields[2])
    if offset not in meme_dict:
        meme_dict[offset] = 1
    else:
        meme_dict[offset] += 1
        
fig, ax = plt.subplots()
for key in meme_dict:
    plt.scatter([key], meme_dict[key])

ax.set_xlabel("Distance")
ax.set_ylabel("Number of Motifs")
ax.set_title("Motif Positions")
fig.savefig("motif_plot.png")
plt.close()