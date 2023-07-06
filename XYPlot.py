# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:44:42 2020

2D Line Plotting File

@author: Thedal
"""
# %% Cell 1

#Imports
from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd

#Changing Font of Plot
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Times New Roman']
rcParams['axes.linewidth'] = 1.2

#Plot Details
Title = ["Plot Title","X label","Y label"]
X = [0, 1, 0.1,'linear']
Y = [0, 1, 0.1,'linear']
LegendPosition= 2

#File Details
fileName =["B:/PhD/resultsCSV/Shitsman/E320/22-5lakhs-all-10-UDF-prandtl.csv","B:/PhD/resultsCSV/Shitsman/E320/20-5lakhs-all-10-UDF-ggdh-prandtl.csv"]
N = len(fileName)
skip = [5]*N
label = ['u SST [Raiesi]','u DNS','v SST [Raiesi]','v DNS','u Present','u 12m','v 8m','v Present']
lineStyle = ['r*--','g+--','r-.','gs--','bo--','ks--','b--','kd--']


#File Import
Var = []
for i in range(N):
    Var.append(np.array(pd.read_csv(fileName[i],skiprows=skip[i])))


# %% Cell 3
#Plotting
fig=plt.figure(figsize=(8,6.5),tight_layout=True)
a = fig.add_subplot(221)
b = fig.add_subplot(224)

#Titles
a.set_title(Title[0],fontsize=18,fontweight='bold')
a.set_xlabel(Title[1],fontsize = 14,fontweight='bold')
a.set_ylabel(Title[2],fontsize = 14,fontweight='bold')

#Axis Limits Grid and Ticks

# Set Axis Limits
a.axis([X[0],X[1],Y[0],Y[1]])

# Set Plot Border
a.spines['right'].set_visible(False)
a.spines['top'].set_visible(False)
a.spines['left'].set_visible(True)
a.spines['bottom'].set_visible(True)

# Grid ON/OFF
a.grid('on',color='k',linestyle='dashed',alpha=0.5)

# Global Tick Parameters
a.tick_params(direction='out', length=5, width=1, colors='k')

# X tick Parameters
if X[3]=='linear':
    a.set_xticks(np.arange(X[0],X[1]+X[2],X[2]))
else:
    a.set_xscale(X[3])

# Y tick Parameters
if Y[3]=='linear':
    a.set_yticks(np.arange(Y[0],Y[1]+Y[2],Y[2]))
else:
    a.set_yscale(Y[3])


# The Plot
for i in range(N):
    a.plot(Var[i][0], Var[i][1], lineStyle[i], label=label[i], markerfacecolor='white', markevery=10)

#Additional Lines
#a.hlines(y=384.9,xmin=0,xmax=1.2,colors='r',linestyles='dashdot',label="T pc",linewidth=1.0)
#a.vlines(x=0.5,ymin=0,ymax=400,colors='c',linestyles='dashdot',label = "V Line",linewidth=0.8)

a.legend(loc=LegendPosition)

plt.show()

#Save Figure
# Directory="F:/PhD/Results/"
# FileName = "Test_File"
# Format=".svg"
# FilePath =Directory+FileName+Format
# fig.savefig(FilePath)