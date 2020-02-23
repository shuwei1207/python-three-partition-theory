# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 23:01:55 2018

@author:
"""

import numpy as np
import random
import csv

f=open('pdata.txt','w')
#j1 for job,k for machine
j1 = int(input('輸入j(4t+1):'))
k = int(input('請輸入k(3 machines):'))
b = 30

#p = [[0, 2*b,2*b,3t's 0], 
#     [b, b,b,3t's 1/3*b],
#     [2*b, 2*b,3t's 0 ]]

p = [[0, 2*b], 
     [b, b],
     [2*b, 0]]

t=int((j1-1)/4)

for i in range(t-1):
    i = i+1
    p[0].insert(i,2*b)
    p[1].insert(i,b)
    p[2].insert(i,2*b)
    
for i in range(3*t):
    p[0].append(0)
    p[2].append(0)
    
j = 3*t
padd = []
for i in range(t): #1/2-1/4b之間
        fir = random.randint(int(0.25*b),int(0.31*b))
        sec = random.randint(int(0.25*b),int(0.31*b))
        thi = b-fir-sec #可能thi會沒在區間內
        padd.append(fir)
        padd.append(sec)
        padd.append(thi)
        
        
        
for i in range(len(padd)):
    p[1].append(padd[i])   

pdata = []
for i in range(3):
    for j in range(j1):
        pdata.append(p[i][j]) 
#padd是隨機湊a

pdata.append(j1)
pdata.append(k)      
pdatastr=' '.join(str(e) for e in pdata)
f.write(pdatastr)

# 開啟輸出的 CSV 檔案
with open('three.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)

  # 寫入一列資料
  writer.writerow(['index', 'p1', 'p2','p3'])

  # 寫入另外幾列資料
  for i in range(j1):
      writer.writerow([i+1, pdata[i], pdata[i+j1],pdata[i+2*j1]])
 