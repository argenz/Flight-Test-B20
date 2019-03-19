# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:02:58 2019

@author: hksam
"""
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as control
from data_processing import make_list
from readmat import Deflection_of_aileron, Deflection_of_elevator, Deflection_of_elevator
from readmat import UTC_Seconds, Deflection_elev_trim, aoa, Pitch_Angle, true_Airspeed
from readmat import Pressure_Altitude
from Numerical_Sim import sys_asymm
from test import sys_symm

def GetParametersSymm(lsimout):
    # INPUT: State vector from the lsim function
    # OUTPUT: returns the columns of the state space vector AND time vector
    # Description: Simple function to separate the tuple of size three into 
    # separate variables given the state space vector.
    
    time_vector = lsimout[1]
    state_vector = lsimout[2]
    
    u_curl = state_vector[:,0]
    alpha = state_vector[:,1]
    theta = state_vector[:,2]
    pitch_rate = state_vector[:,3]
    
    return u_curl, alpha, theta, pitch_rate, time_vector


##### MAIN ######
# Elevator input
U = make_list(Deflection_of_elevator, UTC_Seconds[0] + 2889, UTC_Seconds[0]+2980)

dT = UTC_Seconds[1] - UTC_Seconds[0]
T = np.linspace(U[0][1], U[0][-1], (len(U[0])-1))
U = np.array(U[1][1::])


U0 = U[0]
U = U - U0
y = control.lsim(sys_symm, U, T, np.zeros([4,1]))
u_curl, alpha, theta, pitch_rate, time = GetParametersSymm(y)


plt.figure(1)
plt.plot(time, u_curl, label = "u_curl")
plt.plot(time,alpha, label = "AoA")
plt.plot(time, theta, label = "pitch angle")
plt.plot(time, pitch_rate, label = "dimensionless pitch rate")
plt.legend()
plt.show()
#plt.plot(t,y)
#T = np.linspace(0, 20, 100)
#y,t = control.impulse(sys_symm,T)
##
#plt.plot(t,y)




#-----------------------------------------------------------------------------#
#print ("These are the values you need to set up:")
#hp = make_list(Pressure_Altitude, UTC_Seconds[0] + 2889,UTC_Seconds[0] + 2908)
#V     =  make_list(true_Airspeed, UTC_Seconds[0] + 2889,UTC_Seconds[0] + 2908)       # true airspeed in the stationary flight condition [m/sec]
#alpha =      make_list(aoa, UTC_Seconds[0] + 2889, UTC_Seconds[0] + 2908)       # angle of attack in the stationary flight condition [rad]
#th    =      make_list(Pitch_Angle, UTC_Seconds[0] + 2889, UTC_Seconds[0] + 2908)     # pitch angle in the stationary flight condition [rad]
#
#V0 = V[1][1]
#alpha0 = alpha[1][1]
#th0 = th[1][1]
#hp0 = hp[1][1]

# Simulation
#y,t = control.lsim(sys_symm, U[1][1::], T)