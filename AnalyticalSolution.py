#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:22:27 2019

@author: FCRA
"""

#ANALYTICAL MODEL
from Cit_par import *
from math import *

#Symmetric Motion
#shortperiod

As = 4*muc**2*KY2
Bs = -2*muc*(KY2*CZa+Cmadot+Cmq)
Cs = CZa*Cmq-2*muc*Cma 

eig_shortperiod1_real = (-Bs/(2*As)) 
eig_shortperiod1_complex = sqrt(abs(Bs**2-4*As*Cs))/(2*As)
eig_shortperiod2_real = (-Bs/(2*As))
eig_shortperiod2_complex = -sqrt(abs(Bs**2-4*As*Cs))/(2*As)

#phugoid
Ap = 2*muc*(CZa*Cmq-2*muc*Cma)
Bp = 2*muc*(CXu*Cma-Cmu*CXa)+Cmq*(CZu*CZa-CXu*CZa)
Cp = CZ0*(Cmu*CZa - CZu*Cma)

eig_phugoid1_real = (-Bp/(2*Ap))
eig_phugoid1_complex = +sqrt(abs(Bp**2-4*Ap*Cp))/(2*Ap)
eig_phugoid2_real = (-Bp/(2*Ap))
eig_phugoid2_complex = -sqrt(abs(Bp**2-4*Ap*Cp))/(2*Ap)

#Assymmetric Motion
#aperiodic roll
eig_aperiodicroll = Clp/(4*muc*KX2)

#Dutch Roll
Adr = 8*mub**2*KZ2
Bdr = -2*mub*(Cnr+2*KZ2*CYb)
Cdr = 4*mub*Cnb + CYb*Cnr

eig_droll1_real = (-Bdr/(2*Adr))
eig_droll1_complex = +sqrt(abs(Bdr**2-4*Adr*Cdr))/(2*Adr)
eig_droll2_real = (-Bdr/(2*Adr))
eig_droll2_complex = -sqrt(abs(Bdr**2-4*Adr*Cdr))/(2*Adr)

#spiral 
eig_spiral = 2*CL*(Clb*Cnr-Cnb*Clr)/(Clp*(CYb*Cnr+ 4*mub*Cnb)-Cnp*(CYb*Clr+4*mub*Clb))

print "Eigenvalue 1 Short Period", eig_shortperiod1_real,"+",eig_shortperiod1_complex, "j"
print "Eigenvalue 2 Short Period", eig_shortperiod2_real,"+",eig_shortperiod2_complex, "j"
print "Eigenvalue 1 Phugoid", eig_phugoid1_real,"+",eig_phugoid1_complex, "j"
print "Eigenvalue 2 Phugoid", eig_phugoid2_real,"+",eig_phugoid2_complex, "j"
print "Eigenvalue Aperiodic Roll", eig_aperiodicroll
print "Eigenvalue 1 Dutch Roll", eig_droll1_real,"+",eig_droll1_complex, "j"
print "Eigenvalue 2 Dutch Roll", eig_droll2_real,"+",eig_droll2_complex, "j"
print "Eigenvalue Spiral", eig_spiral
#print "Eivenvalue

#print "Eigenvalues Phugoid", eig_phugoid1, eig_phugoid2
#print "Eigenvalues Aperiodic Roll", eig_aperiodicroll
#print "Eigenvalues Dutch Roll", eig_droll1, eig_droll2
#print "Eigenvalues Spiral", eig_spiral 

