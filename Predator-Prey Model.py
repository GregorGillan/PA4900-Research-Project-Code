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

x0 = 10 #gamma/delta #Initial prey population
z0 = 2 #alpha/beta #Initial predator population

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
fig.patch.set_alpha(0.0)
#fig.figure(figsize = (1920/96, 1080/96), dpi = 96) 
ax.patch.set_alpha(0.0)
ax.plot(t, X, 'r', alpha=1, lw=2, label='Prey')
ax.plot(t, Y, 'b', alpha=1, lw=2, label='Predator')
ax.set_title('Lotka-Volterra Solution', c = 'black', fontsize = 20)
ax.set_xlabel('Time (days)', fontsize = 18, c = 'black')
ax.set_ylabel('Population', fontsize = 18, c = 'black')
ax.set_ylim(0, 12.2)

ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black') 
ax.spines['right'].set_color('black')
ax.spines['left'].set_color('black')

ax.tick_params(axis='x', colors='black', labelsize = 18)
ax.tick_params(axis='y', colors='black', labelsize = 18)

ax1.patch.set_alpha(0.0)
ax1.set_title('Phase Plot for Solution', c = 'black', fontsize = 20)
ax1.plot(X, Y, c = 'g', alpha = 1, lw = 2)
ax1.set_xlim(0, 12)
ax1.set_ylim(0, 6.2)
ax1.set_xlabel('Prey Population', fontsize = 18, c = 'black')
ax1.set_ylabel('Predator Population', fontsize = 18, c = 'black')

ax1.tick_params(axis='x', colors='black', labelsize = 18)
ax1.tick_params(axis='y', colors='black', labelsize = 18)


#ax.set_ylim(0,1.1)
#ax.yaxis.set_tick_params(length=0)
#ax.xaxis.set_tick_params(length=0)
#ax.grid(b=True, which='major', c='black', lw=2, ls='-')
legend = ax.legend(labelcolor = 'black', facecolor = 'k', framealpha = 0, frameon = False, fontsize = 18)
legend.get_frame().set_alpha(0)

#for spine in ('top', 'right', 'bottom', 'left'):
 #   ax.spines[spine].set_visible(False)
  #  ax1.spines[spine].set_visible(False)
plt.show()