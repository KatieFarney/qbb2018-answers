#!/usr/bin/env python3

"""
Usage: ./diff.py hema_data.txt

"""
import sys
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list, optimal_leaf_ordering
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans,vq
from scipy.stats import ttest_ind

df=pd.read_table(sys.argv[1], sep = "\t", header = 0, index_col = 0).loc[:, ("CFU", "mys", "poly", "unk")].dropna()


early = ["CFU", "mys"]
late = ["poly", "unk"]

t_stat, p_val = ttest_ind(df[early], df[late], axis = 1)
df["p_value"] = p_val

df = df.mask(df["p_value"] > 0.05).dropna(how = "any").sort_values ("p_value")
print (df.ix[:,4].to_csv(sep='\t'))

print(df.index)

