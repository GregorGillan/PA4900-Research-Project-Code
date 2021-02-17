import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

#Defining Initial conditions
#----------------------------------------------------#
n = 68E6 #Total population GM = 1000

I0 = 1 #GM = 1
#Initial number of infected people
R0 = 0 #Initial number of recovered people GM = 0

#Everyone else 'S0', ie susceptable to infection initially
S0 = n - I0 - R0 

i = 0.2 #Infection rate GM = 0.2
r = 1/10 #Recovery rate (1/days) GM = 1/10
#----------------------------------------------------#

#Defining a time range
days = 365 #Length of time 
t = np.linspace(0, days, days)

#Defining the SIR model equations
def modelSIR(y, t, n, i, r):
    S, I, R = y
    dSdt = - i*S*I/n  #Susceptible model
    dIdt = i*S*I/n-r*I #Infection model
    dRdt = r*I #Infection model
    return dSdt, dIdt, dRdt

#Initial conditions vector
iCV = S0, I0, R0

#integrating SIR equations over time grid
soln = odeint(modelSIR, iCV, t, args = (n, i, r))

S, I, R = soln.T

#defining Recovery function

lab = [
    "Population: {}, ".format(n), 
    "S_0: {}, ".format(S0),
    "I_0: {}, ".format(I0),
    "R_0: {}, ".format(R0),
    "Infection Rate: {}, ".format(i),
    "Recovery Rate: {} ".format(r)
    ]
    
lab = ''.join(lab)

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(t, S/n, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/n, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/n, 'g', alpha=0.5, lw=2, label='Recovered')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Proportion of Population')
ax.set_ylim(0,1.1)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend1 = ax.legend()
ax.annotate(lab, xy=(0, 1), xycoords='axes fraction')
legend1.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
