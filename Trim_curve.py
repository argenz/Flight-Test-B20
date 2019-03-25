# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:44:52 2019

@author: biron
"""
import operator
import matplotlib.pyplot as plt

from delta_e_meas import delta_e
from DataReader import get_Data1, get_Data2
from ParameterReader import cessna, ISAmodule, OpenThrustFile, GetAirspeeds
from CMdelta import Cm_delta, UTC_sec
from findCG import *
from data_processing import *
from AerodynamicCoeff import *
import numpy as np
from scipy import stats

# retrieve data from DataReader
Tl = OpenThrustFile("thrustREF2.DAT")[:,0]
Tr = OpenThrustFile("thrustREF2.DAT")[:,1]
h = get_Data2()[5]
IAS = get_Data2()[6]
F_fl = get_Data2()[11]
F_fr = get_Data2()[12]
TAT = get_Data2()[14]
t = get_Data2()[4]

delta_estar = delta_e(cessna, get_Data2()[8])
#delta_estar = [deltai * -1 for deltai in delta_estar]
RAS = []

for i in range(len(h)): 
    RASi = GetAirspeeds(IAS[i], TAT[i], h[i], t[i])[-1]
    RAS.append(RASi)

fit = np.polyfit(RAS, delta_estar, 3)
#interpolation
V = np.linspace(50, 100, 10)
delta_efit = fit[0]*np.power(V,3) + fit[1]*np.power(V,2) + fit[2]*np.power(V,1) + fit[3]*np.power(V,0)

plt.figure()
plt.gca().invert_yaxis()
plt.scatter(RAS, delta_estar)
plt.plot(V, delta_efit, color = "r")
#plt.axhline(y = 0)
plt.xlabel("V [m/s]")
plt.ylabel("delta_e (-) [rad]")

