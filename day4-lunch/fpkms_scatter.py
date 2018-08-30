#!/usr/bin/env python3

"""
Usage: ./fpkms_scatter.py <sample1/t_data.ctab> <sample2/t_data.ctab>
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

name1 = sys.argv[1].split(os.sep)[-2]
fpkm1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name").loc[:,"FPKM"]
log_fpkm1 = np.log(fpkm1+1)

name2 = sys.argv[2].split(os.sep)[-2]
fpkm2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name").loc[:,"FPKM"]
log_fpkm2 = np.log(fpkm2+1)
#print(log_fpkm1)

fig, ax = plt.subplots()
ax.scatter(log_fpkm1, log_fpkm2, alpha=0.1)
ax.set_xlabel("SRR072893")                      # Label the x axis
ax.set_ylabel("SRR072915")                       # Label the y axis
ax.set_title("FPKM Values")
fig.savefig("fpkms_scatter_log.png")
plt.close(fig)


