# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 14:47:16 2018

@author: USER
"""

import sys
import random
import numpy as np
import csv
from gurobipy import *


#從main拉n m過來做c
c =[[i*0 for i in range(n)] for i in range(m)]


p3=p2
psum = []
ppsum = []
for l in range(m):
    psum.append(p3[l][0])
    c[l][0] = sum(psum)
    for k in range(n):
        ppsum.append(p3[0][l])
        c[0][l] = sum(ppsum)

#第一列歸零重算
for i in range(n):
    c[0][i]=0

#第一列重置   
c[0][0] = p3[0][0]
for i in range(1,n):
    c[0][i] = p3[0][i]+c[0][i-1]
    
for i in range(m-1):
    i=i+1
    for j in range(n-1):   
        j=j+1
        c[i][j]= max(c[i-1][j],c[i][j-1])+p3[i][j]

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
#  writer.writerow(['job', '開始', '結束']) 
    for i in range(n):
        writer.writerow(['M3',c[2][i]-int(p2[2][i]),c[2][i],'3'+str(i+1)])
    for i in range(n):
        writer.writerow(['M2',c[1][i]-int(p2[1][i]),c[1][i],'2'+str(i+1)])
    for i in range(n):
        writer.writerow(['M1',c[0][i]-int(p2[0][i]),c[0][i],'1'+str(i+1)])