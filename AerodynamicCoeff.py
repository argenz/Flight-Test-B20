#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:52:41 2019

@author: FCRA
"""
from DataReader import get_Data1
from ISAmodule import ISA_rho
#from Cit_par import *
from ParameterReader import cessna, Tl, Tr, ISAmodule
#import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def AerodynamicCoeffFunc(data, aircraft, ISAmodel, ThrustL, ThrustR):
    mppl = data[0]                    #mass of people
    OEW = 3504                               #kg 
    mfuel = data[1]                   #mass of fuel 
    W = (mppl+OEW+mfuel)*9.81 

    hp = data[3]                      #altitude
    rho =[]
    for i in hp:
        irho, iT = ISA_rho(i)
        rho.append(irho)                     #get rho from altitudes


    IAS = data[4]                     #indicated airspeed 
    VAS =  []
    CL = []
    for i in range(len(IAS)):                #convert to True airspeed
        vas = np.sqrt(ISAmodel.rho0/rho[i])*IAS[i]
        VAS.append(vas)
        cl = W/(0.5*rho[i]*vas**2*cessna.Geometry.S)
        CL.append(cl)
    

    T = []
    CD = []
    for i in range(len(ThrustL)):
        t = (ThrustL[i]+ThrustR[i])/2
        T.append(t)	
        cd = t/(0.5*rho[i]*VAS[i]**2*cessna.Geometry.S)
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
        e = CL[i]**2/((CD[i]-CD0)*cessna.Geometry.A*np.pi)
        E.append(e)
    
    slope = stats.linregress(np.array(CL)**2, CD)[0]
    e = 1/(slope*cessna.Geometry.A*np.pi)
    
    return CL, CD0, CD, e, VAS
















