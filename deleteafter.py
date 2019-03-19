# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:05:45 2019

@author: biron
"""

pix  = 0.0619753086419 #m/pix


# fuselage
lfuse = 32.5 #m

cg_fus1 = 0.45*lfuse
cg_fus2 = 0.42*lfuse
print((0.47*lfuse), "fuselage cg")


#wing 

bwing = 28.08 #m
cwing = 27*pix

cgwing_hor = 0.35*bwing/2
cgwing_ver = 0.7*cwing

dis =26*pix





#horizontal tail
bhor = 10.04 #m
chor = 55*pix 

hortail_cghor = 0.38*bhor/2
hortail_cgver = 0.42*chor

horizon = lfuse + (0.42*chor)
print(horizon, "horizontal tail")


#vertical tail

bver = 63*pix
cver = 65*pix

cgver_ver = 0.38*bver
cgver_hor = 0.42*cver

vertical = lfuse - ((1-0.42)*cver)
print(vertical, "vertical tail")

#nacelle
nacelleL = 79*pix

cgnacelle = 0.4*nacelleL
print(cgnacelle/pix,"hoho")

#landing gear
#nose the first wheel = distance+14.01
distance = 54*pix
print(distance+14.01,"landing gear")

dis =26*pix

new = distance - dis +14.01
print(new,"wing")

nac = 59*pix

nac_dis = distance+14.01+nac+cgnacelle
print(nac_dis,"nacelle")


#wing group cg

wing_group = (6364.4*15.75+1167.7*17.36)/7532.1
print(wing_group,"wing group cg")

fuse_group = (8312.1*14.14+590.3*30.52+409.4*30.16+202.5*3.47+788.6*25.07+3929.8*24.11)/14232.7
print(fuse_group,"fuselage group cg")
 

#front luggage cabin
x = 75*pix
fr_cabin = distance+14.01-x
print(fr_cabin,"nose to front cabin cg")

#rear luggage cabin
y = 57*pix
re_cabin = distance+14.01+y
print(re_cabin,"nose to rear cabin cg")


row = 5.8986/pix
print(row)



