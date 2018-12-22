#!/usr/bin/env python3

"""
Usage: ./chipseq_v2.py overlappingSites.bed uniqueTF.bed G1E/NA_summits.bed ER4/NA_summits.bed Mus_musculus.GRCm38.94_features.bed 

"""

import sys
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

gained = open(sys.argv[1])
lost = open(sys.argv[2])

gain_count = 0
for line in gained:
    gain_count +=1
loss_count = 0
for line in lost:
    loss_count += 1

y_vals = [gain_count, loss_count]
x_vals_1 = np.arange(2)


G1E_file = open(sys.argv[3])
ER4_file = open(sys.argv[4])
features_file = open(sys.argv[5])

positions = {}
for line in features_file:
    fields = line.rstrip("\r\n").split()

    start = int(fields[1])
    end = int(fields[2])
    feat_type = fields[3]

    for position in range(start, end):
        positions[position] = feat_type

def count_features(filename):
    features = {"other":0}
    for line in filename:
        fields = line.rstrip("\r\n").split()
        start = int(fields[1]) 
        if start in positions:
            feat_type = positions[start]
            if feat_type in features:
                features[feat_type] += 1
            else:
                features[feat_type] = 1 
        else:
            features["other"] += 1
    return(features)

G1E_features = count_features(G1E_file)
ER4_features = count_features(ER4_file)

y_vals_G1E = [G1E_features["intron"], G1E_features["exon"], G1E_features["promoter"], \
            G1E_features["other"]]
y_vals_ER4 = [ER4_features["intron"], ER4_features["exon"], ER4_features["promoter"], \
            ER4_features["other"]]
x_vals_2 = np.arange(4)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(13,5))


ax1.bar(x_vals_1, y_vals, width=0.5, color="lightblue")
ax1.set_xticks(x_vals_1)
ax1.set_xticklabels(["Gained", "Lost"])
ax1.set_xlabel("Change during differentiation")
ax1.set_ylabel("Number of CTCF sites")
ax1.set_title("Change in CTCF binding sites during G1E to ER4 differentiation")


p1 = ax2.bar(x_vals_2, y_vals_G1E, color="rebeccapurple")
p2 = ax2.bar(x_vals_2, y_vals_ER4, bottom=y_vals_G1E, color="magenta")
ax2.set_xticks(x_vals_2)
ax2.set_xticklabels(["Introns", "Exons", "Promoters", "Other"])
ax2.legend((p1[0], p2[0]), ("G1E", "ER4"))
ax2.set_xlabel("Type of region")
ax2.set_ylabel("Number of CTCF sites")
ax2.set_title("Types of features bound by CTCF")

plt.tight_layout()
fig.savefig("chipseq_plots.png")
plt.close(fig)

