#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:52:41 2019

@author: FCRA
"""
from DataReader import get_Data1
#from ISAmodule import ISA_rho
#from Cit_par import *
from ParameterReader import cessna, ISAmodule, OpenThrustFile, GetAirspeeds
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from readmat import UTC_Seconds
from findCG import GetMass

def AerodynamicCoeffFunc(data, aircraft, ThrustL, ThrustR):
    
    # get data from DataReader
    IAS = data[4]
    TAT = data[9]
    hp = data[3]
    time = data[2]
    
    rho = []
    for hi in hp:
        rhoi, Ti = ISAmodule.ISA_rho(hi)
        rho.append(rhoi)                        #get rho from altitudes
        
    TAS = []
    CL = []
    
    for i in range(len(IAS)):                #convert to True airspeed
        tas = GetAirspeeds(IAS[i], TAT[i], hp[i], time[i])[1]
#        print tas
        print "M:", GetAirspeeds(IAS[i], TAT[i], hp[i], time[i])[0]
#        tas = np.sqrt(ISAmodule.rho0/rho[i])*IAS[i]
        TAS.append(tas)
        W = GetMass(UTC_Seconds[0]+time[i])
#        print W
        cl = W/(.5*rho[i]*tas**2*cessna.Geometry.S)
        CL.append(cl)

    CD = []
    for i in range(len(ThrustL)):
        Ti = ThrustL[i]+ThrustR[i]
        cd = Ti/(.5*rho[i]*TAS[i]**2*cessna.Geometry.S)
        CD.append(cd)

    #FINDING CD0 
    poli = np.polyfit(CL, CD, 2)
    CD0 = poli[2]
    
    #FINDING OSWALD EFFICIENCY
    slope = stats.linregress(np.array(CL)**2, CD)[0]
    
    e = 1/(slope*cessna.Geometry.A*np.pi)
    return CL, CD0, CD, e, TAS

F = OpenThrustFile("thrust1n.DAT")
CL, CD0, CD, e, TAS = AerodynamicCoeffFunc(get_Data1(), cessna, F[:,0], F[:,1])
alpha = get_Data1()[5]
plt.scatter(np.rad2deg(alpha), CL)
print "CLa:", stats.linregress(alpha,CL)[0], "CD0:", CD0, "e:", e

# e: 0.7813870700721104; CD0: 0.02072961029837115; CLa = 4.2878514154047185












