# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:56:10 2019

@author: biron
"""

from findCG import *
from DataReader import *
from data_processing import *
from ISAmodule import *
from scipy import stats
from ParameterReader import GetAirspeeds
import numpy as np

rho0 = 1.225
time = get_Data2()[15]
delta_e = get_Data2()[19]
IAS_cg = get_Data2()[17]
TAT_cg = get_Data2()[-1]
h = get_Data2()[16]

h_cg = np.average(h)

rho = ISAmodule.ISA_rho(h_cg)[0]

t1 = time[0] + UTC_Seconds[0]
t2 = time[1] + UTC_Seconds[0]

UTC_sec = (t1+t2)/2

cg_delta = (cg_time(t2,cg_walk) - cg_time(t1,cg_normal)) #inches --> meter
curly_delta_e = delta_e[1]-delta_e[0] #rad
#V = IAS_cg[0]*sqrt(rho0/rho[0]) #m/s
total_mass = GetMass(UTC_sec)
c = 2.0569 #m
S = 30. #m	

##TODO: Get VTAS using code from delta_e_meas
RAS = GetAirspeeds(IAS_cg[0],TAT_cg[0], h_cg, np.average(time))[1]

C_n = total_mass/(.5*S*(RAS**2)*rho)

Cm_delta = -(1/curly_delta_e)*C_n*(cg_delta/c)
#print(Cm_delta)

delta_e_meas = (get_Data2()[8])
alpha = (get_Data2()[7]) 

ddelta_da = stats.linregress(alpha,delta_e_meas)[0]
Cma = -ddelta_da*Cm_delta

print "Cmde:", Cm_delta, "Cma:", Cma

#Cmde: -1.840864274760595 Cma: -0.7797024801826712




