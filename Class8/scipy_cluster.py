#!/usr/bin/env python3

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import pandas as pd
import seaborn as sns


d = pd.read_csv('hema_data.txt', sep="\t", index_col='gene')
df = pd.DataFrame(data=d)

#cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)
cmap = sns.diverging_palette(145, 280, s=85, l=25, n=7, as_cmap=True)

ax = sns.clustermap(df, cmap=cmap)

ax.savefig("heatmap2.png")
plt.close()