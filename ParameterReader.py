# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:46:02 2019

@author: hksam
"""

from scipy import signal
import numpy as np
from Cit_par import *
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












