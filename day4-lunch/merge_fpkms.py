#!/usr/bin/env python3

"""
Usage: ./day4-lunch-exercise1.py <thresh> <sample1/t_data.ctab> <sample2/t_data.ctab>
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

threshold = float(sys.argv[1])

fpkms = {}
for filename in sys.argv[2:]:
    name = filename.split(os.sep)[-2]
    fpkm = pd.read_csv(filename, sep="\t", index_col="t_name").loc[:,"FPKM"]

    fpkms[name] = fpkm

fpkms_df = pd.DataFrame(fpkms)
df = fpkms_df.sum(axis=1)
#total = pd.DataFrame.sum(fpkm1, fpkm2)
#df = fpkm1 + fpkm2


# if total.item() > 40:
#     print(total)
roi = df > threshold
total2 = df.loc[roi]
print(total2)

#fpkms_df.to_csv(sys.stdout)