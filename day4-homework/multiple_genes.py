#!/usr/bin/env python3
"""
Usage: timecourse_replicates.py <samples.csv> <ctab_dir> <gene_name> <gene_name> ...

./multiple_genes.py ~/qbb2018/samples.csv ~/data/results/stringtie/ Sxl msl-2 run sisA

"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

genes = []
for item in sys.argv[3:]:
    genes.append(item)

samples = sys.argv[1]

def getFPKMs(sex, gene):
    df = pd.read_csv(samples)
    soi = df.loc[:,"sex"] == str(sex)
    df = df.loc[soi,:]

    fpkms = []
    mean_fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col="t_name")
        roi = ctab_df.loc[:,"gene_name"] == gene
        #print(ctab_df)
        fpkms.append(ctab_df.loc[roi,"FPKM"])
        mean_fpkms.append(np.mean(fpkms))

    return mean_fpkms

for name in genes:
        
    male_fpkms = getFPKMs('male', name)
    fem_fpkms = getFPKMs('female', name)


    fig, ax = plt.subplots()
    ax.plot(male_fpkms)
    ax.plot(fem_fpkms)
#fig.subtitle("%s" %(sys.argv[1])


    ax.set_xlabel("Stage")                      # Label the x axis
    ax.set_ylabel("Mean FPKM")                       # Label the y axis
    my_xticks = ["9", "10","11","12","13","14A","14B","14C","14D"]
    ax.set_xticklabels(my_xticks)
    plt.xticks(rotation=90)
    ax.legend(bbox_to_anchor=(1.05,0.5), loc= 2, borderaxespad= 0., labels= ['Females', 'Males'])
    ax.set_title(name)
    plt.tight_layout()
    fig.savefig((name) + "_timecourse_mean_FPKM.png")
plt.close(fig)
