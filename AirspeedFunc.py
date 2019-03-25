# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:19:50 2019

@author: hksam
"""
import numpy as np
from ParameterReader import ISAmodule
from DataReader import get_Data2, get_Data1
from findCG import GetMass
from readmat import UTC_Seconds

IAS = get_Data2()[6]
TAT = get_Data2()[14]
hp = get_Data2()[5]
time = get_Data2()[4]
def GetAirspeeds(IAS, TAT, h, t):
    #INPUT: Indicated airspeed, Total Air Speed
    #OUTPUT: Mach number, equivalent airspeed (EAS), true airspeed (TAS)
    #description: Using material discussed in App. B, get EAS
        # constants:
    ymin1 = ISAmodule.gamma-1
    gamma = ISAmodule.gamma
    rho0 = ISAmodule.rho0
    p0 = ISAmodule.p0    
    
    def GetMachNumber(IAS):

        mps2knots = 1.94384449
        knots2mps = 0.514444444
        # IAS to CAS see App. A
        CAS = (IAS*mps2knots - 2) *knots2mps # in m/s
        
        # get pressure ratio
        p_p0 = (1+gamma*h/ISAmodule.temp0)**(-ISAmodule.g/(gamma*ISAmodule.R))
        

        
        M = np.sqrt(2/(ymin1)*((1+p_p0*((1+ymin1/(2*gamma)*rho0/p0*CAS**2)**(gamma/ymin1)-1))**(ymin1/gamma)-1))
        
        if M > 0.7:
            raise ValueError("This is not realistic")
            
        ## calibrate Mach number see App. A
        M = M - 0.07
        return M
    
    M = GetMachNumber(IAS)
    
    # get static temperature from TAT
    T = TAT/(1+ymin1/2*M**2)
    
    # get density ratio (ISA model)
    rho_rho0 = ISAmodule.ISA_rho(h)[0]/ISAmodule.rho0
    
    # get speed of sound
    a = np.sqrt(gamma * ISAmodule.R * T)
    
    # true airspeed
    TAS = M * a
    
    # equivalent airspeed
    EAS = TAS* np.sqrt(rho_rho0)
    
    
    W = GetMass(UTC_Seconds[0]+t)
    Ws = 60500./ISAmodule.g
    
    RAS = EAS*np.sqrt(Ws/W)
    
    
    return M, TAS, EAS, RAS

#print GetAirspeeds(IAS[0], TAT[0], hp[0], time[0])

    