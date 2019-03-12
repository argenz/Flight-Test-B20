#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:52:41 2019

@author: FCRA
"""
from DataReader import get_Data1
from ISAmodule import *
from math import *
from Cit_par import *
import matplotlib.pyplot as plt

mppl = get_Data1()[0]                    #mass of people
oew = 3504                               #kg 
mfuel = get_Data1()[1]                   #mass of fuel 
W = (mppl+oew+mfuel)*9.81 

time  = get_Data1()[2]                   #time of measurements

hp = get_Data1()[3]                      #altitude
rho =[]
for i in hp:
    rho1 = ISA_rho(i)
    rho.append(rho1)                     #get rho from altitudes


IAS = get_Data1()[4]                     #indicated airspeed 
VAS =  []
CL = []
for i in range(len(IAS)):                #convert to True airspeed
    vas = sqrt(1.225/rho[i])*IAS[i]
    VAS.append(vas)
    cl = W/(0.5*rho[i]*vas**2*S)
    CL.append(cl)

alpha = get_Data1()[5]

plt.figure()
plt.plot(alpha, CL)
plt.show()
   

#TAT = get_Data1()[9]                    #temp

T = []








