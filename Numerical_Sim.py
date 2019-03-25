# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 21:36:01 2019
@author: hksam
"""

from ParameterReader import cessna
import numpy as np
import scipy.linalg as slin
import matplotlib.pyplot as plt
<<<<<<< HEAD

#rewrite linear system into SS: x_bar_dot = AX + Bu
#def SSmaker(a, b, c):
#    
#    A = np.dot(slin.inv(a),-b)
#    B = np.dot(slin.inv(a),-c)  
#    C = np.array([[1, 0, 0, 0],
#             [0, 1, 0, 0],
#             [0, 0, 1, 0],
#             [0, 0, 0, 1]])
#    D = np.zeros(np.shape(c))
#    print(np.linalg.eig(A))
#    
#    return control.ss(A,B,C,D)

## SYMMETRIC MOTION
=======
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
    
    
    ## ASYMMETRIC MOTION
    C1a = np.matrix([[(CYbdot - 2 *muc) * b/V0, 0, 0, 0],
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
    
    C = np.matrix([[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]])
    
    def SSmaker(a, b, c):
>>>>>>> ee55e8a05513f23b34922a4e490a8598ea04d8b7
    
        A = np.dot(slin.inv(a),b)
        B = np.dot(slin.inv(a),c)
        C = np.matrix([[1., 0, 0, 0],
                 [0, 1., 0, 0],
                 [0, 0, 1., 0],
                 [0, 0, 0, 1.]])
        D = np.zeros(np.shape(c))
        print "eigenvalues:", np.linalg.eig(A)[0]
    
        return control.ss(A,B,C,D)
    
    sys_symm = SSmaker(C1s, -C2s, -C3s)
    sys_asymm = SSmaker(C1a, -C2a, -C3a)
    
    return sys_symm, sys_asymm
    
## State-Space Models:
<<<<<<< HEAD
#    
#sys_symm = SSmaker(C1s,C2s,C3s)
#print sys_symm

# symmetric

def SSmaker2(a, b, c):  
    A = np.dot(slin.inv(a),-b)
    B = np.dot(slin.inv(a),-c)
    return A,B

def reaction_sym(v, alpha, theta, q, uvector, step_size, simtime):
    x = [[u],[alpha],[theta],[q]]
    x_list = []    
    t = 0
    A = SSmaker2(C1s, C2s, C3s)[0]
    B = SSmaker2(C1s, C2s, C3s)[1]
    
    for i in range(0, simtime/stepsize):
        u = u_vector[i]
        xdot = np.dot(A,x) + np.dot(B,u)
        x += xdot*stepsize
        x_list.append(x)
        t = t + stepsize
        x_list.append(x)

=======
    
#sys_symm = SSmaker(C1s, -C2s, -C3s)
#print sys_symm
#sys_asymm = SSmaker(-C1a, C2a, C3a)
>>>>>>> ee55e8a05513f23b34922a4e490a8598ea04d8b7

#y,t = control.step(sys_symm)
##
#plt.plot(t,y)
#

