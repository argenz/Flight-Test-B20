# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:01:22 2019

@author: biron
"""

from DataReader import *
#from ISAmodule import ISA_rho
from ParameterReader import ISAmodule
import numpy as np
#CL-CD series 1

h1 = get_Data1()[3]
IAS1 = get_Data1()[4]
F_fl1 = get_Data1()[6]
F_fr1 = get_Data1()[7]
TAT1 = get_Data1()[9]

##Elevator trim curve
#
h2 = get_Data2()[5]
IAS2 = get_Data2()[6]
F_fl2 = get_Data2()[11]
F_fr2 = get_Data2()[12]
TAT2 = get_Data2()[14]

## Standard Thrust Coefficient
mdot_fs = [0.048]*len(F_fl2) # kg/s

def thrust(h,IAS,F_fl,F_fr,TAT):
    
    #constants
    k = 1.4   
    
    data_thrust = []
    for i, hi in enumerate(h):
        
        # Compute temperature
        Tsi = ISAmodule.ISA_rho(hi)[1]
        # Compute speed of sound
        ai = np.sqrt(k*ISAmodule.R*Tsi)
#        print ai
        # compute Mach number
        Mi = IAS[i]*np.sqrt(ISAmodule.rho0/ISAmodule.ISA_rho(hi)[0])/ai
#        print Mi
        # Compute Tdiff
        Ts_reali = TAT[i]/(1-((k-1)/2)*Mi**2)
        Tdiffi = Ts_reali - ISAmodule.ISA_rho(hi)[0]
        
        data_thrusti = [hi, Mi,Tdiffi, F_fl[i], F_fr[i]]
        data_thrust.append(data_thrusti)
        
#    print data_thrust
    datfile = open("matlab.dat","w+")
    
    for i in data_thrust:
        for j in i:
            datfile.write(str(j)+str(' '))
        datfile.write("\n") 
    
    datfile.close()
    
    return 
    
thrust(h2, IAS2, mdot_fs, mdot_fs, TAT2)