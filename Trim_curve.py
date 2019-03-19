# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:44:52 2019

@author: biron
"""

import matplotlib.pyplot as plt

from delta_e_meas import *
from DataReader import *
from ParameterReader import cessna, ISAmodule, OpenThrustFile
from CMdelta import Cm_delta
from findCG import *
from data_processing import *
from AerodynamicCoeff import *
import numpy as np


from scipy import stats

Ws = 3655 #N
Tl = OpenThrustFile("thrust.dat")[:,0]
Tr = OpenThrustFile("thrust.dat")[:,1]
W = (3655 + fuel_mass(UTC_sec) + sum(mppl_lbs))*0.45359237
mdot_fs = 0.048
VAS = AerodynamicCoeffFunc(get_Data2(), cessna, Tl, Tr)[4]

aoa = get_Data2()[5]
delta_e = delta_e(cessna, get_Data2()[6])


#finding slope and other shit for angle of attack and delta_e

slope1 = stats.linregress(aoa,delta_e)[0]
intercept1 = stats.linregress(aoa,delta_e)[1]
slope_aoa = [i*slope1 for i in aoa]


#Cm_alpha calculated with slope of aoa and delta_e
Cm_a = -slope1*Cm_delta


VE = []
for i in VAS:
    ve = i**sqrt(Ws/W)
    VE.append(ve)
print(VE)

#finding slope and other shit for VE and delta_e

slope2 = stats.linregress(VE,delta_e)[0]
intercept2 = stats.linregress(VE,delta_e)[1]
slope_VE = [i*slope2 for i in VE]
#
#plot for angle of attack versus delta_e
plt.subplot(1,2,1)
plt.plot(aoa,delta_e, "o", label="original data")
plt.plot(aoa, intercept1 + slope_aoa, "r", label="fitted line")
#plot for VE versus delta_e
plt.subplot(1,2,2)
plt.plot(VE,delta_e, "o", label="original data")
plt.plot(VE, intercept2 + slope_VE, "r", label="fitted line")
#
plt.show()

