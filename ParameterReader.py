# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:46:02 2019

@author: hksam
"""

from scipy import signal
import numpy as np
from Cit_par import *

Tl = [1879.17, 1930.19, 1972.48, 2016.4, 1844.79, 1838.59, 1804.57]	
Tr = [2052.36, 2106.61, 2144.6, 2197.46, 2014.83, 2006.7, 1961.74]

def OpenThrustFile(file):
#   Description: needed function to convert the .txt/.DAT file into useable format
#   INPUT: thrust file, e.g. "thrust.DAT"
#   OUTPUT: thrust in type array of column size 2; left engine (0)
#           right engine (1)
    param_file = open(str(file), "r")
    
    lines = []
    # read line-by-line, split comments
    for line in param_file:
        lines.append(line)
    
    #column 0: LEFT engine thrust; column 1: RIGHT engine thrust
    ThrustLst = np.zeros([len(lines),2], dtype = float)
    
    for i, line in enumerate(lines):
        
        thrusti= line.split('\t')
        
        ThrustLst[i,0] = thrusti[0]
        ThrustLst[i,1] = thrusti[1]
    
    return ThrustLst

class ISAProperties(object):
    # Properties:
    # - values at h = 0
    # func returning values: rho, T @ given h
    def __init__(self, rho0, lmbda, temp0, R, G):
        self.rho0 = rho0
        self.lmbda = lmbda
        self.temp0 = temp0
        self.R = R
        self.g = G
    def ISA_rho(self, h):

    
        HBase = [0, 11000, 20000, 32000, 47000, 51000, 71000, 84852]
        HTop = HBase[1:]+[100000]
        T0 = [288.15, 216.5, 216.5, 228.5, 270.5, 270.5, 214.5 ,186.8 ,-86.2+273.15]
        rho0 = [1.225, 0.36392, 0.08803, 0.01322, 0.00142, 0.00086, 0.00006,0]
    #    P0 = [101325, 22632, 5474.9, 868.02, 110.91, 66.939, 3.9564, 0.3734]
        a = [-0.0065, 0, 1.0, 0.0028, 0, 0.0028, -0.002, 0]
        
        i = 0 
        
        while h>HTop[i]:
            i = i+1
            
#    print "layer ", i
        
        
        if i==1 or i==4 or i==7:
            T = T0[i]
    #        P = P0[i]*(np.e**(-9.80665 / (287*T)*(h - HBase[i])))
            rho = rho0[i]*(np.e**(-9.80665 / (287*T)*(h - HBase[i])))
            
        else:
            T = T0[i] + a[i]*h
    #        P = P0[i]*(T/T0[i])**(-9.80665/(a[i]*287))
            rho = rho0[i]*(T/T0[i])**(-9.80665/(a[i]*287)-1)
            
#    print"Density =", rho,"kg/m^3    - OR -    ", rho*0.062427961,"lb/cu ft"
#    print"Pressure =", float(P),"Pa    - OR -    ", float(P)*0.0001450777202,"psi"
#    print"Temperature =", T,"K    - OR -    ", T-273.25, "°C"   

        return rho, T

class Aircraft(object):
    
    def __init__(self):
        self.StatFlightCond = None
        self.LongStab = None
        self.AeroProp = None
        self.Geometry = None
        self.Inertia = None
        self.StabDeriv = None

class StatFlightCond(object):
    
    def __init__(self, hp0, V0, alpha0, th0):
        self.hp0 = hp0
        self.V0 = V0
        self.alpha0 = alpha0
        self.th0 = th0

class LongStab(object):
    def __init__(self, Cma, Cmde):
        self.Cma = Cma
        self.Cmde = Cmde
        
class AeroProp(object):
    
    def __init__(self, e, CD0, CLa, Cmac, Ah, A, W, rho, V0, S, alpha0):
        self.e = e
        self.CD0 = CD0
        self.CLa = CLa
        # Aerodynamic constants
        
        self.Cmac   = Cmac                      # Moment coefficient about the aerodynamic centre [ ]
        self.CNwa   = CLa                    # Wing normal force slope [ ]
        self.CNha   = 2 * np.pi * Ah / (Ah + 2) # Stabiliser normal force slope [ ]
        self.depsda = 4 / (A + 2)            # Downwash gradient [ ]
    
        # Lift and drag coefficient
        
        self.CL = 2 * W / (rho * V0 ** 2 * S)              # Lift coefficient [ ]
        self.CD = CD0 + (CLa * alpha0) ** 2 / (np.pi * A * e) # Drag coefficient [ ]
class geometry(object):
    
    def __init__(self, S, lh, c, b, bh, Vh_V, ih ):
        self.S = S
        self.Sh = 0.2 * S
        self.Sh_S = self.Sh/self.S
        self.lh = lh
        self.c = c
        self.lh_c = lh / c
        self.b = b
        self.bh = bh
        self.A = b ** 2 / S
        self.Ah = bh ** 2 / self.Sh
        self.Vh_V = 1
        self.ih = -2 * np.pi / 180

class inertia(object):
    
    def __init__(self, m, rho, S, c, b, KX2, KZ2, KXZ, KY2):
        self.muc = m / (rho * S * c)
        self.mub = m / (rho * S * b)
        self.KX2    = KX2
        self.KZ2    = KZ2
        self.KXZ    = KXZ
        self.KY2    = KY2

class StabDeriv(object):
#    
    def __init__(self, W, th0, rho, V0, S, CXu, CXa, CXadot, CXq, CXde, CZ0, CZu, 
                 CZa, CZadot, CZq, CZde, Cmu, Cmadot, Cmq, CYb, CYbdot, CYp, CYr, 
                 CYda, CYdr, Clb, Clp, Clr, Clda, Cldr, Cnb, Cnbdot, Cnp, Cnr, Cnda, Cndr):
        
        self.CX0    = W * np.sin(th0) / (0.5 * rho * V0 ** 2 * S)
        self.CXu    = CXu
        self.CXa    = CXa
        self.CXadot = CXadot
        self.CXq    = CXq
        self.CXde   = CXde
        
        self.CZ0    = -W * np.cos(th0) / (0.5 * rho * V0 ** 2 * S)
        self.CZu    = CZu
        self.CZa    = CZa
        self.CZadot = CZadot
        self.CZq    = CZq
        self.CZde   = CZde
        
        self.Cmu    = Cmu
        self.Cmadot = Cmadot
        self.Cmq    = Cmq
        
        self.CYb    = CYb
        self.CYbdot = CYbdot
        self.CYp    = CYp
        self.CYr    = CYr
        self.CYda   = CYda
        self.CYdr   = CYdr
        
        self.Clb    = Clb
        self.Clp    = Clp
        self.Clr    = Clr
        self.Clda   = Clda
        self.Cldr   = Cldr
        
        self.Cnb    =  Cnb
        self.Cnbdot =  Cnbdot    
        self.Cnp    =  Cnp
        self.Cnr    =  Cnr
        self.Cnda   =  Cnda
        self.Cndr   =  Cndr       
        
cessna = Aircraft()
cessnaStatFlightCond = StatFlightCond(hp0, V0, alpha0, th0)
cessnaLongStab = LongStab(Cma, Cmde)
cessnaAeroProp = AeroProp(e, CD0, CLa, Cmac, Ah, A, W, rho, V0, S, alpha0)
cessnaGeometry = geometry(S, lh, c, b, bh, Vh_V, ih)
cessnaInertia = inertia(m, rho, S, c, b, KX2, KZ2, KXZ, KY2)
cessnaStabDeriv = StabDeriv(W, th0, rho, V0, S, CXu, CXa, CXadot, CXq, CXde, CZ0, CZu, 
                 CZa, CZadot, CZq, CZde, Cmu, Cmadot, Cmq, CYb, CYbdot, CYp, CYr, 
                 CYda, CYdr, Clb, Clp, Clr, Clda, Cldr, Cnb, Cnbdot, Cnp, Cnr, Cnda, Cndr)

cessna.StatFlightCond = (cessnaStatFlightCond)
cessna.LongStab = (cessnaLongStab)
cessna.AeroProp = (cessnaAeroProp)
cessna.Geometry = (cessnaGeometry)
cessna.Inertia = (cessnaInertia)
cessna.StabDeriv = (cessnaStabDeriv)




ISAmodule = ISAProperties(rho0, lmbda, Temp0, R, g)












