import time
import random
import matplotlib.pyplot as mlt
from numba import jit
l1=[2,3,5,10,20,30,40,50,100,200,300,400,500]
l2=[]
@jit
def yes():
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
yes()
mlt.plot(l1,l2)
mlt.xlabel("Order of matrix")
mlt.ylabel("Time Taken(sec)")
mlt.title("TIME VS INPUT GRAPH GCI 2019")
mlt.yticks([10,20,30,40,50,60,70,80,90,100])
mlt.xticks([50,100,150,200,250,300,350,400,450,500,550])
mlt.show()