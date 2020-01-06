import matplotlib.pyplot as mlt
import time
import numpy as np
from numba import jit
l1=[2,3,5,10,20,30,40,50,100,200,300,400,500]
l2=[]
@jit
for t in l1:
    start=time.time()
    a=np.random.rand(t,t)
    b=np.random.rand(t,t)
    c=np.dot(a,b)
    end=time.time()
    a=end-start
    l2.append(a)
mlt.plot(l1,l2)
mlt.xlabel("Order of matrix")
mlt.ylabel("Time Taken(sec)")
mlt.title("TIME VS INPUT GRAPH GCI 2019")
mlt.yticks(l2)
mlt.xticks([50,100,150,200,250,300,350,400,450,500,550])
mlt.show()
    
    