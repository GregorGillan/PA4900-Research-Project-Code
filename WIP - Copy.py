
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pylab import *
import pandas as pd

L = [1,2]
y = [2, 4]
z = [7,8]

#L = pd.DataFrame(L)
#y = pd.DataFrame(y)
df = pd.DataFrame()
df[len(df.columns)] = L
df[len(df.columns)] = y
df[len(df.columns)] = z
#df[''] = L
#df[''] = y
#L = L.insert(L[-1], y)
#L[''] = np.array(y)
#L = L.append(z)

print(df)