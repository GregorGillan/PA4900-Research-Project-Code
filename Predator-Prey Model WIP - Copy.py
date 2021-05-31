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
smarts = 0
smartCoeff = 0

x0 = 10 #gamma/delta #Initial prey population
z0 = 2# [1, 2, 5, 7, 10, 12, 15] #alpha/beta #Initial predator population

days = 100
#Defining a time range
t = np.linspace(0, days, 1000)
#----------------------------------------------------#

#Defining the SIR model equations
def modelPP(i, t, a, b, g, d, sC):
    x, y, s = i

    dxdt = a*x-b*x*y 
    dydt = d*(1-s)*x*y-g*y
    dsdt = (1/21)*(exp((-1/20)*t))
    return dxdt, dydt, dsdt

#Creating graphing functions ophase plot
#----------------------------------------------------#
fig = plt.figure(figsize = (1280/96, 720/96), dpi = 96) 
ax = fig.add_subplot(111, axisbelow=True)
nn = 0
xxx = 1 #len(z0) - 1 
#print(z0[1])
while (nn < xxx):
    nn = nn + 1
    z = z0#[nn]
    iCV = x0, z, smarts
    soln = odeint(modelPP, iCV, t, args=(alpha, beta, gamma, delta, smartCoeff))
    X, Y, S = soln.T
    ax.plot(X, Y, label = ''.join("y0: {} ".format(z0)))#)))[nn])))

ax.set_title('Smart Prey - Lokta-Volterra Phase Plot', c = 'k', fontsize = 24)
ax.set_xlabel('Prey Population', fontsize = 22, c = 'k')
ax.set_ylabel('Predator Population', fontsize = 22, c = 'k')
legend = ax.legend(labelcolor = 'k', facecolor = 'k', framealpha = 0, frameon = False)
#ax.set_ylim(0, 12.2)

print(S)
plt.show()

#All graphs
#----------------------------------------------------#
for i in range(3):
    var_name = 'var{}'.format(i)
    locals()[var_name] = i

#----------------------------------------------------#


fig, (ax, ax1) = plt.subplots(1, 2, figsize = (1280/96, 720/96), dpi = 96) 
#fig.patch.set_alpha(0.0)
#ax.patch.set_alpha(0.0)
ax.plot(t, X, 'r', alpha=1, lw=2, label='Prey')
ax.plot(t, Y, 'b', alpha=1, lw=2, label='Predator')
ax.set_title('Smart Prey - Lotka-Volterra Solution', c = 'k', fontsize = 20)
ax.set_xlabel('Time (days)', fontsize = 18, c = 'k')
ax.set_ylabel('Population', fontsize = 18, c = 'k')
#ax.set_ylim(0, 12.2)

#ax.spines['bottom'].set_color('w')
#ax.spines['top'].set_color('w') 
#ax.spines['right'].set_color('w')
#ax.spines['left'].set_color('w')
#fig.suptitle("MAVEN Flux-Energy")

#ax.tick_params(axis='x', colors='w', labelsize = 16)
#ax.tick_params(axis='y', colors='w', labelsize = 16)

#ax1.patch.set_alpha(0.0)
ax1.set_title('Phase Plot for Solution', c = 'k', fontsize = 20)
ax1.plot(X, Y, c = 'g', alpha = 1, lw = 2)
#ax1.set_xlim(0, 12)
#ax1.set_ylim(0, 6.2)
ax1.set_xlabel('Prey Population', fontsize = 18, c = 'k')
ax1.set_ylabel('Predator Population', fontsize = 18, c = 'k')

#ax1.tick_params(axis='x', colors='k', labelsize = 16)
#ax1.tick_params(axis='y', colors='k', labelsize = 16)

#ax.set_ylim(0,1.1)
#ax.yaxis.set_tick_params(length=0)
#ax.xaxis.set_tick_params(length=0)
#ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend(labelcolor = 'k', facecolor = 'k', framealpha = 0, frameon = False, fontsize = 18)
#legend.get_frame().set_alpha(0)

#for spine in ('top', 'right', 'bottom', 'left'):
 #   ax.spines[spine].set_visible(False)
  #  ax1.spines[spine].set_visible(False)
plt.show()