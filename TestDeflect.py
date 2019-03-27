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

    # make INPUT vector
    DefElevator0 = DefElevator[1][0]
    DefElevator = np.array(DefElevator[1][:])
    DefElevator = DefElevator - DefElevator0
    DefElevator = [i * 1 for i in DefElevator]
    zero = np.zeros([4,1])
    
    y = control.lsim(sys, DefElevator, T, zero)
        
    if np.size(sys.B) == 4:
        uCurl, AoA, PitchAngle, PitchRate_curl = GetParametersSim(y)
        AoA = AoA + ValidAoA[1][0]
        PitchAngle = PitchAngle + ValidPitchAngle[1][0]
        # redimension parameters:
        uNum = uCurl + ValidVelocity[1][0]
        PitchRate = PitchRate_curl + pitchRateValid[1][0]       
    
    ## subtract 1st element from all lists
    

    DefElevator = [i * 1 for i in DefElevator]
    DefElevator = DefElevator + DefElevator0
    
    #plotting
    legendloc = 2
    validstyle = '--'
    plt.figure(1)
    plt.rcParams.update({'font.size': 15})

    plt.subplot(511)
    plt.title("Phugoid")
    plt.plot(T, uNum, label = "Numerical")
    plt.plot(ValidVelocity[0], ValidVelocity[1], label = "Flight Data", linestyle = validstyle)
    plt.gca().set_ylabel('u [m/s]')        
    plt.legend(loc = legendloc)

#    plt.ylabel("$V [m/s]$")
    
    plt.subplot(512)
    plt.plot(T, AoA, label = "Numerical")
    plt.plot(ValidAoA[0], ValidAoA[1], label = "Flight Data", linestyle = validstyle)
    plt.gca().set_ylabel(r'$\alpha$ [rad]')        
    plt.legend(loc = legendloc)
    
    plt.subplot(513)
    plt.plot(T, (PitchAngle), label = "Numerical")
    plt.plot(ValidPitchAngle[0], (ValidPitchAngle[1]), label = "Flight Data", linestyle = validstyle)
    plt.gca().set_ylabel(r'$\theta$ [rad/s]')
    plt.legend(loc = legendloc)

    
    plt.subplot(514)
    plt.plot(T, PitchRate, label = "Numerical")
    plt.plot(ValidPitchRate[0], ValidPitchRate[1], label = "Flight Data", linestyle = validstyle)
    plt.gca().set_ylabel('q [rad/s]')        
    plt.legend(loc = legendloc)

    
    plt.subplot(515)
    plt.plot(T, DefElevator, label = "Input Elevator")
    plt.gca().set_ylabel(r'$\delta_{e}$ [rad]')
    plt.gca().set_xlabel('time [s]')
    plt.legend(loc = legendloc)

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
    DefRudder0 = DefRudder[1][0]
    
    DefAileron = DefAileron[1][:] - DefAileron[1][0]
#    DefAileron = [-1*i for i in DefAileron]

    DefRudder = DefRudder[1][:] - DefRudder[1][0]
#    DefRudder = [-1*i for i in DefRudder]
    
    U = np.stack((DefAileron,DefRudder), axis = -1)
    zero = np.zeros([4,1])
    y = control.lsim(sys, U, T, zero)
        
    # yaw: beta; phi: roll, p: roll rate, r: pitch rate
    beta, phi, p, r = GetParametersSim(y)
    phi = phi + ValidRollAngle[1][0]
    p = p + ValidRollRate[1][0]
    r = r + ValidYawRate[1][0]
    
    DefRudder = DefRudder + DefRudder0
    DefAileron = DefAileron + DefAileron0
    # plotting
    legendloc = 3
    plt.figure(2)
    validstyle = '--'
    plt.rcParams.update({'font.size': 15}) 
    
    plt.subplot(411)
    plt.title("Spiral")
    plt.plot(T, phi, label = "Numerical")
    plt.plot(ValidRollAngle[0], ValidRollAngle[1], label = "Flight Data", linestyle = validstyle)
    plt.gca().set_ylabel(r'$\phi$ [rad]')        
    plt.legend(loc = legendloc)
    plt.legend()
    
    plt.subplot(412)
    plt.plot(T, p, label = "Numerical")
    plt.plot(ValidRollRate[0], ValidRollRate[1], label = "Flight Data", linestyle = validstyle)
    plt.gca().set_ylabel('p [rad/s]')      
    plt.legend(loc = legendloc)
    plt.legend()
    
    plt.subplot(413)
    plt.plot(T, r, label = "Numerical")
    plt.plot(ValidYawRate[0], (ValidYawRate[1]), label = "Flight Data", linestyle = validstyle)
    plt.gca().set_ylabel('r [rad/s]')        
    plt.legend(loc = legendloc)
    plt.legend()
    
    plt.subplot(414)    
    plt.plot(T, DefAileron, label = r"Input Aileron $\delta_{a}$")
    plt.plot(T, DefRudder, label = r"Input Rudder $\delta_{r}$", linestyle = validstyle)
    plt.gca().set_ylabel(r'$\delta$ [rad]')    
    plt.gca().set_xlabel('time [s]')    
    plt.legend(loc = legendloc)
    plt.legend()
    
    plt.show()   
           
    print ("done")
    return True
#
sys_symm, sys_asymm = InitSS()
SimulateSymmResponse(sys_symm, Ue, uValid, alphaValid, pitchValid, pitchRateValid)
#SimulateAsymmResponse(sys_asymm, Ua, Ur, rollValid, rollRateValid, yawRateValid)


