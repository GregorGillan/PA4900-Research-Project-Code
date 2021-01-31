import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

## Infection

#Defining Initial conditions
#----------------------------------------------------#
#Total population
n = 1000

#Initial number of infected and recovered people, 'I0' and 'R0'
I0, R0 = 50, 0

#Everyone else 'S0', ie susceptable to infection initially
S0 = n - I0 - R0

#Infectrion rate 'i' and mean recovery rate 'r' (1/days)
i, r = 0.001, 1/7 #infection rate
#----------------------------------------------------#

#Defining a time range
t = np.linspace(0, 160, 160)

#Defining the SIR model equations
def modelSIR(y, t, n, i, r):
    S, I, R = y
    dSdt = - i*S*I/n  #Susceptible model
    dIdt = i*S*I/n-r*I #Infection model
    dRdt = r*I #Infection model
    return dSdt, dIdt, dRdt

#Initial conditions vector
y0 = S0, I0, R0

#integrating SIR equations over time grid
soln = odeint(modelSIR, y0, t, args = (n, i, r))

S, I, R = soln.T

#defining Recovery function

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

#plt.plot(t, y_I)
#show()