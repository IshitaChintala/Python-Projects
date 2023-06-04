#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 12:06:24 2023

@author: ishita
"""
#quadratic formula challenge project
#beware complex numbers! 

#insert value for b
b = int(input('insert value for b: '))

#insert value for a 
a = int(input('insert value for a: '))

#insert value for c
c = int(input('insert value for c: '))


#to solve for first factor
x1 = (-1*b + (b**2-4*a*c)**0.5) // 2*a

#to solve for second factor
x2 = (-1*b - (b**2-4*a*c)**0.5) // 2*a

print(x1)
print(x2)

