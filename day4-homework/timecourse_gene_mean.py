#!/usr/bin/env python3
"""
Usage: timecourse_replicates.py <gene_name> <samples.csv> <ctab_dir>

./timecourse_replicates_stage_gene-name_v2.py Gfat1 ~/qbb2018/samples.csv ~/data/results/stringtie/

"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

samples = sys.argv[2]

def getFPKMs(sex):
    df = pd.read_csv(samples)
    soi = df.loc[:,"sex"] == str(sex)
    df = df.loc[soi,:]

    fpkms = []
    mean_fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col="t_name")
        roi = ctab_df.loc[:,"gene_name"] == sys.argv[1]
        #print(ctab_df)
        fpkms.append(ctab_df.loc[roi,"FPKM"])
        mean_fpkms.append(np.mean(fpkms))

    return mean_fpkms
    
male_fpkms = getFPKMs('male')
fem_fpkms = getFPKMs('female')


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
ax.set_title(str(sys.argv[1]))
plt.tight_layout()
fig.savefig((sys.argv[1]) + "_timecourse_mean_FPKM.png")
plt.close(fig)




