#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:23:18 2023

@author: ishita
"""
#a function to add the variables x and y
def add(x, y): 
    #return the x and y variables into console
    return x+y
#display in console
#assign values 1 to x and 2 to y while committing the addition function
print(add(1,2))

#shortcut to above statements
#use lambda function to declare variables, assign the operation, and assign values to variables
#print((lambda x,y: x+y)(1, 2))

#experimentation
print((lambda z, t: z * t)(5, 7))
print((lambda z, t, x, y: (z * t)(x-y))(5, 7, 6, 3))

