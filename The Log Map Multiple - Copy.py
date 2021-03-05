import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *
import pandas as pd

x0 = 0.5 #Initial population
#b0 = 3.99999999999999996 #fecundity rate
b0 = 2.8
bMax = 4
print(b0)
sTP = 0.05

iN = 100 #Number of iterations
iLL = []
itAFT = []
def lMap(b):
    x = x0
    i = 0 #Initialising iterations
    while i < iN:
        i = i + 1
        x = b * x * (1 - x)
        iLL.append(x)
    return(x)

xxxx = [lMap(b0)]
iB = b0
iBC = [b0]
while iB < bMax:
    iB = iB + 0.05
    iB = np.round(iB, decimals = 2)
    xxxx.append(lMap(iB))
    iBC.append(iB)

print(iBC)
xyx = np.arange(2.8, 4.0, 0.05)
print(xxxx)
#xyx = round(xyx, 2)
#print(xyx)
#zzz = lMap(4.0)
#print(zzz)
#print(iLL)
#b_L = format(b_L, '.20g')
#print(b_L)
#print(iL)
#print(itAFT)
#print(size(itAFT))
xx = xyx
yy = xxxx

plt.scatter(xx, yy, s = 0.5)
plt.show()
"""
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot.scatter(xx, yy)
ax.set_xlabel('Iteration')
ax.set_ylabel('Population of x (0 - 1)')
"""
"""
lab = [
    "x_0: {}, ".format(x_0), 
    "b: {}, ".format(b),
    "Iterations: {} ".format(iN),
    ]
    
lab = ''.join(lab)
ax.annotate(lab, xy=(0, 1), xycoords='axes fraction')

for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
#ax.grid(b=True, which='minor', c='black', lw=0.5, ls='-')
#ax.grid(b=True, which='major', c='black', lw=0.5, ls='-')
plt.show()
"""