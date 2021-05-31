import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *
import pandas as pd

#Initializing values
p0 = 0.5 #Initial population.
b0 = 2.8 #Fecundity rate initial value.
bMax = 4.0 #Fecundity rate final value.
bStep = 0.01 #Change the value of dPoints to match the d.p of bStep.
dPoints = 3 #Sets rounding accuracy, needs to match d,p of bstep, otherwise F.P rounding errors occur.
iN = 1000 #Number of iterations.

itPopVal = [] #Initializing array for the iterative population values for ach value of b.
#function for completing the iterations of the function.
def lMap(b):
    p = p0 #Initialising the population value back to p0 before doing iterations.
    i = 0 #Initialising iterations.
    while i < iN:
        i = i + 1
        p = b * p * (1 - p)
        itPopVal.append(p)
    return(p)

pValues = [lMap(b0)] #Initializing the final population values.

b = b0 #Initialising b values.
bValues = [b0] #Initializing array for list of b values used.
#Loop used to calculate p final for values of b.
while b < bMax:
    b = b + bStep
    b = np.round(b, decimals = dPoints) #Change with bStep d.p.!
    pValues.append(lMap(b))
    bValues.append(b)

print(bValues)
print(pValues)
xValues = bValues
yValues= pValues

#Doing scatter plots
plt.scatter(xValues, yValues, s = 0.1)

#Plotting
fig = plt.scatter(xValues, yValues, facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(xValues, yValues, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.set_xlabel('b Values')
ax.set_ylabel('Population of x (0 - 1) after n iterations')





for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
#ax.grid(b=True, which='minor', c='black', lw=0.5, ls='-')
#ax.grid(b=True, which='major', c='black', lw=0.5, ls='-')


plt.show()

'''
lab = [
    "p0: {}, ".format(p0), 
    "b0: {}, ".format(b0),
    "bMax: {}, ".format(bMax),
    "bStep: {}, ".format(bStep),
    "Iterations: {} ".format(iN),
    ]
    
lab = ''.join(lab)
ax.annotate(lab, xy=(0, 1), xycoords='axes fraction')
'''