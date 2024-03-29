import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

#Defining Initial conditions
#----------------------------------------------------#
n = 67E6 #Total population GM = 1000

I0 = 1#GM = 1
#Initial number of infected people
R0 = 0 #Initial number of recovered people GM = 0

#Everyone else 'S0', ie susceptable to infection initially
S0 = n - I0 - R0 

i = 0.2 #Infection rate GM = 0.2
r = 1/10 #Recovery rate (1/days) GM = 1/10

beta = 0#3.36986301369863e-4 #1/Life expectancy UK
#----------------------------------------------------#

oDays = 365 #All time 
t0 = np.linspace(0, oDays, oDays)
lStart = 160 #Lockdown start day
lLength = 20 #Lockdown end day

def timespace (oDays, lStart, lLength):
    tVT = np.linspace(0, lStart, lStart + 1)
    lckDwn = np.linspace(lStart, lStart + lLength + 1 , lLength + 2)
    aLckDwn = np.linspace(lStart + lLength + 1, oDays, oDays - (lStart + lLength))
    return tVT, lckDwn, aLckDwn
    #print(tVT)
    #print(lckDwn)
    #print(aLckDwn)
t1, t2, t3 = timespace(oDays, lStart, lLength)

#print(t1, t2, t3)

def modelSIR(y, t, n, i, r, beta):
    S, I, R = y
    dSdt = beta - i*S*I/n - beta*S #Susceptible model
    dIdt = i*S*I/n-r*I - beta*I #Infection model
    dRdt = r*I - beta*R #Infection model
    return dSdt, dIdt, dRdt


#Initial conditions vector
iCV1 = S0, I0, R0

solnU = soln1 = odeint(modelSIR, iCV1, t0, args = (n, i, r, beta))
SU, IU, RU = solnU.T

#integrating SIR equations over time grid
soln1 = odeint(modelSIR, iCV1, t1, args = (n, i, r, beta))
S1, I1, R1 = soln1.T

iCV2 = S1[-1], I1[-1], R1[-1]
iL = 0.5*i #Transmission rate in lockdown
soln2 = odeint(modelSIR, iCV2, t2, args = (n, iL, r, beta))
S2, I2, R2 = soln2.T

iCV3 = S2[-1]*1, I2[-1], R2[-1]
soln3 = odeint(modelSIR, iCV3, t3, args = (n, i, r, beta))
S3, I3, R3 = soln3.T



#defining Recovery function
fig = plt.figure(facecolor='k', figsize = (1280/96, 720/96), dpi = 96)
fig.patch.set_alpha(0.0)
ax = fig.add_subplot(111, axisbelow=True)
ax.patch.set_alpha(0.0)

def grph(t, S, I, R):
    ax.plot(t, S/n, 'r', ls = 'dashed', alpha=1, lw=2, label='Susceptible w/ Lockdown & Vaccinations')
    ax.plot(t, I/n, 'g', ls = 'dashed', alpha=1, lw=2, label='Infected w/ Lockdown & Vaccinations')
    ax.plot(t, R/n, 'b', ls = 'dashed', alpha=1, lw=2, label='Recovered w/ Lockdown & Vaccinations')

print(S1, S2, S3)

print(type(S1))

#S = np.ndarray.astype(dtype, S1, S2)
S = np.append(np.append(S1, S2), S3)
I = np.append(np.append(I1, I2), I3)
R = np.append(np.append(R1, R2), R3)

t00 = np.append(np.append(t1, t2), t3)
#grph(t2, S2, I2, R2)
#grph(t3, S3, I3, R3)

#Graphing unchanged pandemic
ax.plot(t0, SU/n, 'r', alpha=1, lw=2, label='Susceptible')
ax.plot(t0, IU/n, 'g', alpha=1, lw=2, label='Infected')
ax.plot(t0, RU/n, 'b', alpha=1, lw=2, label='Recovered')

grph(t00, S, I, R)

I = list(I1) + list(I2) +list(I3)

with open('listfile.txt', 'w') as filehandle:
    for listitem in I:
        filehandle.write('%s\n' % listitem)

ax.set_title('SIR Lockdown Modelling With Vaccinations', c = 'k', fontsize = 20)
ax.set_xlabel('Time (days)', c = 'k', fontsize = 18)
ax.set_ylabel('Proportion of Population', c = 'k', fontsize = 18)
ax.set_ylim(0,1.1)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
#ax.grid(b=True, which='major', c='w', lw=2, ls='-')
'''
ax.spines['bottom'].set_color('w')
ax.spines['top'].set_color('w') 
ax.spines['right'].set_color('w')
ax.spines['left'].set_color('w')

ax.tick_params(axis='x', colors='k', labelsize = 18)
ax.tick_params(axis='y', colors='k', labelsize = 18)
'''
legend1 = ax.legend(labelcolor = 'k', facecolor = 'k', framealpha = 0, frameon = False, fontsize = 14)
#ax.annotate(lab, xy=(0, 1), xycoords='axes fraction')
legend1.get_frame().set_alpha(0.5)
'''
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
'''
plt.show()
print(max(R)/n)
print(max(RU)/n)

result1 = np.where(I == np.amax(I))
result2 = np.where(IU == np.amax(IU))
print(result1[0])
print(result2[0])
'''
lab = [
    "Population: {}, ".format(n), 
    "S_0: {}, ".format(S0),
    "I_0: {}, ".format(I0),
    "R_0: {}, ".format(R0),
    "Infection Rate: {}, ".format(i),
    "Recovery Rate: {} ".format(r)
    ]
    
lab = ''.join(lab)
'''