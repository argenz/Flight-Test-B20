# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:01:22 2019

@author: biron
"""

from DataReader import *
from ISAmodule import *
#constants
k = 1.4
R = 286.9
lamb = -0.0065
rho0 = 1.225

h = get_Data1()[3]
IAS = get_Data1()[4]
F_fl = get_Data1()[6]
F_fr = get_Data1()[7]
TAT = get_Data1()[9]

rho = get_ISA_rho(h)


c = []
for i in range(len(TAT)):
    x = (k*R*TAT[i])**(1/2)
    c.append(x)


Mach = []
for i in range(len(TAT)):
    m = IAS[i]*sqrt(rho0/rho[i])/c[i]
    Mach.append(m)
    
Ts = []
for i in range(len(TAT)):
    x = TAT[i]/(1-((k-1)/2)*Mach[i]**2)
    Ts.append(x)
    
Tdif = []
for i in range(len(TAT)):
    x = 288.15 + (lamb * h[i])
    dif = Ts[i] - x
    Tdif.append(dif)

data_thrust = []    
for i in range(len(pres)):
    x = [ pres[i], Mach[i], Tdif[i], flow_left[i], flow_right[i]]
    data_thrust.append(x)

datfile = open("matlab.dat","w+")

for i in data_thrust:
    for j in i:
        datfile.write(str(j) + " ")
    datfile.write("\n")

datfile.close()