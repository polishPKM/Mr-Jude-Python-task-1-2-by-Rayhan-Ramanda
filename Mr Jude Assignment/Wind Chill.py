# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 19:04:03 2021

@author: ibure
"""
import math


while True :
    try:
        temperature = float(input("enter the Temperature for today: "))
        
        
        if temperature <= -58:
            print ("Temperature must be between -58F and 41F")
            continue
        elif temperature >= 41:
            print ("Temperature must be between -58F and 41F")
            continue
        elif temperature >= -58:
             break
        elif temperature <= 41:
            break
    except ValueError:
        print("NaN")
        continue
    
while True:
    try:
        speed = float(input("enter the speed: "))
        if speed <2:
            print("must be greater or equal than 2 MPH")
            continue
        else:
            break
    except ValueError:
        continue

wind_chill_factor_index = 35.74 + 0.6215*temperature - 35.75*math.pow(speed , 0.16) + 0.4275*temperature*math.pow(speed , 0.16)
   
print("the wind chill is " + str("{0:.3f}".format(wind_chill_factor_index)))