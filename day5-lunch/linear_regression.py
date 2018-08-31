#!/usr/bin/env python3

"""
Usage: ./linear_regression.py <t_data.ctab> <His_out1.tab> <His_out2.tab> 
"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.sandbox.regression.predstd import wls_prediction_std

df_fpkm = pd.read_table(sys.argv[1], index_col="t_name")
df_his = pd.read_csv(sys.argv[2], sep="\t", header=None, index_col="t_name", names=["t_name", "size", "covered", "sum", "mean0", "mean"])

#trans_start = df.loc[:,"start"]
df_new = pd.DataFrame (
    {#"t_name" : df_fpkm.loc[:,"t_name"],
    "FPKM" : df_fpkm.loc[:,"FPKM"]}
)

for item in sys.argv[2:len(sys.argv)]:
    hisname = item.split(".")[-2]
    df_his = pd.read_csv(item, sep="\t", header=None, index_col="t_name", names=["t_name", "size", "covered", "sum", "mean0", "mean"])
    df_new = df_new.assign(name= df_his.loc[:,"mean"])
    df_new = df_new.rename(columns={"name": str(hisname)})
    
df_new.to_csv(sys.stdout, sep="\t")  
exit()

y = df_new.loc[:,"FPKM"]
x = df_new.loc[:,"mean"]
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

