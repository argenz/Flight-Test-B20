# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:02:58 2019

@author: hksam
"""
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as control
from Numerical_Sim import InitSS
from ParameterReader import cessna
from Cit_par import Ue, Ua, Ur, uValid, alphaValid, pitchValid, pitchRateValid
from Cit_par import rollValid, yawRateValid, rollRateValid
#from test import sys_symm

##### MAIN ######
def GetParametersSim(lsimout):
    # INPUT: State vector from the lsim function
    # OUTPUT: returns the columns of the state space vector AND time vector
    # Description: Simple function to separate the tuple of size three into 
    # separate variables given the state space vector.
    
    state_vector = lsimout[2]

    #Y1: symmetrical case: Y1 = u_curl, Y2 = AoA, Y3 = theta/pitch, Y4 = pitch rate
    Y1 = state_vector[:,0]
    Y2 = state_vector[:,1]
    Y3 = state_vector[:,2]
    Y4 = state_vector[:,3]
    
    return Y1, Y2, Y3, Y4
def SimulateSymmResponse(sys, DefElevator, ValidVelocity, ValidAoA, ValidPitchAngle
                     , ValidPitchRate):
    #INPUT: SS model and given parameters of type list
    #OUTPUT: validation plots
    
    # make time vector
    T = np.linspace(DefElevator[0][0], DefElevator[0][-1],len(DefElevator[0]))
#    print (T[2]-T[1])
    # make INPUT vector
    DefElevator0 = DefElevator[1][0]
    DefElevator = np.array(DefElevator[1][:])
    DefElevator = DefElevator - DefElevator0
    U0 = [[uValid[1][0]],[alphaValid[1][0]],
          [pitchValid[1][0]], [pitchRateValid[1][0]]]
    zero = np.zeros([4,1])
    y = control.lsim(sys, DefElevator, T, U0)
        
    if np.size(sys.B) == 4:
        uCurl, AoA, PitchAngle, PitchRate_curl = GetParametersSim(y)
        AoA = AoA + alphaValid[1][0]
        PitchAngle = PitchAngle #+ pitchValid[1][0]
        # redimension parameters:
        uNum = uCurl
        PitchRate = PitchRate_curl #+ pitchRateValid[1][0]       
    
    ## subtract 1st element from all lists
    
    #validation lists
    plt.figure(1)
    plt.subplot(511)
    plt.plot(T, uNum, label = "Numerical: velocity")
    plt.plot(ValidVelocity[0], ValidVelocity[1], label = "Validation velocity")
    plt.legend()
    
    plt.subplot(512)
    plt.plot(T, AoA, label = "Numerical: AoA")
    plt.plot(ValidAoA[0], ValidAoA[1], label = "Validation: AoA")
    plt.legend()
    
    plt.subplot(513)
    plt.plot(T, (PitchAngle), label = "Numerical: pitch angle")
    plt.plot(ValidPitchAngle[0], (ValidPitchAngle[1]), label = "Validation: pitch angle")
    plt.legend()
    
    plt.subplot(514)
    plt.plot(T, PitchRate, label = "Numerical: pitch rate")
    plt.plot(ValidPitchRate[0], ValidPitchRate[1], label = "Validation: pitch rate")
#    plt.plot(time, pitch_rate, label = "dimensionless pitch rate")
    plt.legend()
    
    plt.subplot(515)
    plt.plot(T, DefElevator, label = "Input Elevator")
    plt.legend()
    
    plt.show()
    
    print("done")
    return True

def SimulateAsymmResponse(sys, DefAileron, DefRudder, ValidRollAngle
                     , ValidRollRate, ValidYawRate):
    #INPUT: SS model and given parameters of type list
    #OUTPUT: validation plots
    
    # make time vector
    T = np.linspace(DefAileron[0][0], DefAileron[0][-1],len(DefAileron[0]))

    # make INPUT vector
    DefAileron0 = DefAileron[1][0]
    DefAileron = np.array(DefAileron[1][:])
    DefAileron = DefAileron - DefAileron0
    
    DefRudder0 = DefRudder[1][0]
    DefRudder = np.array(DefRudder[1][:])
    DefRudder = DefRudder - DefRudder0
    
    U = np.stack((Ua[1],Ur[1]), axis = -1)
    zero = np.zeros([4,1])
    y = control.lsim(sys, U, T, zero)
        
    # yaw: beta; phi: roll, p: roll rate, r: pitch rate
    beta, phi, p, r = GetParametersSim(y)
    phi = phi + ValidRollAngle[1][0]
    p = p #+ ValidRollRate[1][0]
    r = r #+ ValidYawRate[1][0]
    
    
    # plotting
    plt.figure(2)
    plt.subplot(411)
    plt.plot(T, phi, label = "Numerical: Roll Angle")
    plt.plot(ValidRollAngle[0], ValidRollAngle[1], label = "Validation: Roll Angle")
    plt.legend()
    
    plt.subplot(412)
    plt.plot(T, p, label = "Numerical: Roll Rate")
    plt.plot(ValidRollRate[0], ValidRollRate[1], label = "Validation: Roll Rate")
    plt.legend()
    
    plt.subplot(413)
    plt.plot(T, r, label = "Numerical: Yaw Rate")
    plt.plot(ValidYawRate[0], (ValidYawRate[1]), label = "Validation: Yaw Rate")
    plt.legend()
    
    plt.subplot(414)    
    plt.plot(T, DefAileron, label = "Input Aileron")
    plt.plot(T, DefRudder, label = "Input Rudder")
    plt.legend()
    
    plt.show()   
        
    
    ## subtract 1st element from all lists
    
    #validation lists    
    print ("done")
    return True

sys_symm, sys_asymm = InitSS()
SimulateSymmResponse(sys_symm, Ue, uValid, alphaValid, pitchValid, pitchRateValid)
SimulateAsymmResponse(sys_asymm, Ua, Ur, rollValid, rollRateValid, yawRateValid)


