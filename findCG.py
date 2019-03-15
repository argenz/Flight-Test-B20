
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:02:09 2019

@author: biron
"""

from DataReader import *

pplname = get_Data2()[2]
#pplname.insert(0,"nose")
#pplname.insert(1,"aft cabin1")
#pplname.insert(2,"aft cabin2")

mpplist_kg = get_Data2()[1]
#mpplist_kg.insert(0,100)
#mpplist_kg.insert(1,200)
#mpplist_kg.insert(2,200)

mppl_lbs = []
for i in mpplist_kg:
    mppl_lbs.append(i*2.20462)
    


cg_list = [131,131,170,214,214,251,251,288,288]

moment = 0
total_mass = 0
for i in range(len(mppl_lbs)):
    moment += mppl_lbs[i]*cg_list[i] #pounds*inches
    total_mass += mppl_lbs[i]
    
cg = moment/total_mass  #cg location measured from the nose of the plane


#,-*-,coding:,utf-8,-*-
"""
Created on Wed Mar 13,11:39:32 2019

@author: Klaas
"""

fuel_masses = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,3100,3200,3300,3400,3500,3600,3700,3800,3900,4000,4100,4200,4300,4400,4500,4600,4700,4800,4900,5008]

fuel_moments = [298.16,591.18,879.08,1165.42,1448.40,1732.53,2014.80,2298.84,2581.92,2866.30,3150.18,3434.52,3718.52,4003.23,4287.76,4572.24,4856.56,5141.16,5425.64,5709.90,5994.04,6278.47,6562.82,6846.96,7131.00,7415.33,7699.60,7984.34,8269.06,8554.05,8839.04,9124.80,9410.62,9696.97,9983.40,10270.08,10556.84,10843.87,11131.00,11418.20,11705.50,11993.31,12281.18,12569.04,12856.86,13144.73,13432.48,13720.56,14008.46,14320.34]
fuel_moments = [x * 100 for x in fuel_moments]

def fuel_moment(fuel_mass):
    for i in range(len(fuel_masses)):
        if fuel_mass >= fuel_masses[i]:
            i = i+1
        else:
            break
    distance = fuel_mass - fuel_masses[i-1]
    gradient = (fuel_moments[i]-fuel_moments[i-1])/100
    moment = fuel_moments[i-1] + gradient * distance
    
    return moment
    

