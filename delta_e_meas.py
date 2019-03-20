# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:06:21 2019

@author: hksam
"""
from ParameterReader import ISAmodule, cessna, OpenThrustFile
from AerodynamicCoeff import AerodynamicCoeffFunc
from DataReader import get_Data2
import numpy as np
from CMdelta import Cm_delta

def delta_e(aircraft, delta_e_meas):
      
    #To minimize this error, we choose its value at the thrust "normally"
    #required to sustain horizontal flight at the measurement conditions.
    
    # constants
    CmTc =  -0.0064

    Diameter = 686. # m
    Radius = Diameter/2
    F = OpenThrustFile("thrust2.DAT")
    Fs = OpenThrustFile("thrustfs.DAT")
    mppl = get_Data2()[0]
    mfuel = get_Data2()[1]
    OEW = 3655 ## PLACEHOLDER
    
    def GetReducedV(V):
#       INPUT: VAS
#       OUTPUT: LIST of equivalent reduced airspeed
        Ws = 60500
        VE = []
        W = sum(mppl) + (mfuel) + OEW
        for v in V:
            ve = v**np.sqrt(Ws/W)
            VE.append(ve)
        
        return VE
            
    def GetThrustCoeff(ISAmodel, thrustL, thrustR, aircraft):
        
        Tavg = []
        Tc = []

        
        for i, thrust in enumerate(thrustL):
            Tavgi = np.sum((thrust, thrustR[i]))
            Tci = Tavgi/(0.5*ISAmodel.rho0*Vreduced[i]**2*Diameter**2)
            Tavg.append(Tavgi)
            Tc.append(Tci)
        return Tc
    
    def GetStandardThrustCoeff(Fs):
        Tcs = []
        for i, vi in enumerate(Vreduced):
            Tcsi = np.sum(Fs[i])/(0.5*ISAmodule.rho0*vi**2*Diameter**2)
            Tcs.append(Tcsi)
        return Tcs

    VAS = AerodynamicCoeffFunc(get_Data2(), cessna, F[:,0], F[:,1])[4]
    Vreduced = GetReducedV(VAS)
    Tc = GetThrustCoeff(ISAmodule, F[:,0], F[:,1], cessna)
    Tcs = GetStandardThrustCoeff(Fs)
#    Vreduced
    dDelta_e = []
    
    for i, Tci in enumerate(Tc):
        
        dDelta_ei = delta_e_meas[i] - 1/Cm_delta * CmTc * (Tcs[i] - Tci)    
        dDelta_e.append(dDelta_ei)

#T_c = ThrustCoeff(VAS, ISAmodule, Tl, Tr, cessna)

    return dDelta_e

#print delta_e(cessna, get_Data2()[6])
    