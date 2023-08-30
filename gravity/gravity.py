import numpy as np
import matplotlib.pyplot as plt

h0,a,u=500,9.8,0.0
time=[i/100 for i in range(1000)]
h=[h0-((u*t)+(0.5*a*(t**2))) for t in time]

for i in range(0,len(time),100):
  plt.plot(5,h[i],'go')
  plt.yticks([0,500])
  #plt.show()
  plt.savefig("new"+str(i))
