# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:56:10 2019

@author: biron
"""

from findCG import *
from DataReader import *
from data_processing import *

time = get_Data2()[15]

t1 = time[0] + UTC_Seconds[0]
t2 = time[1] + UTC_Seconds[0]

cg_delta = cg_time(t2,cg_walk) - cg_time(t1,cg_normal)
print(cg_delta, cg_time(t2,cg_walk), cg_time(t1,cg_normal))