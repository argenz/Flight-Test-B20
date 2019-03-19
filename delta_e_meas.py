# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:06:21 2019

@author: hksam
"""
from ParameterReader import ISAmodule, cessna, OpenThrustFile
from AerodynamicCoeff import AerodynamicCoeffFunc
from DataReader import get_Data2
import numpy as np

def delta_e(aircraft, delta_e_meas):
      
    #To minimize this error, we choose its value at the thrust "normally"
    #required to sustain horizontal flight at the measurement conditions.
    
    # constants
    CmTc =  -0.0064
    mdot_fs = 0.048 # kg/s
    Diameter = 686. # m
    Radius = Diameter/2
    F = OpenThrustFile("thrust.DAT")
    
    def GetThrustCoeff(ISAmodel, thrustL, thrustR, aircraft):
        
        Tavg = []
        Tc = []

        
        for i, thrust in enumerate(thrustL):
            Tavgi = np.average((thrust, thrustR[i]))
            Tci = Tavgi/(0.5*ISAmodel.rho0*VAS[i]**2*np.pi*Radius**2)
            Tavg.append(Tavgi)
            Tc.append(Tci)
        return Tc
    
    def GetStandardThrustCoeff(mdot):
        Tcs = []
        for v in VAS:
            Tcsi = mdot/(0.5*ISAmodule.rho0*v*np.pi*Radius)
            Tcs.append(Tcsi)
        return Tcs

    VAS = AerodynamicCoeffFunc(get_Data2(), cessna, Tl, Tr)[4]
    Tc = GetThrustCoeff(ISAmodule, F[:,0], F[:,1], cessna)
    Tcs = GetStandardThrustCoeff(mdot_fs)

    dDelta_e = []
    
    for i, Tci in enumerate(Tc):
        
        dDelta_ei = delta_e_meas[i] - 1/aircraft.LongStab.Cmde * CmTc * (Tcs[i] - Tci)    
        dDelta_e.append(dDelta_ei)

#T_c = ThrustCoeff(VAS, ISAmodule, Tl, Tr, cessna)

    return dDelta_e

print (delta_e(cessna, get_Data2()[6]))
    