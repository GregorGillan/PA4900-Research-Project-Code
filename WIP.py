import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from pylab import *

#defining functions
def modelRecovery(I, t):
    r = 1/7
    dIdt = - r * I  
    return dIdt


#inintial conditions
I_0 = 0.7

t = np.linspace(0, 20)

#solve ODE
I = odeint(modelRecovery, I_0, t)

#plotting results

plt.plot(t, I)

show()