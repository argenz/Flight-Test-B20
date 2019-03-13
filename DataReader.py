#!/usr/bin/env python2
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


loc = ("REFERENCE_Post_Flight_Datasheet_Flight.xlsx") 
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
    TAT = []          #°C
    
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
            f_used = float(sheet.cell_value(i, 8))*0.000125998  #lbs/hr --> kg/s
            F_used.append(f_used)
            #
            temp = float(sheet.cell_value(i, 9))+273.15
            TAT.append(temp)
    return mppl, mfuel, time, hp, IAS, alpha, F_fl, F_fr, F_used, TAT
            

def get_Data2():
    
    mppl = 0
    for i in range(16):
        if i>6:
            mppl = mppl + sheet.cell_value(i,7)
    
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
    TAT = []          #°C
    
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
            f_used = float(sheet.cell_value(i, 11))*0.000125998  #lbs/hr --> kg/s
            F_used.append(f_used)
            #
            temp = float(sheet.cell_value(i, 12))+273.15  #C --> K
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
    TAT_cg = []      #[°C]
    
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
            f_used= float(sheet.cell_value(i, 11))*0.000125998  #lbs/hr --> kg/s
            F_used_cg.append(f_used)
            #
            temp = float(sheet.cell_value(i, 12))
            TAT_cg.append(temp)    
    
    #EIGENMOTIONS ??
    #
    #
    #
    #
    
    return mppl, mfuel, time, hp, IAS, alpha, delta_e, delta_tr, F_e, F_fl, F_fr, F_used, TAT, t_cg, hp_cg, IAS_cg, alpha_cg, delta_e_cg, delta_tr_cg, F_e_cg, F_fl_cg, F_fr_cg, F_used_cg, TAT_cg
 
#COPY AND PASE THIS TO YOUR .PY TO HAVE ALL VARIABLES READY TO USE

#mppl = get_Data()[0]
#mfuel = get_Data()[1]
#time  = get_Data()[2]
#hp = get_Data()[3]
#IAS = get_Data()[4]
#alpha = get_Data()[5]
#delta_e = get_Data()[6]
#delta_tr  = get_Data()[7]
#F_e = get_Data()[8]
#F_fl = get_Data()[9]
#F_fr = get_Data()[10]
#F_used = get_Data()[11]
#TAT = get_Data()[12]
#t_cg = get_Data()[13]
#hp_cg = get_Data()[14]
#IAS_cg = get_Data()[15]
#alpha_cg = get_Data()[16]
#delta_e_cg = get_Data()[17]
#delta_tr_cg = get_Data()[18]
#F_e_cg = get_Data()[19]
#F_fl_cg = get_Data()[20]
#F_fr_cg = get_Data()[21]
#F_used_cg = get_Data()[22]
#TAT_cg = get_Data()[23]
#
#print alpha 