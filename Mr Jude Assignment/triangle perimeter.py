# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:14:36 2021

@author: ibure
"""

a = float(input("Enter the length of the first side in cm : "))
b = float(input("Enter the length of the second side in cm : "))
c = float(input("Enter the length of the third side in cm : "))
    

perimeter = a + b + c

if a + b > c:
    print("The perimeter of the triangle is {} ".format(perimeter))

if a + b < c :
    print("cant be printed")

