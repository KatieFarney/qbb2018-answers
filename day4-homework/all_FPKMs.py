#!/usr/bin/env python3

"""
Usage: ./all_FPKMs.py <samples.csv> <ctab dir>

merge FPKM values from all ctab files
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])

compiled= {}

for index, sample, sex, stage in df.itertuples():
   filename = os.path.join(sys.argv[2], sample, "t_data.ctab")

   ctab_df = pd.read_table(filename, index_col="t_name")

   compiled[sex + "_" + stage] = ctab_df.loc[:, "FPKM"]

compiled_df = pd.DataFrame(compiled)
compiled_df.to_csv(sys.stdout)