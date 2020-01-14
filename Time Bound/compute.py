import time
import random
import matplotlib.pyplot as mlt
import numpy as np
from numba import jit
l1=[2,3,5,10,20,30,40,50,100,200,300,400,500]
l2=[]
l3=[]
l4=[]
def normal():
    global l1
    global l2
    for t in l1:
        start = time.time()
        m1=[]
        m2=[]
        m3=[]
        for i in range(t):
            x=[]
            y=[]
            z=[]
            for j in range(t):
                x.append(random.randint(0,9))
                y.append(random.randint(0,9))
                z.append(0)
            m1.append(x)
            m2.append(y)
            m3.append(z)

        for i in range(t):
            for j in range(t):
                for k in range(t):
                    m3[i][j] += m1[i][k] * m2[k][j]
        end=time.time()
        a=(end-start)
        l2.append(a)
        
def numpy1():
	global l1
	global l3
	for t in l1:
		start=time.time()
		a=np.random.rand(t,t)
		b=np.random.rand(t,t)
		c=np.dot(a,b)
		end=time.time()
		a=end-start
		l3.append(a)
    
    
@jit
def numba1_multi():
    global l1
    global l4
    for t in l1:
        start = time.time()
        m1=[]
        m2=[]
        m3=[]
        for i in range(t):
            x=[]
            y=[]
            z=[]
            for j in range(t):
                x.append(random.randint(0,9))
                y.append(random.randint(0,9))
                z.append(0)
            m1.append(x)
            m2.append(y)
            m3.append(z)

        for i in range(t):
            for j in range(t):
                for k in range(t):
                    m3[i][j] += m1[i][k] * m2[k][j]
        end=time.time()
        a=(end-start)
        l4.append(a)
normal()
numpy1()
numba1_multi()

mlt.plot(l1,l2,color="red",label="Matrix Multiplication")
mlt.plot(l1,l3,color="blue",label="Numpy Multiplication")
mlt.plot(l1,l4,color="green",label="Numba @Jit Multiplication")
mlt.xlabel("Order of matrix")
mlt.ylabel("Time Taken(sec)")
mlt.legend()
mlt.title("TIME VS INPUT GRAPH GCI 2019")
mlt.xticks([50,100,150,200,250,300,350,400,450,500,550])
mlt.show()
    
