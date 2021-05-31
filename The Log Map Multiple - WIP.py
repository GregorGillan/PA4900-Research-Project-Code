import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *
import pandas as pd

#Initializing values
p0 = 0.5 #Initial population.
b0 = 0 #Fecundity rate initial value.
bMax = 4.0 #Fecundity rate final value.
bStep = 0.001 #Change the value of dPoints to match the d.p of bStep.
dPoints = 3 #Sets rounding accuracy, needs to match d,p of bstep, otherwise F.P rounding errors occur.
iN = 200 #Number of iterations.

itPopVal = [] #Initializing array for the iterative population values for ach value of b.
#function for completing the iterations of the function.
def lMap(b):
    pExVal.clear()
    p = p0 #Initialising the population value back to p0 before doing iterations.
    i = 0 #Initialising iterations.
    while i < iN:
        i = i + 1
        p = b * p * (1 - p)
        itPopVal.append(p)
        if i > 100:
            pExVal.append(p)
    return(p)

pExVal = []
pValues = [lMap(b0)] #Initializing the final population values.

b = b0 #Initialising b values.
bValues = [b0] #Initializing array for list of b values used.
#Loop used to calculate p final for values of b.
df = pd.DataFrame() #Creating dataframe for p value for iterations of b.
df[len(df.columns)] = pExVal
while b < bMax:
    pExVal = []
    b = b + bStep
    b = np.round(b, decimals = dPoints) #Change with bStep d.p.!
    pValues.append(lMap(b))
    bValues.append(b)
    df[len(df.columns)] = pExVal
'''
print(bValues)
print(pValues)
print(len(pExVal))
print(df.ndim)
print(df)
print(df[:1])
'''
xValues = bValues
yValues = pValues


#Doing scatter plots
print(type(bValues))
xxx = df
#xxx = df.iloc[1].T
#xxx = df.T
#xxx = xxx.values.tolist()   
#print(type(xxx))
#print(xxx)
#plt.scatter(xValues, yValues, s = 0.5)

#Plotting
fig = plt.figure(facecolor='black', figsize = (1280/96, 720/96), dpi = 96)
fig.patch.set_alpha(0.0)
ax = fig.add_subplot(111, axisbelow=True)
ax.patch.set_alpha(0.0)
#ax.scatter(xValues, yValues, s = 0.1, c = 'deeppink', label='Susceptible')
ax.set_title('The Logistic Map - Bifurcation Diagram', c = 'black', fontsize = 20)
ax.set_xlabel('b Values', c = 'black', fontsize = 18)
ax.set_ylabel('Population of x (0 - 1)', c = 'black', fontsize = 18)
ax.tick_params(axis='x', colors='black', labelsize = 18)
ax.tick_params(axis='y', colors='black', labelsize = 18)

#Plotting scatter
#fig1 = plt.figure(facecolor='black')
#ax1 = fig1.add_subplot(111, axisbelow=True)


iii = 0

while iii < (iN - 100):
    xxx = df.iloc[iii].T
    xxx = xxx.values.tolist()
    print(xxx)
    ax.scatter(xValues, xxx, c = 'b', s = 0.001)
    iii = iii + 1


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
