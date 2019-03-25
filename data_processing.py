# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:15:45 2019

@author: Klaas
"""
from readmat import *
import matplotlib.pyplot as plt

def clock_to_utc(hour, minute, second, millisecond):
    utc_time = (hour-1)*60**2 + minute*60 + second + millisecond*0.001
    return utc_time

def seconds_to_utc(s):
    utc_time = 37856.910821 + s
    return utc_time

def utc_to_normal(utc_time):
    x = utc_time
    hour = 1+int(x/(60**2))
    x = x - 60**2*(hour-1)
    minute = int(x/60)
    x = x - 60*minute
    second = int(x)
    x = x - second
    millisecond = int(1000*x)
    return (hour,minute,second,millisecond)

def find_index(utc_time):
    i = 0
    if utc_time <= UTC_Seconds[0]:
        raise ValueError('utc_time too low in find_index function')
    if utc_time > UTC_Seconds[-1]:
        raise ValueError('utc_time too high in find_index function')
    for x in [10000, 1000, 10, 1]:
        while UTC_Seconds[i] <= utc_time:
            i = i + x
            try:
                UTC_Seconds[i+1]
            except IndexError:
                break
        i = i - x
    return(i)

def make_list(data_list, start_time, end_time):
    y_values = []
    time_values = []
    start_index = find_index(start_time)
    end_index = find_index(end_time)
    
    for i in range(start_index, end_index):
        y_values.append(data_list[i])
        time_values.append(UTC_Seconds[i]-start_time)
        
    return(time_values, y_values)

#phugoid
#plt.figure(1)
#phugoid = make_list(Pressure_Altitude, UTC_Seconds[0] + 2880, UTC_Seconds[0]+3020)
#plt.plot(phugoid[0], phugoid[1])
<<<<<<< HEAD
#
=======
##
>>>>>>> ee55e8a05513f23b34922a4e490a8598ea04d8b7
#plt.figure(2)
#elevator = make_list(Deflection_of_elevator, UTC_Seconds[0] + 2889, UTC_Seconds[0]+2908)
#plt.plot(elevator[0], elevator[1])
#
#plt.figure(3)
#f1 = make_list(Fuel1, UTC_Seconds[0], UTC_Seconds[-1])
#f2 = make_list(Fuel2, UTC_Seconds[0], UTC_Seconds[-1])
#
#plt.plot(f1[0],f1[1])
#plt.plot(f2[0],f2[1])