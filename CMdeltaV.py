#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:00:23 2019

@author: FCRA
"""
#ELEVATOR TRIM CURVE 
from math import *
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from DataReader import *
from ISAmodule import *
from Cit_par import *
from AerodynamicCoeff import *

#CM delta elevator

#Getting data
mppl = get_Data2()[0]
mfuel = get_Data2()[1]
alpha = get_Data2()[5]
delta_e = get_Data2()[6]
delta_tr  = get_Data2()[7]
F_e = get_Data2()[8]

#shift in cg
t_cg = get_Data2()[13]
alpha_cg = get_Data2()[16]
delta_e_cg = get_Data2()[17]
Ws = 60500 #N

def get_CM_delta():

   
    W =  Ws + (mppl+mfuel)*9.81
    delta_xcg = 1
    CN = CL
    deltadelta_e =  delta_e_cg[-1]-delta_e_cg[0]
    CM_delta = []
    
    for i in range(len(CN)):
        cm = 1/(deltadelta_e)*CN[i]*delta_xcg/c
        CM_delta.append(cm)
        
    return CM_delta
    
VE = []
for i in VAS:
    ve = i**sqrt(Ws/W)
    VE.append(ve)


#CM_alpha =  delta_e/alpha*CM_delta


#plt.figure()
#plt.plot(VE, CM_delta)
#plt.show()




