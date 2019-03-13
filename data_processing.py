# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:15:45 2019

@author: Klaas
"""
from readmat import *
import matplotlib.pyplot as plt

def normal_to_utc(hour, minute, second, millisecond):
    utc_time = (hour-1)*60**2 + minute*60 + second + millisecond*0.001
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
    return[time_values, y_values]

f1 = make_list(Fuel1, UTC_Seconds[0]+4000, UTC_Seconds[-1])
f2 = make_list(Fuel2, UTC_Seconds[0]+4000, UTC_Seconds[-1])

plt.plot(f1[0],f1[1])
plt.plot(f2[0],f2[1])