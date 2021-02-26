import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

#Defining Initial conditions
#----------------------------------------------------#
alpha = 0.9
beta = 0.5
gamma = 0.75
delta = 0.25

x0 = gamma/delta #Initial prey population
z0 = alpha/beta #Initial predator population

days = 50
#Defining a time range
t = np.linspace(0, days, 1000)
#----------------------------------------------------#

#Defining the SIR model equations
def modelPP(i, t, a, b, g, d):
    x, y = i

    dxdt = a*x-b*x*y 
    dydt = d*x*y-g*y
    return dxdt, dydt

iCV = x0, z0

soln = odeint(modelPP, iCV, t, args=(alpha, beta, gamma, delta))

X, Y = soln.T

fig, (ax, ax1) = plt.subplots(1, 2, figsize = (1280/96, 720/96), dpi = 96) 
#fig.figure(figsize = (1920/96, 1080/96), dpi = 96) 
ax.plot(t, X, 'b', alpha=0.5, lw=2, label='Prey')
ax.plot(t, Y, 'r', alpha=0.5, lw=2, label='Predator')
ax.set_xlabel('Time (days)')
ax.set_ylabel('Population')
ax1.plot(X, Y)
ax1.set_xlim(0,20)
ax1.set_ylim(0,20)
ax1.set_xlabel('Prey Polulatioon')
ax1.set_ylabel('Predator Population')
#ax.set_ylim(0,1.1)
#ax.yaxis.set_tick_params(length=0)
#ax.xaxis.set_tick_params(length=0)
#ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
plt.show()