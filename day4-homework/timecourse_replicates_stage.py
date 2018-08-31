#!/usr/bin/env python3
"""
Usage: timecourse_replicates.py <gene_name> <samples.csv> <ctab_dir>
Create a timecourse of a given transcript (FBtr0331261) for females

./03-timecourse.py FBtr0331261 ~/qbb2018/samples.csv ~/data/results/stringtie/

"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[2])

def getFPKMs(sex, df):
    soi = df.loc[:,"sex"] == sex
    df = df.loc[soi,:]
    stage2 = []
    fpkms = []
    for index, sample, sex, stage in df.itertuples():
        filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
        ctab_df = pd.read_table(filename, index_col="t_name")
        #print(ctab_df)
        fpkms.append(ctab_df.loc[sys.argv[1],"FPKM"])
        stage2.append(stage)
    return fpkms, stage2
    
male_fpkms, stage = getFPKMs('male', df)
fem_fpkms, stage = getFPKMs('female', df)


fig, ax = plt.subplots()
ax.plot(male_fpkms)
ax.plot(fem_fpkms)
ax.set_xticklabels(stage)
ax.set_xlabel("stage")                      # Label the x axis
ax.set_ylabel("FPKMs")                       # Label the y axis
plt.xticks(rotation=90)
ax.legend(bbox_to_anchor=(1.05,0.5), loc= 2, borderaxespad= 0., labels= ['Females', 'Males'])
ax.set_title("FPKM Values")
plt.tight_layout()
fig.savefig("timecourse_male-female_stage.png")
plt.close(fig)




