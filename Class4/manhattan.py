#!/usr/bin/env python3

"""
Usage: ./manhattan.py /plink_out/
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fasta
from collections import defaultdict
import math
import os

all_plinks = ["plink.Cadmium_Chloride.qassoc", "plink.Lactate.qassoc", "plink.YNB:ph3.qassoc", "plink.Caffeine.qassoc", "plink.Lactose.qassoc", "plink.YNB:ph8.qassoc", "plink.Calcium_Chloride.qassoc", "plink.Lithium_Chloride.qassoc", "plink.YPD.qassoc", "plink.Cisplatin.qassoc", "plink.Magnesium_Chloride.qassoc", "plink.YPD:15C.qassoc", "plink.Cobalt_Chloride.qassoc", "plink.Magnesium_Sulfate.qassoc", "plink.YPD:37C.qassoc", "plink.Congo_red.qassoc", "plink.Maltose.qassoc", "plink.YPD:4C.qassoc", "plink.Copper.qassoc", "plink.Mannose.qassoc", "plink.Zeocin.qassoc", "plink.Cycloheximide.qassoc", "plink.Menadione.qassoc", "plink.eigenval", "plink.Diamide.qassoc", "plink.Neomycin.qassoc", "plink.eigenvec", "plink.E6_Berbamine.qassoc", "plink.Paraquat.qassoc", "plink.irem", "plink.Ethanol.qassoc", "plink.Raffinose.qassoc", "plink.log", "plink.Formamide.qassoc", "plink.SDS.qassoc", "plink.nosex", "plink.Galactose.qassoc", "plink.Sorbitol.qassoc", "plink.x4-Hydroxybenzaldehyde.qassoc", "plink.Hydrogen_Peroxide.qassoc", "plink.Trehalose.qassoc", "plink.x4NQO.qassoc", "plink.Hydroquinone.qassoc", "plink.Tunicamycin.qassoc", "plink.x5-Fluorocytosine.qassoc", "plink.Hydroxyurea.qassoc", "plink.Xylose.qassoc", "plink.x5-Fluorouracil.qassoc", "plink.Indoleacetic_Acid.qassoc", "plink.YNB.qassoc", "plink.x6-Azauracil.qassoc"]


def manhattan(filename):
    sig_psn = []
    sig_pval = []
    insig_psn = []
    insig_pval = []
    threshold_val = 0.00001
    file_number = 0
    for line in open(filename):
        if "NA" in line or "BETA" in line:
            continue
        else:
            fields = line.rstrip("\r\n").split()
            file_number += 1
            psn = float(fields[2])
            pval = float(fields[8])
            pval2 = -(math.log(pval, 10))
            if pval < threshold_val:
                sig_psn.append(psn)
                sig_pval.append(pval2)
            elif pval > threshold_val:
                insig_psn.append(psn)
                insig_pval.append(pval2)  
    return sig_psn, sig_pval, insig_psn, insig_pval, file_number       

def graph(sig_psn, sig_pval, insig_psn, insig_pval, file_number):
    fig, ax = plt.subplots()
    plt.scatter(sig_psn, sig_pval, color = "maroon", alpha = 0.9, label = "significant")
    plt.scatter(insig_psn, insig_pval, color = "grey", alpha = 0.2, label = "insignificant")
    ax.set_xlabel("SNP position")
    ax.set_ylabel("-log10(p-value)")
    fig.savefig(str(all_plinks[p]) + ".png")
    plt.close()


for p in range(len(all_plinks)):
    path = "/Users/cmdb/qbb2018-answers/Class4/plink_out/" + all_plinks[p]
    print(path)
    
    sig_psn, sig_pval, insig_psn, insig_pval, file_number = manhattan(path)
    graph(sig_psn, sig_pval, insig_psn, insig_pval, file_number)

