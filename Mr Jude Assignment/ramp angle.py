# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 08:38:29 2021

@author: ibure
"""

import math

g = 9.8
m = float(input("enter the mass of of the cart in KG"))
f = float(input("enter the force in N"))

formula = math.asin(f/(m*g))
degree = formula * (180/math.pi)
    
print ("angle of the ramp is : ", round(degree,1),"degrees")