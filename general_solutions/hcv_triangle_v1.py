import math
import random

def coordinate_giver(d=3,v=2,dt=0.001,niter=20000):
    theta=(60*math.pi)/180

    x=[0.,0]
    y=[d,0.0]
    z=[d*math.cos(theta),d*math.sin(theta)]


    X,Y,Z=[x],[y],[z]
    for i in range(niter):
        X+=[[X[i][j]+((norm(Y[i],X[i])[0][j])*v*dt) for j in range(2)]]
        Y+=[[Y[i][j]+((norm(Z[i],Y[i])[0][j])*v*dt) for j in range(2)]]
        Z+=[[Z[i][j]+((norm(X[i],Z[i])[0][j])*v*dt) for j in range(2)]]
    return X,Y,Z

def norm(b,a):
    d=[]
    sum_t=0
    for i in range(2):
        t=b[i]-a[i]
        sum_t+=t**2
        d+=[t]
    distance=sum_t**0.5
    c=[d[i]/distance for i in range(2)]
    return c,distance

def time_calc(X1,Y1,dt=0.001,niter=20000):       # Note dt here should be same as first function.
    for i in range(niter):
        if norm(Y1[i],X1[i])[1]<0.01:
            break
        time_approach=i*dt
    return time_approach

dis=[i+1 for i in range(5)]
vel=[i+5 for i in range(5)]
time_a=[]
for i in range(5):
    new=coordinate_giver(dis[i],vel[i])
    time_a+=[time_calc(new[0],new[1])]
x_coor=[dis[i]/vel[i] for i in range(5)]

import matplotlib.pyplot as plt
plt.plot(x_coor,time_a,'bo')
plt.show()





import numpy as np
A,B,C=coordinate_giver(d=6,v=2,dt=0.1,niter=32)
Ax,Ay=np.array(A)[:,0],np.array(A)[:,1]
Bx,By=np.array(B)[:,0],np.array(B)[:,1]
Cx,Cy=np.array(C)[:,0],np.array(C)[:,1]


from matplotlib import pyplot as plt, animation
fig,ax=plt.subplots()
def animate(i):
   plt.plot(Ax[i],Ay[i],'bo')
   plt.plot(Bx[i],By[i],'go')
   plt.plot(Cx[i],Cy[i],'ro')
   
   plt.xlim(-1,7)
   plt.ylim(-1,7)
anim = animation.FuncAnimation(fig,func= animate, interval=500, frames=len(Ax))
plt.show()
