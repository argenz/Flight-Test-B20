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
from readmat import Pressure_Altitude, Body_Pitch_Rate
from Numerical_Sim import sys_symm, sys_asymm
from ParameterReader import cessna
#from test import sys_symm



##### MAIN ######
# Elevator input
U = make_list(Deflection_of_elevator, UTC_Seconds[0] + 2889, UTC_Seconds[0]+2980)

#dT = UTC_Seconds[1] - UTC_Seconds[0]
#T = np.linspace(U[0][1], U[0][-1], (len(U[0])-1))
#U0 = U[1][0]
#U = np.array(U[1][1::])
#U = U-U0

#validation input
uValid = make_list(true_Airspeed, UTC_Seconds[0] + 2889, UTC_Seconds[0]+2980)
alphaValid = make_list(aoa, UTC_Seconds[0] + 2889, UTC_Seconds[0]+2980)
pitchValid = make_list(Pitch_Angle, UTC_Seconds[0] + 2889, UTC_Seconds[0]+2980)
pitchRateValid = make_list(Body_Pitch_Rate, UTC_Seconds[0] + 2889, UTC_Seconds[0]+2980)

def SimulateResponse(sys, DefAileron, ValidVelocity, ValidAoA, ValidPitchAngle
                     , ValidPitchRate):
    #INPUT: SS model and given parameters of type list
    #OUTPUT: validation plots
    
#    #constants
#    KnotsToMs = 0.51444
    # make time vector
    T = np.linspace(DefAileron[0][0], DefAileron[0][-1],len(DefAileron[0]))
    print (T[2]-T[1])
    # make INPUT vector
    DefAileron0 = DefAileron[1][0]
    DefAileron = np.array(DefAileron[1][:])
    DefAileron = DefAileron - DefAileron0
    y = control.lsim(sys, DefAileron, T, np.zeros([len(sys.B),1]))
    
    def GetParametersSymm(lsimout):
        # INPUT: State vector from the lsim function
        # OUTPUT: returns the columns of the state space vector AND time vector
        # Description: Simple function to separate the tuple of size three into 
        # separate variables given the state space vector.
        
#        time_vector = lsimout[1]
        state_vector = lsimout[2]

        #Y1: symmetrical case: Y1 = u_curl, Y2 = AoA, Y3 = theta/pitch, Y4 = pitch rate
        Y1 = state_vector[:,0]
        Y2 = state_vector[:,1]
        Y3 = state_vector[:,2]
        Y4 = state_vector[:,3]
        
        return Y1, Y2, Y3, Y4
    
    if np.size(sys.B) == 4:
        u_curl, AoA, PitchAngle, PitchRate_curl = GetParametersSymm(y)
        uNum = u_curl* cessna.StatFlightCond.V0
        PitchRate = PitchRate_curl * cessna.StatFlightCond.V0/cessna.Geometry.c
        print ValidVelocity[1]
    else: raise ValueError
#    elif np.size(sys.B) == 8:
#        beta, phi, p_curl, r_curl = GetParametersSymm(y)
#        p = p_curl * 2*cessna.StatFlightCond.V / cessna.Geometry.b
#        r = r_curl * 2*cessna.StatFlightCond.V / cessna.Geometry.b
        
    
    ## subtract 1st element from all lists
    
    #validation lists
#    ValidAoA[1] = ValidAoA[1] - ValidAoA[1][0]
#    ValidVelocity[1] = np.asarray(ValidVelocity[1]) - cessna.StatFlightCond.V0
#    ValidPitchAngle[1] = ValidPitchAngle[1] - ValidPitchAngle[1][0]
#    ValidPitchRate[1] = ValidPitchRate[1] - ValidPitchRate[1][0]
    
    #Numerical lists
#    uNum = uNum - cessna.StatFlightCond.V0
#    AoA = AoA - cessna.StatFlightCond.alpha0
#    PitchAngle = PitchAngle - cessna.StatFlightCond.th0
#    PitchRate = PitchRate - PitchRate[0]
    
    plt.subplot(411)
    plt.plot(ValidVelocity[0], ValidVelocity[1], label = "Validation velocity")
    plt.plot(T, uNum, label = "Numerical: velocity")
    plt.legend()
    plt.subplot(412)
    plt.plot(T, AoA, label = "AoA")
    plt.plot(ValidAoA[0], ValidAoA[1], label = "AoA validation")
    plt.legend()
    plt.subplot(413)
    plt.plot(T, PitchAngle, label = "pitch angle")
    plt.plot(ValidPitchAngle[0], ValidPitchAngle[1], label = "pitch angle Validation")
    plt.legend()
    plt.subplot(414)
    plt.plot(T, PitchRate, label = "pitch rate")
    plt.plot(ValidPitchRate[0], ValidPitchRate[1], label = "pitch rate validation")
    #plt.plot(time, pitch_rate, label = "dimensionless pitch rate")
    plt.legend()
    plt.show()
    
    print("done")
    return
print(SimulateResponse(sys_symm, U, uValid, alphaValid, pitchValid, pitchRateValid))
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