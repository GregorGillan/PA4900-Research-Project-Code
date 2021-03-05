import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

#Defining Initial conditions
#----------------------------------------------------#
n = 68E6 #Total population GM = 1000

I0 = 1 #GM = 1 Initial number of infected people
R0 = 0 #Initial number of recovered people GM = 0

#Everyone else 'S0', ie susceptable to infection initially
S0 = n - I0 - R0 

i = 0.2 #Infection rate GM = 0.2
r = 1/10 #Recovery rate (1/days) GM = 1/10
#----------------------------------------------------#

oDays = 365 #All time 
t0 = np.linspace(0, oDays, oDays)
t_s = 160 #Lockdown start day
lLength = 20 #Lockdown end day

def timespace (oDays, t_s, lLength):
    tVT = np.linspace(0, lStart, lStart + 1)
    lckDwn = np.linspace(lStart, lStart + lLength + 1 , lLength + 2)
    aLckDwn = np.linspace(lStart + lLength + 1, oDays, oDays - (lStart + lLength))
    return tVT, lckDwn, aLckDwn

t1, t2, t3 = timespace(oDays, lStart, lLength)


def modelSIR(y, t, n, i, r):
    S, I, R = y
    dSdt = - i*S*I/n  #Susceptible model
    dIdt = i*S*I/n-r*I #Infection model
    dRdt = r*I #Infection model
    return dSdt, dIdt, dRdt


def lkDnModel(t_s, t_d):
    #timespace for lockdowns
    #----------------------------------------------------#
    t1 = np.linspace(0, t_s, t_s + 1) #Up to lockdown time
    t2 = np.linspace(t_s, t_s + t_d + 1 , t_d + 2) #Lockdown time
    t3 = np.linspace(t_s + t_d + 1, oDays, oDays - (t_s + t_d)) #After lockdown time
    #----------------------------------------------------#
    
    iCV1 = S0, I0, R0

    solnU = soln1 = odeint(modelSIR, iCV1, t0, args = (n, i, r))
    SU, IU, RU = solnU.T

    #integrating SIR equations over time grid
    soln1 = odeint(modelSIR, iCV1, t1, args = (n, i, r))
    S1, I1, R1 = soln1.T

    iCV2 = S1[-1], I1[-1], R1[-1]
    iL = 0.5*i #Transmission rate in lockdown
    soln2 = odeint(modelSIR, iCV2, t2, args = (n, iL, r))
    S2, I2, R2 = soln2.T

    iCV3 = S2[-1], I2[-1], R2[-1]
    soln3 = odeint(modelSIR, iCV3, t3, args = (n, i, r))
    S3, I3, R3 = soln3.T


#Initial conditions vector




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

def grph(t, S, I, R):
    ax.plot(t, S/n, 'b', alpha=0.5, lw=2, label='Susceptible w/ Lockdown')
    ax.plot(t, I/n, 'r', alpha=0.5, lw=2, label='Infected w/ Lockdown')
    ax.plot(t, R/n, 'g', alpha=0.5, lw=2, label='Recovered w/ Lockdown')

print(S1, S2, S3)

print(type(S1))

#S = np.ndarray.astype(dtype, S1, S2)
S = np.append(np.append(S1, S2), S3)
I = np.append(np.append(I1, I2), I3)
R = np.append(np.append(R1, R2), R3)

t00 = np.append(np.append(t1, t2), t3)
grph(t00, S, I, R)
#grph(t2, S2, I2, R2)
#grph(t3, S3, I3, R3)

#Graphing unchanged pandemic
ax.plot(t0, SU/n, 'dodgerblue', ls = 'dashed',  alpha=0.5, lw=2, label='Susceptible')
ax.plot(t0, IU/n, 'salmon', ls = 'dashed',  alpha=0.5, lw=2, label='Infected')
ax.plot(t0, RU/n, 'teal', ls = 'dashed',  alpha=0.5, lw=2, label='Recovered')


I = list(I1) + list(I2) +list(I3)

with open('listfile.txt', 'w') as filehandle:
    for listitem in I:
        filehandle.write('%s\n' % listitem)

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

