# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:36:01 2019
@author: hksam
"""

from ParameterReader import cessna
import numpy as np
import scipy.linalg as slin
import matplotlib.pyplot as plt
import control.matlab as control
from Cit_par import *

#rewrite linear system into SS: x_bar_dot = AX + Bu


## SYMMETRIC MOTION

    #C1 x_bar_dot + C2 x_bar + C3 u_bar = 0
def InitSS():
    C1s = np.matrix([[-2 *muc * c/V0/V0, 0, 0, 0],
                   [0, (CZadot-2*muc)*c/V0, 0, 0],
                   [0, 0, -c/V0, 0],
                   [0, Cmadot * c/V0, 0,
                    -2* muc* KY2*c/V0*c/V0]])
        
    C2s = np.matrix([[CXu/V0, CXa, CZ0, CXq*c/V0],
                  [CZu/V0, CZa, -CX0, c/V0*(CZq + 2*muc)],
                   [0, 0, 0, c/V0],
                   [Cmu/V0, Cma, 0, Cmq*c/V0]])
            
    C3s = np.matrix([[-CXde], [-CZde],[ 0], [-Cmde]])
    
    As = np.dot(slin.inv(C1s), -C2s)
    print "As:", np.linalg.eig(As)[0]
    Bs = np.dot(slin.inv(C1s), C3s)
    Cs = np.matrix([[1/V0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, c/V0]])
    Ds = np.zeros(np.shape(C3s))
    
    ## ASYMMETRIC MOTION
    C1a = np.matrix([[(CYbdot - 2 *mub) * b/V0, 0, 0, 0],
                   [0, -.5*b/V0, 0, 0],
                   [0, 0, -4*mub * KX2 * b/V0* b/(2*V0),
                    4*mub * KXZ * b/V0* b/(2*V0)],
                   [Cnbdot * b/V0, 0,
                    4*mub * KXZ * b/V0* b/(2*V0),
                    -4* mub* KZ2*b/V0* b/(2*V0)]])
    
    C2a = np.matrix([[CYb, CL, CYp* b/(2*V0),
                   (CYr - 4 * mub)* b/(2*V0)],
                   [0, 0, b/(2*V0), 0],
                   [Clb, 0, Clp* b/(2*V0),
                   Clr* b/(2*V0)],
                   [Cnb, 0, Cnp* b/(2*V0), Cnr* b/(2*V0)]])
    
    C3a = np.matrix([[-CYda, -CYdr], 
                    [0,0], 
                    [-Clda, -Cldr], 
                    [-Cnda, -Cndr]])
    
    Aa = np.dot(slin.inv(C1a), -C2a)
    print "Aa", np.linalg.eig(Aa)[0]
    Ba = np.dot(slin.inv(C1a), -C3a)
    
    Ca = np.matrix([[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, b/(2*V0), 0],
             [0, 0, 0, b/(2*V0)]])   
    Da = np.zeros(np.shape(C3a))
#    def SSmaker(a, b, c):
#    
#        A = np.dot(slin.inv(a),b)
#        B = np.dot(slin.inv(a),c)
#        C = np.matrix([[1., 0, 0, 0],
#                 [0, 1., 0, 0],
#                 [0, 0, 1., 0],
#                 [0, 0, 0, 1.]])
#        D = np.zeros(np.shape(c))
#        print "eigenvalues:", np.linalg.eig(A)[0]
#    
#        return control.ss(A,B,C,D)
    
    sys_symm = control.ss(As,Bs,Cs,Ds)
    sys_asymm = control.ss(Aa, Ba, Ca, Da)
    
    return sys_symm, sys_asymm
    
#InitSS()