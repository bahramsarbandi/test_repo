import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd

SP = pd.read_csv('RFD.csv')
SP.columns = ['u', 'RF']
print(SP.head())
plt.plot(SP.u,SP.RF, color='blue')
plt.show()
plt.fill_between(SP.u,SP.RF)
plt.show()

road = pd.read_csv('road.csv')
road.columns = ['v', 'RF3']
print(road.head())
plt.plot(road.v,road.RF3, color='red')
plt.show()
plt.fill_between(road.v,road.RF3)
plt.show()

##plt.plot(SP.u,SP.RF, color='blue')
plt.plot(road.v,road.RF3, color='red')
##plt.fill_between(road.v,road.RF3, SP.RF, color='green', alpha=0.4)
plt.fill_between(road.v,road.RF3, color='green', alpha=0.4)
plt.xlabel('Displacement (mm)')
plt.ylabel('RF3 (N)')
plt.show()

plt.xlim([0, 45])
plt.ylim([0, 1500])
##plt.plot(SP.u,SP.RF, color='blue')
plt.plot(road.v,road.RF3, color='red')
##plt.fill_between(road.v,road.RF3, SP.RF, color='green', alpha=0.4)
plt.fill_between(road.v,road.RF3, color='green', alpha=0.4)
plt.grid()
plt.show()
