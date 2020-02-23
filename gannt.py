# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 01:12:21 2018

@author: USER
"""

import pandas as pd
import io
import matplotlib.pyplot as plt
    
plt.rcParams['font.sans-serif']=['SimHei']  
plt.rcParams['axes.unicode_minus']=False 

height=16
interval=4 
colors = ("turquoise","crimson","black","red","yellow","green","brown","blue") #color set
x_label=u"Time"

df = pd.read_csv('output.csv', header=None, names=["Machine", "Start", "Finish","Title"] )
df["Diff"] = df.Finish - df.Start
fig,ax=plt.subplots(figsize=(20,10))
labels=[]
count=0;
for i,machine in enumerate(df.groupby("Machine")):
    labels.append(machine[0])
    data=machine[1]
    for index,row in data.iterrows():
        ax.broken_barh([(row["Start"],row["Diff"])], ((height+interval)*i+interval,height), facecolors=colors[i])
        plt.text(row["Start"], (height+interval)*(i+1),row['Title'],fontsize='22')  
        if(row["Finish"]>count):
            count=row["Finish"]
ax.set_ylim(0, (height+interval)*len(labels)+interval)
ax.set_xlim(0, count+2)
ax.set_xlabel(x_label)
ax.set_yticks(range(interval+(height/2),(height+interval)*len(labels),(height+interval)))
ax.set_yticklabels(labels)
ax.xaxis.grid(True) #只顯示X
plt.savefig('gantt.png',dpi=800)
plt.show()