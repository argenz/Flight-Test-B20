import numpy as np
import h5py
import scipy.io as sio
import matplotlib.pyplot as plt

matcon = sio.loadmat('FTISxprt-20190315_102511.mat')
data = matcon["flightdata"]



    

#fd is list containing the matrix with the data 
    
fd = []   
    
for i in range(len(data[0][0])):
    numbers = data[0][0][i][0][0][0]
    #title = data[0][0][i][0][0][2][0][0][0]
    #fd.append(title)
    fd.append(numbers)
    

#every variable list with their data

aoa = [fd[0][i][0]*0.0174532925 for i in range(len(fd[0]))]#angle of attack #DEG --> rad
   
Deflection_elev_trim = [fd[1][i][0]*0.0174532925 for i in range(len(fd[1]))] #Deflection of elevator trim   #DEG --> rad

Force_elevator_control_wheel = [fd[2][i][0] for i in range(len(fd[2]))] #Force on elevator control wheel  #N

Fuel_mass_flow1 = [fd[3][i][0]*0.000125997881 for i in range(len(fd[3]))] #Engine 1: Fuel mass flows    #lbs/hr --> kg/s

Fuel_mass_flow2 = [fd[4][i][0]*0.000125997881 for i in range(len(fd[4]))] #Engine 2: Fuel mass flow    #lbs/hr --> kg/s

#Inter_Turbine_Temperature1  = [fd[5][i][0] for i in range(len(fd[5]))] #Engine 1: Inter Turbine Temperature (ITT)   #C
#
#Inter_turbine_temperature2  = [fd[6][i][0] for i in range(len(fd[6]))] #Engine 2: Inter turbine temperature (ITT)  #C

#Oil_pressure1 = [fd[7][i][0] for i in range(len(fd[7]))] #Engine 1: Oil pressure    #psi
#
#Oil_pressure2 = [fd[8][i][0] for i in range(len(fd[8]))] #Engine 2: Oil pressure    #psi

Deflection_of_Control_Column = [fd[9][i][0]*0.0174532925 for i in range(len(fd[10]))] #Stick Deflection    #deg --> rad

#Fan_speed1 = [fd[10][i][0] for i in range(len(fd[9]))] #Engine 1: Fan speed (N1)         #%
#
#Turbine_speed1 = [fd[11][i][0] for i in range(len(fd[10]))] #Engine 1: Turbine speed (N2)  #%
#
#Fan_speed2 = [fd[12][i][0] for i in range(len(fd[11]))] #Engine 2: Fan speed (N1)     #%
#
#Turbine_speed2 = [fd[13][i][0] for i in range(len(fd[12]))] #Engine 2: Turbine speed (N2)  #%

Fuel1 = [fd[14][i][0]*0.45359237 for i in range(len(fd[13]))]  #Engine 1         #lbs --> kg

Fuel2 = [fd[15][i][0]*0.45359237 for i in range(len(fd[14]))]  #Engine 2         #lbs --> kg

Deflection_of_aileron = [fd[16][i][0]*0.0174532925 for i in range(len(fd[15]))]   #deg --> rad

Deflection_of_elevator = [fd[17][i][0]*0.0174532925 for i in range(len(fd[16]))]  #deg --> rad

Deflection_of_rudder = [fd[18][i][0]*0.0174532925 for i in range(len(fd[17]))]    #deg --> rad

#UTC Date DD:MM:YY = [fd[19][i][0] for i in range(len(fd[18]))]

UTC_Seconds = [fd[20][i][0] for i in range(len(fd[19]))]                #sec

Roll_Angle = [fd[21][i][0]*0.0174532925 for i in range(len(fd[20]))]                 #deg -->rad

Pitch_Angle = [fd[22][i][0]*0.0174532925 for i in range(len(fd[21]))]                #deg --> rad

#<no description> = [fd[23][i][0] for i in range(len(fd[22]))]

GNSS_Latitude = [fd[24][i][0]*0.0174532925 for i in range(len(fd[23]))]              #deg --> rad

GNSS_Longitude = [fd[25][i][0]*0.0174532925 for i in range(len(fd[24]))]            #deg --> rad

Body_Roll_Rate = [fd[26][i][0]*0.0174532925 for i in range(len(fd[25]))]            #deg/s --> rad/s

Body_Pitch_Rate = [fd[27][i][0]*0.0174532925 for i in range(len(fd[26]))]           #deg/s --> rad/s

Body_Yaw_Rate = [fd[28][i][0]*0.0174532925 for i in range(len(fd[27]))]              #deg/s --> rad/s

#Body_Long_Accel = [fd[29][i][0] for i in range(len(fd[28]))]            #g
#
#Body_Lat_Accel = [fd[30][i][0] for i in range(len(fd[29]))]             #g
#
#Body_Norm_Accel = [fd[31][i][0] for i in range(len(fd[30]))]            #g
#
#Along_Heading_Accel = [fd[32][i][0] for i in range(len(fd[31]))]        #g
#
#Cros_Heading_Accel = [fd[33][i][0] for i in range(len(fd[32]))]        #g
#
#Vertical_Accel = [fd[34][i][0] for i in range(len(fd[33]))]        #g

Static_Air_Temperature = [fd[35][i][0]+274.15 for i in range(len(fd[3]))] #C --> kelvin

Total_Air_Temperature = [fd[36][i][0]+274.15 for i in range(len(fd[35]))] #C --> kelvin

Pressure_Altitude = [fd[37][i][0]*0.3048 for i in range(len(fd[36]))]        #  (1013.25 mB)  #ft --> m

#Baro_Corrected_Altitude  = [fd[38][i][0] for i in range(len(fd[37]))]  #ft

#<no description> = [fd[39][i][0] for i in range(len(fd[38]))]

Mach = [fd[40][i][0] for i in range(len(fd[39]))]

Computed_Airspeed = [fd[41][i][0]*0.514444444 for i in range(len(fd[40]))]   #kts --> m/s

true_Airspeed = [fd[42][i][0]*0.514444444 for i in range(len(fd[41]))]    #kts --> m/s

#Altitude_Rate = [fd[43][i][0] for i in range(len(fd[42]))]   #ft/min
#
#Measurement_Running = [fd[44][i][0] for i in range(len(fd[43]))]  #

#Numberof Measurements Ready = []
#Status of graph = []
#Active Screen = []
#T = []


    
