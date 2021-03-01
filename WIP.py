
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pylab import *
import pandas as pd

X = pd.read_csv('owid-covid-data.csv')

XF = X[(X == 'GBR').any(axis = 1)]

xx = pd.to_datetime(XF["date"], format = '%d/%m/%Y')
#xx = xx.dt.strftime('%d/%m/%Y')

yy = ((XF.filter(regex = 'new_cases_smoothed$', axis = 1))/(67))

xLength = np.linspace(0, len(XF) -1, len(XF))


#outputArr = np.asarray[[list(xLength)], [list(yy)]]
#print(outputArr)

#with open('UKData.txt', 'w') as filehandle:
 #   for listitem in outputArr:
  #      filehandle.write('%s\n' % listitem)


print(xx)
print(yy)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(xLength, yy, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.set_xlabel('Date')
ax.set_ylabel('Daily confirmed Cases Per Million')
#ax.xaxis.set_major_locator(mdates.MonthLocator())
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
#plt.xticks(rotation=45)
#ax.xaxis.set_minor_locator(mdates.DayLocator())
#ax.grid(b=True, which='minor', c='black', lw=0.5, ls='-')
#ax.grid(b=True, which='major', c='black', lw=0.5, ls='-')
plt.show()
