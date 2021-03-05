import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *
import pandas as pd

x_0 = 0.5 #Initial population
b = 3.75 #fecundity rate

iN = 100 #Number of iterations
i = 0 #Initialising iterations

iL = [x_0] #Initialising iteration list

x = x_0
while i < iN:
    i = i + 1
    
    x = b * x * (1 - x)

    iL.append(x) #Creating iteration array

print(iL[-1])
#print(len(iL))

yy = iL
xx = np.linspace(0, iN, iN + 1)
#print(yy)
#print(xx)
"""
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(xx, yy, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.set_xlabel('Iteration')
ax.set_ylabel('Population of x (0 - 1)')


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