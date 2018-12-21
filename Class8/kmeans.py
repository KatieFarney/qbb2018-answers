#!/usr/bin/env python3

"""
Usage: ./kmeans.py hema_data.txt

"""
import sys
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list, optimal_leaf_ordering
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans,vq

df=pd.read_table(sys.argv[1], sep = "\t", header = 0, index_col = 0).loc[:, ("CFU", "poly")]
array = df.values
col_names = df.columns.values.tolist()

Z = linkage(array, 'ward')
kmeans = KMeans(n_clusters = 4)
kmeans.fit(Z)
y_means = kmeans.predict(Z)
fig, ax = plt.subplots()
plt.scatter(Z[:, 0], Z[:, 1], c = y_means, s=10, cmap = "coolwarm_r")
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c = "black", s=100, alpha = 0.5)
fig.savefig("kmeans_heatmap.png")
plt.close(fig)



