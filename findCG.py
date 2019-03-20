
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:02:09 2019

@author: biron
"""

from DataReader import *
from data_processing import *

pplname = get_Data2()[2]
#pplname.insert(0,"nose")
#pplname.insert(1,"aft cabin1")
#pplname.insert(2,"aft cabin2")

ppl_weights = [i*9.80665 for i in get_Data2()[1]] # kg
#ppl_weights_kg.insert(0,100)
#ppl_weights_kg.insert(1,200)
#ppl_weights_kg.insert(2,200)
    


cg_normal_inches = [131,131,170,214,214,251,251,288,288]
cg_walk_inches = [131,131,170,214,214,251,251,170,288]
cg_normal = [i * 0.0254 for i in cg_normal_inches] # m
cg_walk = [i * 0.0254 for i in cg_walk_inches] # m

def peeps_mom(cg_config):
    peeps_moment = 0
    for i in range(len(ppl_weights)):
        peeps_moment += ppl_weights[i]*cg_config[i]
      #cg location measured from the nose of the plane
    return peeps_moment
    
#,-*-,coding:,utf-8,-*-
"""
Created on Wed Mar 13,11:39:32 2019

@author: Klaas
"""

fuel_weights_lbs = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900,4000,4100,4200,4300,4400,4500,4600,4700,4800,4900,5008]
fuel_weights = [i*4.44822 for i in fuel_weights_lbs] # N 

fuel_moments_lbin = [298.16,591.18,879.08,1165.42,1448.40,1732.53,2014.80,2298.84,2581.92,2866.30,3150.18,3434.52,3718.52,4003.23,4287.76,4572.24,4856.56,5141.16,5425.64,5709.90,5994.04,6278.47,6562.82,6846.96,7131.00,7415.33,7699.60,7984.34,8269.06,8554.05,8839.04,9124.80,9410.62,9696.97,9983.40,10270.08,10556.84,10843.87,11131.00,11418.20,11705.50,11993.31,12281.18,12569.04,12856.86,13144.73,13432.48,13720.56,14008.46,14320.34]
fuel_moments_lbin = [x * 100 for x in fuel_moments_lbin]
fuel_moments = [i*0.11298 for i in fuel_moments_lbin] # Nm

def fuel_weight(utc_seconds):
    i = find_index(utc_seconds)
    block_fuel = get_Data1()[1]
    mfuel = block_fuel - Fuel1[i] - Fuel2[i]
    return mfuel

def fuel_moment(current_fuel_weight):
    for i in range(len(fuel_weights)):
        if current_fuel_weight >= fuel_weights[i]:
            i = i+1
        else:
            break
    distance = current_fuel_weight - fuel_weights[i-1]
    gradient = (fuel_moments[i]-fuel_moments[i-1])/(fuel_weights[i]-fuel_weights[i-1])
    moment = fuel_moments[i-1] + gradient * distance
    return moment

def cg_time(UTC_sec, cg_config):
    EOW_mom = 2677847.5 * 0.11298
    fuel_mom = fuel_moment(fuel_weight(UTC_sec))
    ppl_mom = peeps_mom(cg_config)
    total_mom = EOW_mom + fuel_mom + ppl_mom
    
    total_weight = 9165*4.44822 + fuel_weight(UTC_sec) + sum(ppl_weights)
    
    return total_mom/total_weight #in meter

