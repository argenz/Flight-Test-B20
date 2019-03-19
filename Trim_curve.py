# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:44:52 2019

@author: biron
"""

import matplotlib.pyplot as plt

from delta_e_meas import *
from DataReader import *
from ParameterReader import cessna
from CMdelta import Cm_delta

from scipy import stats
mdot_fs = 0.048

aoa = get_Data2()[5]
print(aoa)
delta_e = delta_e(cessna, get_Data2()[6])
print(delta_e)


slope = stats.linregress(aoa,delta_e)[0]
intercept = stats.linregress(aoa,delta_e)[1]
slope_aoa = [i*slope for i in aoa]


Cm_a = -slope*Cm_delta
print(Cm_a)


plt.plot(aoa,delta_e, "o", label="original data")
plt.plot(aoa, intercept + slope_aoa, "r", label="fitted line")
plt.show()

