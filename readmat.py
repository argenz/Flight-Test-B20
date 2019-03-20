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

aoa = [fd[0][i][0] for i in range(len(fd[0]))] #angle of attack

Deflection_elev_trim = [fd[1][i][0] for i in range(len(fd[1]))] #Deflection of elevator trim

Force_elevator_control_wheel = [fd[2][i][0] for i in range(len(fd[2]))] #Force on elevator control wheel

Fuel_mass_flow1 = [fd[3][i][0] for i in range(len(fd[3]))] #Engine 1: Fuel mass flows

Fuel_mass_flow2 = [fd[4][i][0] for i in range(len(fd[4]))] #Engine 2: Fuel mass flow

Inter_Turbine_Temperature1  = [fd[5][i][0] for i in range(len(fd[5]))] #Engine 1: Inter Turbine Temperature (ITT)

Inter_turbine_temperature2  = [fd[6][i][0] for i in range(len(fd[6]))] #Engine 2: Inter turbine temperature (ITT)

Oil_pressure1 = [fd[7][i][0] for i in range(len(fd[7]))] #Engine 1: Oil pressure

Oil_pressure2 = [fd[8][i][0] for i in range(len(fd[8]))] #Engine 2: Oil pressure

Fan_speed1 = [fd[9][i][0] for i in range(len(fd[9]))] #Engine 1: Fan speed (N1)

Turbine_speed1 = [fd[10][i][0] for i in range(len(fd[10]))] #Engine 1: Turbine speed (N2)

Fan_speed2 = [fd[11][i][0] for i in range(len(fd[11]))] #Engine 2: Fan speed (N1)

Turbine_speed2 = [fd[12][i][0] for i in range(len(fd[12]))] #Engine 2: Turbine speed (N2)

Fuel1 = [fd[13][i][0] for i in range(len(fd[13]))]  #Engine 1

Fuel2 = [fd[14][i][0] for i in range(len(fd[14]))]  #Engine 2

Deflection_of_aileron = [fd[15][i][0] for i in range(len(fd[15]))]

Deflection_of_elevator = [fd[16][i][0] for i in range(len(fd[16]))]

Deflection_of_rudder = [fd[17][i][0] for i in range(len(fd[17]))]

#UTC Date DD:MM:YY = [fd[18][i][0] for i in range(len(fd[18]))]

UTC_Seconds = [fd[19][i][0] for i in range(len(fd[19]))]

Roll_Angle = [fd[20][i][0] for i in range(len(fd[20]))]

Pitch_Angle = [fd[21][i][0] for i in range(len(fd[21]))]

#<no description> = [fd[22][i][0] for i in range(len(fd[22]))]

GNSS_Latitude = [fd[23][i][0] for i in range(len(fd[23]))]

GNSS_Longitude = [fd[24][i][0] for i in range(len(fd[24]))]

Body_Roll_Rate = [fd[25][i][0] for i in range(len(fd[25]))]

Body_Pitch_Rate = [fd[26][i][0] for i in range(len(fd[26]))]

Body_Yaw_Rate = [fd[27][i][0] for i in range(len(fd[27]))]

Body_Long_Accel = [fd[28][i][0] for i in range(len(fd[28]))]

Body_Lat_Accel = [fd[29][i][0] for i in range(len(fd[29]))]

Body_Norm_Accel = [fd[30][i][0] for i in range(len(fd[30]))]

Along_Heading_Accel = [fd[31][i][0] for i in range(len(fd[31]))]

Cros_Heading_Accel = [fd[32][i][0] for i in range(len(fd[32]))]

Vertical_Accel = [fd[33][i][0] for i in range(len(fd[33]))]

Static_Air_Temperature = [fd[34][i][0] for i in range(len(fd[34]))]

Total_Air_Temperature = [fd[35][i][0] for i in range(len(fd[35]))]

Pressure_Altitude = [fd[36][i][0] for i in range(len(fd[36]))]          #(1013.25 mB)

Baro_Corrected_Altitude  = [fd[37][i][0] for i in range(len(fd[37]))] 

#<no description> = [fd[38][i][0] for i in range(len(fd[38]))]

Mach = [fd[39][i][0] for i in range(len(fd[39]))]

Computed_Airspeed = [fd[40][i][0] for i in range(len(fd[40]))]

true_Airspeed = [fd[41][i][0] for i in range(len(fd[41]))]

Altitude_Rate = [fd[42][i][0] for i in range(len(fd[42]))]

Measurement_Running = [fd[43][i][0] for i in range(len(fd[43]))]

#Numberof Measurements Ready = []
#Status of graph = []
#Active Screen = []
#T = []
time = np.arange(0,43641,1)

plt.figure()
plt.plot(time, Altitude_Rate)
plt.show()


    
    
