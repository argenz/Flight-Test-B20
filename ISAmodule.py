#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:47:18 2017

@author: FCRA
"""
import numpy as np

def ISA_rho(h_list):
    
    
    HBase = [0, 11000, 20000, 32000, 47000, 51000, 71000, 84852]
    HTop = HBase[1:]+[100000]
    T0 = [288.15, 216.5, 216.5, 228.5, 270.5, 270.5, 214.5 ,186.8 ,-86.2+273.15]
    rho0 = [1.225, 0.36392, 0.08803, 0.01322, 0.00142, 0.00086, 0.00006,0]
#    P0 = [101325, 22632, 5474.9, 868.02, 110.91, 66.939, 3.9564, 0.3734]
    a = [-0.0065, 0, 1.0, 0.0028, 0, 0.0028, -0.002, 0]
     
    rho = []
    for h in h_list:
        
        i = 0
        while h>HTop[i]:
            i = i+1
            
    #    print "layer ", i
        if i==1 or i==4 or i==7:
            T = T0[i]
    #        P = P0[i]*(np.e**(-9.80665 / (287*T)*(h - HBase[i])))
            rho1 = rho0[i]*(np.e**(-9.80665 / (287*T)*(h - HBase[i])))
            rho.appned(rho1)
        else:
            T = T0[i] + a[i]*h
    #        P = P0[i]*(T/T0[i])**(-9.80665/(a[i]*287))
            rho2 = rho0[i]*(T/T0[i])**(-9.80665/(a[i]*287)-1)
            rho.append(rho2)  
    #    print"Density =", rho,"kg/m^3    - OR -    ", rho*0.062427961,"lb/cu ft"
    #    print"Pressure =", float(P),"Pa    - OR -    ", float(P)*0.0001450777202,"psi"
    #    print"Temperature =", T,"K    - OR -    ", T-273.25, "°C"   
        
    return rho  


    


