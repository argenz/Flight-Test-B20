#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:51:54 2019

@author: FCRA
"""
import numpy as np
from Numerical_Sim import InitSS
from TestDeflect import  SimulateSymmResponse, SimulateAsymmResponse
from Cit_par import *
#MAIN 

sys_symm, sys_asymm = InitSS()

if motion == 1 or 2:
    SimulateSymmResponse(sys_symm, Ue, uValid, alphaValid, pitchValid, pitchRateValid)

elif motion == 3 or 4 or 5:
    SimulateAsymmResponse(sys_asymm, Ua, Ur, rollValid, rollRateValid, yawRateValid)

    


    
   
    
    
    