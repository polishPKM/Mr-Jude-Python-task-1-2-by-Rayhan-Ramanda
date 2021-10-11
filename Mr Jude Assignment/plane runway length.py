# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:15:23 2021

@author: ibure
"""

speed= eval(input("enter the plane takeoff speed in m/s: "))
acceleration = eval(input("enter the plane acceleration in m/s**2: "))

length = speed**2 / (2*acceleration)


print("The minimum runway length for this airplane is " + str("{0:.4f}".format(length)) + " meters")