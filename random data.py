# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:03:51 2018

@author: USER
"""

import numpy as np
import random
f=open('pdata.txt','w')
#j for job,k for machine
j = int(input('輸入j:'))
k = int(input('請輸入k(3 machines):'))
a=15
b=25

pdata=[]
for i in range(j):
    k1 = random.randint(a,b)
    k2 = random.randint(a,b)
    k3 = random.randint(a,b)
    pdata.append(k1)
    pdata.append(k2)
    pdata.append(k3)


pdata.append(j)
pdata.append(k)      
pdatastr=' '.join(str(e) for e in pdata)
f.write(pdatastr)