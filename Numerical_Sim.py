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

#rewrite linear system into SS: x_bar_dot = AX + Bu
def SSmaker(a, b, c):
    
    A = np.dot(slin.inv(a),-b)
    B = np.dot(slin.inv(a),-c)  
    C = np.array([[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]])
    D = np.zeros(np.shape(c))
    print np.linalg.eig(A)
    
    return control.ss(A,B,C,D)

## SYMMETRIC MOTION
    
    #C1 x_bar_dot + C2 x_bar + C3 u_bar = 0
C1s = np.array([[2 *cessna.Inertia.muc * cessna.Geometry.c/cessna.StatFlightCond.V0, 0, 0, 0],
               [0, -(cessna.StabDeriv.CZa-2*cessna.Inertia.muc)*cessna.Geometry.c/cessna.StatFlightCond.V0, 0, 0],
               [0, 0, cessna.Geometry.c/cessna.StatFlightCond.V0, 0],
               [0, -cessna.StabDeriv.Cmadot * cessna.Geometry.c/cessna.StatFlightCond.V0, 0,
                2* cessna.Inertia.muc* cessna.Inertia.KY2*cessna.Geometry.c/cessna.StatFlightCond.V0]])
    
C2s = np.array([[cessna.StabDeriv.CXu, cessna.StabDeriv.CXa, cessna.StabDeriv.CZ0,
               cessna.StabDeriv.CXq],
              [cessna.StabDeriv.CZu, cessna.StabDeriv.CZa, -cessna.StabDeriv.CX0,
               cessna.StabDeriv.CZq + 2*cessna.Inertia.muc],
               [0, 0, 0, 1],
               [cessna.StabDeriv.Cmu, cessna.LongStab.Cma, 0, cessna.StabDeriv.Cmq]])
    
C3s = np.array([[cessna.StabDeriv.CXde], [cessna.StabDeriv.CZde], [0], [cessna.LongStab.Cmde]])


## ASYMMETRIC MOTION
C1a = np.array([[-(cessna.StabDeriv.CYbdot + 2 *cessna.Inertia.muc) * cessna.Geometry.b/cessna.StatFlightCond.V0, 0, 0, 0],
               [0, .5*cessna.Geometry.b/cessna.StatFlightCond.V0, 0, 0],
               [0, 0, 4*cessna.Inertia.mub * cessna.Inertia.KX2 * cessna.Geometry.b/cessna.StatFlightCond.V0,
                -4*cessna.Inertia.mub * cessna.Inertia.KXZ * cessna.Geometry.b/cessna.StatFlightCond.V0],
               [-cessna.StabDeriv.Cnbdot * cessna.Geometry.c/cessna.StatFlightCond.V0, 0,
                -4*cessna.Inertia.mub * cessna.Inertia.KXZ * cessna.Geometry.b/cessna.StatFlightCond.V0,
                4* cessna.Inertia.muc* cessna.Inertia.KZ2*cessna.Geometry.c/cessna.StatFlightCond.V0]])

C2a = np.array([[cessna.StabDeriv.CYb, cessna.AeroProp.CL, cessna.StabDeriv.CYp,
               cessna.StabDeriv.CYr - 4 * cessna.Inertia.mub],
               [0, 0, 1, 0],
               [cessna.StabDeriv.Clb, 0, cessna.StabDeriv.Clp,
               cessna.StabDeriv.Clr],
               [cessna.StabDeriv.Cnb, 0, cessna.StabDeriv.Cnp, cessna.StabDeriv.Cnr]])

C3a = np.array([[-cessna.StabDeriv.CYda, -cessna.StabDeriv.CYdr], 
                [0,0], 
                [-cessna.StabDeriv.Clda, -cessna.StabDeriv.Cldr], 
                [-cessna.StabDeriv.Cnda, -cessna.StabDeriv.Cndr]])
    
## State-Space Models:
    
sys_symm = SSmaker(C1s,C2s,C3s)
print sys_symm
sys_asymm = SSmaker(C1a, C2a, C3a)



eigenval = np.linalg.eig()
#y,t = control.step(sys_symm)
##
#plt.plot(t,y)
#



