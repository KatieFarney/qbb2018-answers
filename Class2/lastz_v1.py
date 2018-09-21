#!/usr/bin/env python3

"""
Uasge: ./lastz_v1.py lastz_sort.out

"""

import sys
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

f = open(sys.argv[1], 'r')

lines = f.readlines()
fig, ax = plt.subplots(figsize=(25, 10))
x_pos = 0

for line in lines:
    lines = line.rstrip('\r\n').split("\t")
    if line.startswith('#score'):
        continue
    else:
        start = int(lines[4])
        end = int(lines[5])
        length = end - start
        #print(length)
        
        x = np.linspace(x_pos,x_pos+length)  
        y = np.linspace(start,end)
        ax.plot(x, y)
        x_pos += length

ax.set_xlabel("Contigs")
ax.set_ylabel("Reference Sequence Position")
ax.set_title("Spades High Contigs")
fig.savefig("Spades_High_Contigs.png")
plt.close(fig)
        