# Citation 550 - Linear simulation

# Stationary flight condition


import numpy as np
from TimeIntervals import short_period, phugoid, dutch_roll, dutch_roll_yd, aper_roll, spiral
from data_processing import make_list
from readmat import Deflection_of_aileron, Deflection_of_elevator, Deflection_of_rudder, Deflection_elev_trim
from readmat import Pitch_Angle, Roll_Angle
from readmat import UTC_Seconds, aoa, true_Airspeed
from readmat import Pressure_Altitude, Body_Pitch_Rate, Body_Roll_Rate, Body_Yaw_Rate
from findCG import GetMass
#from Main import motion
#from Main import 

# Choose Eigenmotion:
#print "1.", "Short Period"
#print "2.", "Phugoid"
#print "3.", "Dutch Roll"
#print "4.", "Dutch Roll with Yaw Damper"
#print "5.", "Aperiodic Roll"
#print "6.", "Spiral"
#    
#running = True
#while running:   
#    motion = int(raw_input("Select number of motion to plot:"))
#    for i in np.arange(1,7,1):
#        if i == motion:
#            running = False
#
#mot = [short_period(), phugoid(), dutch_roll(), dutch_roll_yd(), aper_roll(), spiral()]
tStart, tEnd, ti = short_period()

# Elevator input
Ue = make_list(Deflection_of_elevator, tStart, tEnd)         #(time_values, y_values)
Ua = make_list(Deflection_of_aileron, tStart, tEnd)
Ur = make_list(Deflection_of_rudder, tStart, tEnd)

#validation input
uValid = make_list(true_Airspeed, tStart, tEnd)
height = make_list(Pressure_Altitude, tStart, tEnd)

alphaValid = make_list(aoa, tStart, tEnd)
rollValid = make_list(Roll_Angle, tStart, tEnd)
pitchValid = make_list(Pitch_Angle, tStart, tEnd)
pitchRateValid = make_list(Body_Pitch_Rate, tStart, tEnd)
rollRateValid = make_list(Body_Roll_Rate, tStart, tEnd)
yawRateValid = make_list(Body_Yaw_Rate, tStart, tEnd)

hp0 =  height[1][0]
V0 = uValid[1][0] 
alpha0 =  alphaValid[1][0]
th0 = pitchValid[1][0]

hp0    =       hp0       # pressure altitude in the stationary flight condition [m]
V0     =       V0       # true airspeed in the stationary flight condition [m/sec]
alpha0 =      alpha0       # angle of attack in the stationary flight condition [rad]
th0    =      th0     # pitch angle in the stationary flight condition [rad]

# Aircraft mass
W     =     GetMass(tStart)      #weight in [N]
m = W/9.81
#print m
# aerodynamic properties
e      =     0.9702770390615243       # Oswald factor [ ]
CD0    =     0.021102518946169862       # Zero lift drag coefficient [ ]
CLa    =     5.265521398365575     # Slope of CL-alpha curve []

# Longitudinal stability
Cma    =        -0.5376411647209149    # longitudinal stabilty [ ]
Cmde   =        -1.2693616320721883    # elevator effectiveness [ ]

# Aircraft geometry

S      = 30.00	          # wing area [m^2]
Sh     = 0.2 * S         # stabiliser area [m^2]
Sh_S   = Sh / S	          # [ ]
lh     = 4.23728    # tail length [m] .71 * 5.968
c      = 2.0569	          # mean aerodynamic cord [m]
lh_c   = lh / c	          # [ ]
b      = 15.911	          # wing span [m]
bh     = 5.791	          # stabilser span [m]
A      = b ** 2 / S      # wing aspect ratio [ ]
Ah     = bh ** 2 / Sh    # stabilser aspect ratio [ ]
Vh_V   = 1	          # [ ]
ih     = -2 * np.pi / 180   # stabiliser angle of incidence [rad]

# Constant values concerning atmosphere and gravity

rho0   = 1.2250          # air density at sea level [kg/m^3] 
lmbda = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m^2/sec^2K]
g      = 9.81            # [m/sec^2] (gravity constant)

# air density [kg/m^3]
rho    = rho0 * np.power( ((1+(lmbda * hp0 / Temp0))), (-((g / (lmbda*R)) + 1)))   
W      = m * g            # [N]       (aircraft weight)
#print rho
# Constant values concerning aircraft inertia

muc    = m / (rho * S * c)
mub    = m / (rho * S * b)
KX2    = 0.019
KZ2    = 0.042
KXZ    = 0.002
KY2    = 1.3925          # 1.25 * 1.114

# Aerodynamic constants
Cmac   = 0                      # Moment coefficient about the aerodynamic centre [ ]
CNwa   = CLa                    # Wing normal force slope [ ]
CNha   = 2 * np.pi * Ah / (Ah + 2) # Stabiliser normal force slope [ ]
depsda = 4 / (A + 2)            # Downwash gradient [ ]

# Lift and drag coefficient

CL = 2 * W / (rho * V0 ** 2 * S)              # Lift coefficient [ ]
CD = CD0 + (CLa * alpha0) ** 2 / (np.pi * A * e) # Drag coefficient [ ]

# Stabiblity derivatives

CX0    = W * np.sin(th0) / (0.5 * rho * V0 ** 2 * S)
CXu    = -0.02792
CXa    = -0.47966
CXadot = +0.08330
CXq    = -0.28170
CXde   = -0.03728

CZ0    = -W * np.cos(th0) / (0.5 * rho * V0 ** 2 * S)
CZu    = -0.37616
CZa    = -6.74340
CZadot = -0.00350
CZq    = -5.66290
CZde   = -0.69612

Cmu    = +0.06990
Cmadot = +0.17800
Cmq    = -8.79415

CYb    = -0.7500
CYbdot =  0     
CYp    = -0.0304
CYr    = +0.8495
CYda   = -0.0400
CYdr   = +0.2300

Clb    = -0.10260
Clp    = -0.71085
Clr    = +0.23760
Clda   = -0.23088
Cldr   = +0.03440

Cnb    =  +0.1348
Cnbdot =   0     
Cnp    =  -0.0602
Cnr    =  -0.2061
Cnda   =  -0.0120
Cndr   =  -0.0939


