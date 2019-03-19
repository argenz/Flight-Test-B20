# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 01:12:31 2019

@author: hksam
"""
import numpy as np
def OpenThrustFile(file):
    
    param_file = open(str(file), "r")
    
    lines = []
    # read line-by-line, split comments
    for line in param_file:
        lines.append(line)
    
    #column 0: LEFT engine thrust; column 1: RIGHT engine thrust
    ThrustLst = np.zeros([len(lines),2], dtype = float)
    
    for i, line in enumerate(lines):
        
        thrusti= line.split('\t')
        
        ThrustLst[i,0] = thrusti[0]
        ThrustLst[i,1] = thrusti[1]
    
    return ThrustLst