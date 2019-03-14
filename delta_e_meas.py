# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:06:21 2019

@author: hksam
"""
from ParameterReader import ISAmodule, Tl, Tr, cessna
from AerodynamicCoeff import AerodynamicCoeffFunc
from DataReader import get_Data1
import numpy as np

def delta_e(Cmde, Tcs, Tc, CmTc, delta_e_meas):
    
    dDelta_e = delta_e_meas - 1/Cmde * (Tcs - Tc)
    
    return dDelta_e

#To minimize this error, we choose its value at the thrust "normally"
#required to sustain horizontal flight at the measurement conditions.

def ThrustCoeff(V, ISAmodel, thrustL, thrustR, aircraft):
    T_avg = []
    T_c = []
    for i, thrust in enumerate(thrustL):
        T_avgi = np.average((thrust, thrustR[i]))
        T_ci = T_avgi/(0.5*ISAmodel.rho0*V[i]**2*cessna.Geometry.S)
        T_avg.append(T_avgi)
        T_c.append(T_ci)
    return T_c

VAS = AerodynamicCoeffFunc(get_Data1(), cessna, ISAmodule, Tl, Tr)[4]
T_c = ThrustCoeff(VAS, ISAmodule, Tl, Tr, cessna)


    