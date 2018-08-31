#!/usr/bin/env python3
"""
Usage: MA-plot.py <sample1/t_data.ctab> <sample2/t_data.ctab>

"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import math

name1 = sys.argv[1].split(os.sep)[-2]
fpkm1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name").loc[:,"FPKM"]
#log_fpkm1 = np.log(fpkm1+1)

name2 = sys.argv[2].split(os.sep)[-2]
fpkm2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name").loc[:,"FPKM"]
#log_fpkm2 = np.log(fpkm2+1)
#y = log2(mut/wt)
#x = log2(sqrt(wt*mut))

average = (np.log2(fpkm1+1) + np.log2(fpkm2+1))/2
ratio = np.log2((fpkm1+1)/(fpkm2+1))

fig, ax = plt.subplots()
ax.scatter(average, ratio, alpha=0.1)
ax.set_xlabel("Average")                      # Label the x axis
ax.set_ylabel("Ratio")                       # Label the y axis
ax.set_title("FPKM1 vs FPKM2 MA-Plot")
fig.savefig("fpkms_MAplot.png")
plt.close(fig)
