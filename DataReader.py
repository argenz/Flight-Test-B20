2#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:15:50 2019

@author: FCRA
"""

from math import *
import numpy as np
#from control.matlab import *
#import scipy.linalg as la
import xlrd 


loc = ("Post_Flight_Datasheet_15_03_V2.xlsx") 
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
#print sheet.cell_value(0, 0) 


def get_Data1():
    
    mppl = 0
    for i in range(16):
        if i>6:
            mppl = mppl + sheet.cell_value(i,7)
    
    mfuel = sheet.cell_value(17, 3)*0.453592  #lbs--->kg
    
    
    time = []         #time elapsed  @ each measurement [s]
    hp = []           #??? [m]
    IAS = []          #Calibrated Airspeed [m/s]
    alpha = []        #Angle of attack [rad]         
    F_fl = []         #??   [kg/s]
    F_fr = []         #??   [kg/s]
    F_used = []       #??   [kg/s]
    TAT = []          #C
    
    for i in range(33):
        if i > 26:
            a = sheet.cell_value(i, 1).replace(':',' ')
            b = float(a[0:2])*60 + float(a[3:5])
            time.append(b)
            #
            h = float(sheet.cell_value(i, 3))*0.3048     #ft-->m
            hp.append(h)
            #
            v = float(sheet.cell_value(i, 4))*0.514444    #kts-->m/s
            IAS.append(v)
            #
            aoa = float(sheet.cell_value(i, 5))*pi/180   #deg-->rad
            alpha.append(aoa)
            #
            ffl = float(sheet.cell_value(i, 6))*0.000125998   #lbs/hr --> kg/s
            F_fl.append(ffl)
            #
            ffr = float(sheet.cell_value(i, 7))*0.000125998  #lbs/hr --> kg/s
            F_fr.append(ffr)
            #
            f_used = float(sheet.cell_value(i, 8))*0.453592  #lbs --> kg
            F_used.append(f_used)
            #
            temp = float(sheet.cell_value(i, 9))+273.15    #C --> K
            TAT.append(temp)
    return mppl, mfuel, time, hp, IAS, alpha, F_fl, F_fr, F_used, TAT

#FIRST MEASUREMENT SET 
    
mppl = get_Data1()[0]
mfuel = get_Data1()[1]
time = get_Data1()[2]
hp = get_Data1()[3]
IAS = get_Data1()[4]
alpha = get_Data1()[5]
F_fl = get_Data1()[6]
F_fr = get_Data1()[7]
F_used = get_Data1()[8]
TAT = get_Data1()[9]
            

def get_Data2():
    
    mppl = 0
    mpplist = []
    pplname = []
    for i in range(16):
        if i>6:
            mppl = mppl + sheet.cell_value(i,7)
            mpplist.append(sheet.cell_value(i,7))
            pplname.append(sheet.cell_value(i,0))
            
    mfuel = sheet.cell_value(17, 3)*0.453592  #lbs--->kg
    
    time = []         #time elapsed  @ each measurement [s]
    hp = []           #??? [m]
    IAS = []          #Calibrated Airspeed [m/s]
    alpha = []        #Angle of attack [rad]
    delta_e = []      #elevator deflection angle [rad]
    delta_tr = []     #trim?   [rad]                       -->    DONT KNOWWWWWWW
    F_e = []          #Force on elevator [N] 
    F_fl = []         #??   [kg/s]
    F_fr = []         #??   [kg/s]
    F_used = []       #??   [kg/s]
    TAT = []          #C
    
    for i in range(65):
        if i > 57:
            a = sheet.cell_value(i, 1).replace(':',' ')
            b = float(a[0:2])*60 + float(a[3:5])
            time.append(b)
            #
            h = float(sheet.cell_value(i, 3))*0.3048     #ft-->m
            hp.append(h)
            #
            v = float(sheet.cell_value(i, 4))*0.514444    #kts-->m/s
            IAS.append(v)
            #
            aoa = float(sheet.cell_value(i, 5))*pi/180   #deg-->rad
            alpha.append(aoa)
            #
            de = float(sheet.cell_value(i, 6))*pi/180    #deg-->rad
            delta_e.append(de)
            #
            trim = float(sheet.cell_value(i, 7))*pi/180  #deg-->rad
            delta_tr.append(trim)
            #
            fe = float(sheet.cell_value(i, 8))
            F_e.append(fe)
            #
            ffl = float(sheet.cell_value(i, 9))*0.000125998   #lbs/hr --> kg/s
            F_fl.append(ffl)
            #
            ffr = float(sheet.cell_value(i, 10))*0.000125998  #lbs/hr --> kg/s
            F_fr.append(ffr)
            #
            f_used = float(sheet.cell_value(i, 11))*0.453592  #lbs --> kg
            F_used.append(f_used)
            #
            temp = float(sheet.cell_value(i, 12))+273.15   #C-->K
            TAT.append(temp)
            
    
    
    #SHIFT IN CENTER OF GRAVITY
    t_cg = []       #time elapsed @ each measurement [s]
    hp_cg = []      #??? [m]
    IAS_cg = []     #Indicated Airpspeed [m/s]
    alpha_cg = []   # [rad]
    delta_e_cg = [] # [rad]
    delta_tr_cg = [] #[rad]
    F_e_cg = []      #[N]
    F_fl_cg = []     #[kg/s]
    F_fr_cg = []     #[kg/s]
    F_used_cg = []   #[kg/s]
    TAT_cg = []      #[C]
    
    for i in range(76):
        if i > 73:  
            a = sheet.cell_value(i, 1).replace(':',' ')
            b = float(a[0:2])*60 + float(a[3:5])
            t_cg.append(b)
            #
            h = float(sheet.cell_value(i, 3))*0.3048     #ft-->m
            hp_cg.append(h)
            #
            v = float(sheet.cell_value(i, 4))*0.514444    #kts-->m/s
            IAS_cg.append(v)
            #
            aoa = float(sheet.cell_value(i, 5))*pi/180   #deg-->rad
            alpha_cg.append(aoa)
            #
            de = float(sheet.cell_value(i, 6))*pi/180    #deg-->rad
            delta_e_cg.append(de)
            #
            trim = float(sheet.cell_value(i, 7))*pi/180  #deg-->rad
            delta_tr_cg.append(trim)
            #
            fe = float(sheet.cell_value(i, 8))
            F_e_cg.append(fe)
            #
            ffl = float(sheet.cell_value(i, 9))*0.000125998   #lbs/hr --> kg/s
            F_fl_cg.append(ffl)
            #
            ffr= float(sheet.cell_value(i, 10))*0.000125998  #lbs/hr --> kg/s
            F_fr_cg.append(ffr)
            #
            f_used= float(sheet.cell_value(i, 11))*0.453592  #lbs --> kg
            F_used_cg.append(f_used)
            #
            temp = float(sheet.cell_value(i, 12))+273.15   #C-->K
            TAT_cg.append(temp)    
    
    
    return mppl, mpplist, pplname, mfuel, time, hp, IAS, alpha, delta_e, delta_tr, F_e, F_fl, F_fr, F_used, TAT, t_cg, hp_cg, IAS_cg, alpha_cg, delta_e_cg, delta_tr_cg, F_e_cg, F_fl_cg, F_fr_cg, F_used_cg, TAT_cg
 
#COPY AND PASE THIS TO YOUR .PY TO HAVE ALL VARIABLES READY TO USE
#SECOND MEASUREMENT SET 
mppl= get_Data2()[0]
mpplist = get_Data2()[1]
pplname = get_Data2()[2]
mfuel  = get_Data2()[3]
time = get_Data2()[4]
hp = get_Data2()[5]
IAS = get_Data2()[6]
alpha = get_Data2()[7]
delta_e = get_Data2()[8]
delta_tr = get_Data2()[9]
F_e = get_Data2()[10]
F_fl = get_Data2()[11]
F_fr = get_Data2()[12]
F_used = get_Data2()[13]
TAT = get_Data2()[14]
t_cg = get_Data2()[15]
hp_cg = get_Data2()[16]
IAS_cg = get_Data2()[17]
alpha_cg = get_Data2()[18]
delta_e_cg = get_Data2()[19]
delta_tr_cg = get_Data2()[20]
F_e_cg = get_Data2()[21]
F_fl_cg = get_Data2()[22]
F_fr_cg = get_Data2()[23]
F_used_cg = get_Data2()[24]
TAT_cg = get_Data2()[25]
#print alpha 

def get_eigentimes():
    #EIGENMOTIONS 
    
    a = sheet.cell_value(82, 3).replace(':',' ')
    phugoid = float(a[0:2])*60 + float(a[3:5])
            
    a = sheet.cell_value(83, 3).replace(':',' ')
    short_period = float(a[0:2])*60 + float(a[3:5])
    #
    a = sheet.cell_value(82, 6).replace(':',' ')
    dutch_roll = float(a[0:2])*60 + float(a[3:5])
    
    a = sheet.cell_value(83, 6).replace(':',' ')
    dutch_roll_yd = float(a[0:2])*60 + float(a[3:5])
    
    a = sheet.cell_value(82, 9).replace(':',' ')
    aper_roll = float(a[0:2])*60 + float(a[3:5])
    
    a = sheet.cell_value(83, 9).replace(':',' ')
    spiral = float(a[0:2])*60 + float(a[3:5])
    return phugoid, short_period, dutch_roll, dutch_roll_yd, aper_roll, spiral

#EGIVENMOTIONS STARTIME 
phugoid = get_eigentimes()[0]
short_period = get_eigentimes()[1]
dutch_roll = get_eigentimes()[2]
dutch_roll_yd = get_eigentimes()[3]
aper_roll = get_eigentimes()[4]
spiral = get_eigentimes()[5]

