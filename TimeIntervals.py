#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:02:32 2019

@author: FCRA
"""

from DataReader import get_eigentimes
from readmat import *
from data_processing import find_index, seconds_to_utc


#SHORT PERIOD START
def short_period():
    short_period = get_eigentimes()[1]              #times from post_datasheet
    t_sp_utc = seconds_to_utc(short_period)         #converting that to UTC time
    i_t_sp = find_index(t_sp_utc)                   #index of the start of each motion
    tend_sp_utc = 40420                             #end time of motion
    return t_sp_utc, tend_sp_utc, i_t_sp
    

def phugoid():
    phugoid = get_eigentimes()[0]
    t_phu_utc = seconds_to_utc(phugoid)
    i_t_phu = find_index(t_phu_utc)
    tend_phu_utc = 40650
    return t_phu_utc, tend_phu_utc, i_t_phu
    
def dutch_roll():
    dutch_roll = get_eigentimes()[2]
    t_dr_utc = seconds_to_utc(dutch_roll)
    i_t_dr = find_index(t_dr_utc)
    tend_dr_utc = 40695.4
    return t_dr_utc, tend_dr_utc, i_t_dr
    
def dutch_roll_yd():
    dutch_roll_yd = get_eigentimes()[3]
    t_dryd_utc = seconds_to_utc(dutch_roll_yd)
    i_t_dryd = find_index(t_dryd_utc)
    tend_dryd_utc = 40815
    return t_dryd_utc, tend_dryd_utc, i_t_dryd

def aper_roll():
    aper_roll = get_eigentimes()[4]
    t_apr_utc = seconds_to_utc(aper_roll)
    i_t_apr = find_index(t_apr_utc)
    tend_apr_utc = 40335
    return t_apr_utc, tend_apr_utc, i_t_apr

def spiral():
    spiral = get_eigentimes()[5]
    t_spir_utc  = seconds_to_utc(spiral)
    i_t_spir = find_index(t_sp_utc)
    tend_spir_utc = 41031
    return t_spir_utc, tend_spir_utc, i_t_spir
