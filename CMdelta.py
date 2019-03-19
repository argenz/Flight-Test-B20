# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:56:10 2019

@author: biron
"""

from findCG import *
from DataReader import *
from data_processing import *
from ISAmodule import *



rho0 = 1.225
time = get_Data2()[13]
delta_e = get_Data2()[17]
IAS_cg = get_Data2()[15]

h = get_Data2()[14]

h_cg = [(h[0]+h[1])/2]

rho = ISA_rho(h_cg)

t1 = time[0] + UTC_Seconds[0]
t2 = time[1] + UTC_Seconds[0]

UTC_sec = (t1+t2)/2

cg_delta = (cg_time(t2,cg_walk) - cg_time(t1,cg_normal))*0.0254 #inches --> meter
curly_delta_e = delta_e[1]-delta_e[0] #rad
#V = IAS_cg[0]*sqrt(rho0/rho[0]) #m/s
total_mass = (3655 + fuel_mass(UTC_sec) + sum(mppl_lbs))*0.45359237    #lbs --> kg
c = 2.0569 #m
S = 30 #m	


C_n = total_mass/((1/2)*S*(IAS_cg[0]**2)*rho0)

Cm_delta = -(1/curly_delta_e)*C_n*(cg_delta/c)
print(Cm_delta)




