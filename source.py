import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from sys import argv

nmax=int(argv[2])
num=np.zeros((nmax))
xaxis=np.zeros((nmax))
num[0]=argv[1]
for i in range(1,nmax):
    if(num[i-1] % 2 ==0):
        num[i]=num[i-1]/2
        xaxis[i]=i
    else:
        num[i]=num[i-1]*3+1
        xaxis[i]=i
 #   print(xaxis[i],num[i])
##########

fig = plt.figure()
fig.set_size_inches(4.8,3.0)

ax = plt.subplot()
divider = make_axes_locatable(ax)
colors1='#00CED1'
numplot=ax.scatter(xaxis,num,c=colors1,alpha=0.4)
plt.legend()
plt.savefig(r'./collatz.png',dpi=300)
plt.show()
