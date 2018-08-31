#!/usr/bin/env python3

"""
Usage: ./promotor-region.py <sample1/t_data.ctab> 
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#filename = sys.argv[1].split(os.sep)[-2]

df = pd.read_table(sys.argv[1])
trans_start = df.loc[:,"start"]
start_promo = []
end_promo = []

for item in trans_start:
    if item <= 499:
        start_promo.append(0)
        end_promo.append(0)
    else:
        start_promo.append(item - 500)
        end_promo.append(item + 500)

#start_promo = trans_start - 500
#end_promo = trans_start + 500

df2 = pd.DataFrame (
    {"chromosome" : df.loc[:,"chr"], 
    "start" : start_promo,
    "end" : end_promo,
    "t_name" : df.loc[:,"t_name"]}
)
df2.to_csv(sys.stdout, sep="\t")  



#tail -n+2 .bed |cut -f 2,3,4 > new.bed

# coi = df.loc[:,"start"]
# trans_start = []
#
# df = df.loc[coi,:]
#
# for index, sample, sex, stage in df.itertuples():
#     filename = os.path.join(sys.argv[3], sample, "t_data.ctab")
#     ctab_df = pd.read_table(filename, index_col="t_name")
#     #print(ctab_df)
#     fpkms.append(ctab_df.loc[sys.argv[1],"FPKM"])


