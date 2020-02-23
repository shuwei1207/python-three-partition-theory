import numpy as np
import random
#j1 for job,k for machine
j1 = int(input('輸入j(4t+1):'))
k = int(input('請輸入k(3 machines):'))
k1 = k
times = int(input('請輸入組數:'))
b = 30
totaltime = []

for i in range(times):
    f=open('pdata.txt','w')
    f.truncate()
    p = [[0, 2*b], 
         [b, b],
         [2*b, 0]]
    
    t=int((j1-1)/4)
    
    #用來補p1j~p1t-1
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
    for i in range(t):
            fir = random.randint(int(0.25*b),int(0.5*b))
            sec = random.randint(int(0.25*b),int(0.5*b))
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
    pdata.append(k1)      
    pdatastr=' '.join(str(e) for e in pdata)
    f.write(pdatastr)
    # -*- coding: utf-8 -*-
    """
    Created on Mon Dec 11 20:30:31 2017
    
    @author: USER
    """
    import sys
    import csv
    import time
    from gurobipy import *
    import matplotlib.pyplot as plt
    cons = []
    p = []
    for x in range(30):
        cons.append(0)
    f=open('pdata.txt','r')
    file = f.read()
    file =file[:].split(' ')
    f.close()
    
    file = list(file)
    m = file.pop()
    n = file.pop()
    n = int(n) #j
    o = n
    m = int(m) #k
    file = np.asarray(file)
    file = file.reshape(m,n)
    p = file.tolist()
    
    try:
      M=Model("mip1")
      #m為job n為工作 有4job 5work [, , , ]X5
      
      x=M.addVars(n,o,vtype=GRB.BINARY,name="x")
      c=M.addVars(m,o,vtype=GRB.INTEGER,name="c")
        
      M.update()
      Line = LinExpr()
      Line.addTerms(1,c[(m-1),(o-1)])
          
          
      M.setObjective(Line,GRB.MINIMIZE)
      
      for k in range(o):
          cons[0] = LinExpr()
          for j in range(n):
              cons[0].addTerms(1,x[j,k])
          M.addConstr(cons[0]==1)
      
      for j in range(n):
          cons[1] = LinExpr()
          for k in range(o):
              cons[1].addTerms(1,x[j,k])
          M.addConstr(cons[1]==1)
          
      cons[2] = LinExpr()
      for j in range(n):
          cons[2].addTerms(p[0][j],x[j,0])
      M.addConstr(c[0,0]==cons[2])
      
      for k in range(o-1):
          cons[3] = LinExpr()
          for j in range(n):
              cons[3].addTerms(p[0][j],x[j,k+1])
          M.addConstr(c[0,k+1]==cons[3]+c[0,k])
      
      i=k=j=0
      for i in range(m-1):
          for k in range(o):
              cons[2*i+4] = LinExpr()   
              for j in range(n):
                  cons[2*i+4].addTerms(p[i+1][j],x[j,k])
              M.addConstr(c[i+1,k]>=cons[2*i+4]+c[i,k])          
     
      i=k=j=0
      for i in range(m-1):
          for k in range(o-1):
              cons[2*i+5] = LinExpr()
              for j in range(n):
                    cons[2*i+5].addTerms(p[i+1][j],x[j,k+1])
              M.addConstr(c[i+1,k+1]>=cons[2*i+5]+c[i+1,k])
     
      starttime = time.time()     
      M.optimize()
      endtime = time.time()    
      totaltime.append(endtime-starttime)
      for v in M.getVars():
          print('%s %g'%(v.varName,v.x))
          
      print('Obj:%g'%M.objVal)
      
    except GurobiError:
        print('Encountered a Gurobi error')
        
    except AttributeError:
        print('Encountered an attribute error')

                    
print('Total time:',totaltime)
print('Max time:',max(totaltime))
print('Min time:',min(totaltime))
print('Average time:',float(sum(totaltime)/len(totaltime)))
                     