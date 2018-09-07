#!/usr/bin/env python3

"""
Histogram of linear regression of log values
input <HIS_means_exp.tab>
"""

import sys
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets
import numpy as np
import pandas as pd
import statsmodels.api as sm

filename = pd.read_table(sys.argv[1])

Y = np.log(1 + filename.loc[:,"FPKM"])
X = filename.iloc[:,2:]
X = sm.add_constant(X)
model = sm.OLS(Y,X)
results = model.fit()
results.params
results.tvalues
new_Y = results.fittedvalues

r = new_Y - Y 

#labels = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width",]
#means = ["H3K27ac_out", "H3K27me3_out", "H3K4me1_out", "H3K4me3_out", "H3K9ac_out"]



fig, ax = plt.subplots(figsize=(8, 6))
#hist = 
ax.hist(r, bins = 300)
ax.set_xlim(-7,7) 
#ax.set_ylim(0,200) 
ax.set_title("Linear Regression Residuals")
ax.set_xlabel("Residuals")
ax.set_ylabel("Log Frequency")  

fig.savefig("SRR2893_log_hist.png")          
plt.close(fig)   
#plt.show(fig)

#minimum = np.min(r)          
#maximum = np.max(r)   
   
