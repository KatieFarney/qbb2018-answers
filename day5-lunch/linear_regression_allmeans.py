#!/usr/bin/env python3

"""
Usage: ./linear_regression.py <t_data.ctab> <HIS_means_exp.tab> 
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std

filename = pd.read_table(sys.argv[1])
his_means = []
for i in range(2,7):
    his_means.append(filename.iloc[:,i])
#[filename.iloc[2]]
#his_means = filename.loc[:,"mean"]

y = filename.loc[:,"FPKM"]
x = filename.iloc[:,2:]
x = sm.add_constant(x)
model = sm.OLS(y,x)
results = model.fit()
results.params
results.tvalues
#print(results.t_test([1, 0]))
print(results.summary())

# prstd, iv_l, iv_u = wls_prediction_std(model)
#
# fig, ax = plt.subplots()
#
# ax.plot(x, y, 'o', label="data")
# #ax.plot(x, y_true, 'b-', label="True")
# ax.plot(x, model.fittedvalues, 'r--.', label="OLS")
# ax.plot(x, iv_u, 'r--')
# ax.plot(x, iv_l, 'r--')
# ax.legend(loc='best');
# fig.savefig("linear_regression_v1.png")
# plt.close(fig)







##FPKM (Y) and His expression means for x values

