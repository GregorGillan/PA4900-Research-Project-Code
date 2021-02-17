import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

#Defining Initial conditions
#----------------------------------------------------#
x0 = 1000 #Initial prey population
y0 = 10 #Initial predator population

alpha = 1 
beta = 1
gamma = 1
delta = 1

#----------------------------------------------------#

#Defining a time range
t = np.linspace(0, 200, 200)

#Defining the SIR model equations
def modelPP(iCV, t):
    a, b, g, d, x, y = iCV

    dxdt = a*x-b*x*y 
    dydt = d*x*y-g*y
    return dxdt, dydt

iCV = alpha, beta, gamma, delta, x0, y0

soln = odeint(modelPP, iCV, t)

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(t, x, 'b', alpha=0.5, lw=2, label='Prey')
ax.plot(t, y, 'r', alpha=0.5, lw=2, label='Predator')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Population')
#ax.set_ylim(0,1.1)
#ax.yaxis.set_tick_params(length=0)
#ax.xaxis.set_tick_params(length=0)
#ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()