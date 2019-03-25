# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:01:22 2019

@author: biron
"""

from DataReader import *
#from ISAmodule import ISA_rho
from ParameterReader import ISAmodule, GetAirspeedsREF
import numpy as np
#CL-CD series 1

h1 = get_Data1()[3]
IAS1 = get_Data1()[4]
F_fl1 = get_Data1()[6]
F_fr1 = get_Data1()[7]
TAT1 = get_Data1()[9]
mppl1 = get_Data1()[0]
mfuel1 = get_Data1()[1]
F_used1 = get_Data1()[-2]
#Elevator trim curve

h2 = get_Data2()[5]
IAS2 = get_Data2()[6]
F_fl2 = get_Data2()[11]
F_fr2 = get_Data2()[12]
TAT2 = get_Data2()[14]
mppl2 = get_Data2()[0]
mfuel2 = get_Data2()[3]
F_used2 = get_Data2()[13]
## Standard Thrust Coefficient
mdot_fs = [0.048]*len(F_fl2) # kg/s

def thrust(h,IAS,F_fl,F_fr, TAT, mppl, mfuel, F_used):
    
    #constants
    k = 1.4   
    
    data_thrust = []
    for i, hi in enumerate(h):
        
        Wi = 9165*4.44822 + (mppl+mfuel - F_used[i])*ISAmodule.g

        # Get Mach number using GetAirSpeeds
        Mi = GetAirspeedsREF(IAS[i], TAT[i], hi, Wi)[0]
        
        # Compute Tdiff
        Ts_reali = TAT[i]/(1+((k-1)/2)*Mi**2)
        Tdiffi = Ts_reali - ISAmodule.ISA_rho(hi)[1]
        
        data_thrusti = [hi, Mi, Tdiffi, F_fl[i], F_fr[i]]
        data_thrust.append(data_thrusti)
        
#    print data_thrust
    datfile = open("matlab.dat","w+")
    
    for i in data_thrust:
        for j in i:
            datfile.write(str(j)+str(' '))
        datfile.write("\n") 
    
    datfile.close()
    
    return 

thrust(h2, IAS2, F_fl2, F_fr2, TAT2, mppl2, mfuel2, F_used2)