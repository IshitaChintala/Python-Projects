#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:08:42 2023

@author: ishita
"""

#notes about boolean functions: 
    #and = true if both conditions are true- returns false if not true
    #or = true if at least one condition is true- think either or, false if otherwise
    #not = true if condition is false and vice versa; opposite day!
    
#ask user to input value for height variable
height = int(input("What is your height? "))

#ask user to input value for credits variable
credits = int(input("How many credits do you have? "))

#conditions: 
if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
#use elif for any else statement after if besides the last one
#it will throw an error if you use else instead of elif
elif height < 137: 
    print("You're not tall enough to ride.") 
        
elif credits < 10: 
    print("You don't have enough credits")

else: 
    print("Invalid data.")
    
    