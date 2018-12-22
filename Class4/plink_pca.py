#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor
PCA plot for chromosome 22 of VCF file
Input = pca_analysis_22.eigenvec
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df = pd.read_csv(sys.argv[1], sep=" ", header=None)
#df_pca = df.iloc[:, 2]
#col_names = df.columns.values.tolist()
#print(df_pca)
#exit()

#pca = PCA(n_components = 2)
#fit = pca.fit(df_pca)
#x = fit.transform(df_pca)

fig, ax = plt.subplots()
ax.scatter(df.iloc[:, 2], df.iloc[:, 3])
ax.set_title("BYxRM Yeast Variation")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")

#for i in range(len(col_names)):
#    ax.annotate(col_names[i], x[i,0, x[i,1]])
    
fig.savefig("pca_BYxRM.png")
plt.close(fig)