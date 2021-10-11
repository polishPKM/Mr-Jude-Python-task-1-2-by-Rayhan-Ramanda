# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 06:48:56 2021

@author: ibure
"""

cost = 1
totalCost = 0

print("Input prices. Enter 0 to indicate that you are done entering.")
while cost != 0:
    strCost = input("Enter the cost of the item: ")
    cost = float(strCost)
    totalCost += cost
else:
    print ("The total is " + "${:,.2f}".format(totalCost))

strTip = input("How much would you like to tip? Enter whole numbers, I will treat it as a percent: ")

tipPercent = float(strTip) / 100

tipAmount = totalCost * tipPercent
print("You want to tip " + strTip + "%")
print("That is " + "${:,.2f}".format(tipAmount))
grandTotal = float(tipAmount) + totalCost
print("The total cost, with tip, is: "  "${:,.2f}".format(grandTotal))