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

poly_fpkm = np.polyfit(log_fpkm1, log_fpkm2, 1)

#x = np.linspace( minimum val, max val)
x = np.linspace(0.000, 8, num=100)


#x = np.linspace(0, 1000, 50)
#print(x)
y = np.poly1d(poly_fpkm)
# print(type(y))
# exit()
#for i in range(120):
print(y(x))


fig, ax = plt.subplots()
ax.scatter(x, y(x))
#ax.scatter(x, y)
ax.scatter(log_fpkm1, log_fpkm2, alpha=0.1)
ax.set_xlabel("SRR072893")                      # Label the x axis
ax.set_ylabel("SRR072915")                       # Label the y axis
ax.set_title("FPKM Values")
fig.savefig("fpkms_scatter_poly_testlog.png")

plt.close(fig)


