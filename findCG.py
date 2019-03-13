# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:02:09 2019

@author: biron
"""

from DataReader import *

pplname = get_Data2()[2]
pplname.insert(0,"nose")
pplname.insert(1,"aft cabin1")
pplname.insert(2,"aft cabin2")
print(pplname)
mpplist = get_Data2()[1]
cg_list = [74,321,338,131,131,170,214,214,251,251,288,288]
