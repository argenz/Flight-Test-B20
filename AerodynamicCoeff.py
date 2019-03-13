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
import numpy as np
from scipy import stats
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

#plt.figure()
#plt.plot(alpha, CL)
#plt.show()
#   
Tl = [3642.21, 2996.15, 2413.35, 1882.48, 1918.05, 2235.97]	
Tr = [3745.21, 3057.76, 2540.09, 2035.8, 	2100.45, 2433.76]
	
T = []
CD = []
for i in range(len(Tl)):
    t = (Tl[i]+Tr[i])/2
    T.append(t)	
    cd = t/(0.5*rho[i]*VAS[i]**2*S)
    CD.append(cd)
    
#FINDING CD0 
poli = np.polyfit(CL, CD, 2)
CL1 = np.linspace(0, CL[-1], 20)
CD1 =  []
for i in range(len(CL1)):
    cd = poli[0]*CL1[i]**2 + poli[1]*CL1[i] + poli[2]
    CD1.append(cd)
    
CD0 = CD1[0]

#FINDING OSWALD EFFICIENCY

E =[]
for i in range(len(CD)):
    e = CL[i]**2/((CD[i]-CD0)*A*pi)
    E.append(e)

slope = stats.linregress(np.array(CL)**2, CD)[0]
e = 1/(slope*A*pi)






















