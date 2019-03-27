# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:00:41 2019

@author: hksam
"""

import numpy as np
import matplotlib.pyplot as plt
import control.matlab as control
from Numerical_Sim import InitSS
import control.matlab as control
from Cit_par import *
def InitialSim(sys, X0, T, title):
    #plotting
    
    y,t = control.initial(sys, T, X0)
    
    uNum = y[:,0]
    AoA =y[:,1]
    PitchAngle = y[:,2]
    PitchRate = y[:,3]
    
    legendloc = 2
    plt.figure()
    plt.rcParams.update({'font.size': 18})

    plt.subplot(411)
    plt.title(r"Initial Value Problem: " + str(title))
    plt.plot(T, uNum)
    plt.gca().set_ylabel('u [m/s]')        
    plt.xlim(left = 0)
    
    plt.subplot(412)
    plt.plot(T, AoA)
    plt.gca().set_ylabel(r'$\alpha$ [rad]')        
    plt.xlim(left = 0)  
    
    plt.subplot(413)
    plt.plot(T, (PitchAngle))
    plt.gca().set_ylabel(r'$\theta$ [rad]')
    plt.xlim(left = 0)   
    
    plt.subplot(414)
    plt.plot(T, PitchRate)
    plt.gca().set_ylabel('q [rad/s]')        
    plt.gca().set_xlabel('time [s]')
    plt.xlim(left = 0)
    
    plt.show()
    
    return True

sys_symm, sys_asymm = InitSS()

#X0 = np.zeros([4,1])
#X0[0] = 10*V0
#T = np.linspace(0, 70, 200)
#title = r"$u$ = 10 [m/s]"
#InitialSim(sys_symm, X0, T, title)

#X0 = np.zeros([4,1])
#X0[1] = 0.1
#T = np.linspace(0, 5, 200)
#title = r"$\alpha$ = 0.10 [rad]"
#InitialSim(sys_symm, X0, T, title)

#X0 = np.zeros([4,1])
#X0[2] = 0.1
#T = np.linspace(0, 100, 1000)
#title = r"$\theta$ = 0.10 [rad]"
#InitialSim(sys_symm, X0, T, title)

#X0 = np.zeros([4,1])
#X0[3] = 2*0.10*c/V0*1000
#T = np.linspace(0, 70, 200)
#title = r"$q$ = 0.10 [rad/s]"
#InitialSim(sys_symm, X0, T, title)

def InitialSimA(sys, X0, T, title):
    #plotting
    
    y,t = control.initial(sys, T, X0)
    
    yaw = y[:,0]
    roll =y[:,1]
    roll_rate = y[:,2]
    yaw_rate = y[:,3]
    
    plt.figure()
    plt.rcParams.update({'font.size': 18})

    plt.subplot(411)
    plt.title(r"Initial Value Problem: " + str(title))
    plt.plot(T, yaw)
    plt.gca().set_ylabel(r'$\beta$ [rad]')        
    plt.xlim(left = 0)
    
    plt.subplot(412)
    plt.plot(T, roll)
    plt.gca().set_ylabel(r'$\phi$ [rad]')        
    plt.xlim(left = 0)  
    
    plt.subplot(413)
    plt.plot(T, roll_rate)
    plt.gca().set_ylabel(r'$p$ [rad/s]')
    plt.xlim(left = 0)   
    
    plt.subplot(414)
    plt.plot(T, yaw_rate)
    plt.gca().set_ylabel('r [rad/s]')        
    plt.gca().set_xlabel('time [s]')
    plt.xlim(left = 0)
    
    plt.show()
    
    return True

X0 = np.zeros([4,1])
X0[0] = 0.10
T = np.linspace(0, 20, 2000)
title = r"$\beta$ = 0.10 [rad]"
InitialSimA(sys_asymm, X0, T, title)
#
X0 = np.zeros([4,1])
X0[1] = 0.10
T = np.linspace(0, 20, 2000)
title = r"$\phi$ = 0.10 [rad]"
InitialSimA(sys_asymm, X0, T, title)

X0 = np.zeros([4,1])
X0[2] = .10*2*V0/b
T = np.linspace(0, 20, 2000)
title = r"$p$ = 0.10 [rad/s]"
InitialSimA(sys_asymm, X0, T, title)
#
X0 = np.zeros([4,1])
X0[3] = .10*2*V0/b
T = np.linspace(0, 20, 2000)
title = r"$r$ = 0.10 [rad/s]"
InitialSimA(sys_asymm, X0, T, title)

