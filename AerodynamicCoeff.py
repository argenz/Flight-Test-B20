#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:52:41 2019

@author: FCRA
"""
from DataReader import get_Data1
#from ISAmodule import ISA_rho
#from Cit_par import *
from ParameterReader import cessna, ISAmodule, OpenThrustFile
#import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Tl = [3642.21, 2996.15, 2413.35, 1882.48, 1918.05, 2235.97]	
#Tr = [3745.21, 3057.76, 2540.09, 2035.8, 	2100.45, 2433.76]
def AerodynamicCoeffFunc(data, aircraft, ThrustL, ThrustR):
    mppl = data[0]                    #mass of people
    OEW = 3504                               #kg 
    mfuel = data[1]                   #mass of fuel 
    W = (mppl+OEW+mfuel)*9.81 

    hp = data[3]                      #altitude
    rho =[]
    for i in hp:
        irho, iT = ISAmodule.ISA_rho(i)
        rho.append(irho)                     #get rho from altitudes


    IAS = data[4]                     #indicated airspeed 
    VAS =  []
    CL = []
    for i in range(len(IAS)):                #convert to True airspeed
        vas = np.sqrt(ISAmodule.rho0/rho[i])*IAS[i]
        VAS.append(vas)
        cl = W/(0.5*rho[i]*vas**2*cessna.Geometry.S)
        CL.append(cl)
    

    T = []
    CD = []
    for i in range(len(ThrustL)):
        t = (ThrustL[i]+ThrustR[i])
        T.append(t)	
        cd = t/(0.5*rho[i]*VAS[i]**2*cessna.Geometry.S)
        CD.append(cd)
        
    #FINDING CD0 
    poli = np.polyfit(CL, CD, 2)
    CD0 = poli[2]
    
    #FINDING OSWALD EFFICIENCY
    slope = stats.linregress(np.array(CL)**2, CD)[0]
    
    e = 1/(slope*cessna.Geometry.A*np.pi)
    return CL, CD0, CD, e, VAS













