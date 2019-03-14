# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:06:21 2019

@author: hksam
"""
from ParameterReader import ISAmodule, Tl, Tr, cessna
from AerodynamicCoeff import AerodynamicCoeffFunc
from DataReader import get_Data1
import numpy as np

def delta_e(aircraft, delta_e_meas):
      
    #To minimize this error, we choose its value at the thrust "normally"
    #required to sustain horizontal flight at the measurement conditions.
    
    def GetThrustCoeff(V, ISAmodel, thrustL, thrustR, aircraft):
        Tavg = []
        Tc = []
        for i, thrust in enumerate(thrustL):
            Tavgi = np.average((thrust, thrustR[i]))
            Tci = Tavgi/(0.5*ISAmodel.rho0*V[i]**2*cessna.Geometry.S)
            Tavg.append(Tavgi)
            Tc.append(Tci)
        return Tc
    
    def GetStandardThrustCoeff():
        ## TODO: add func calculating Tsc with mdot_sc
        
        return False
    
    Tcs = GetStandardThrustCoeff()
    VAS = AerodynamicCoeffFunc(get_Data1(), cessna, ISAmodule, Tl, Tr)[4]
    Tc = GetThrustCoeff(VAS, ISAmodule, Tl, Tr, cessna)
    CmTc =  -0.0064
    dDelta_e = delta_e_meas - 1/aircraft.LongStab.Cmde * CmTc * (Tcs - Tc)    
    
#T_c = ThrustCoeff(VAS, ISAmodule, Tl, Tr, cessna)

    return dDelta_e
    