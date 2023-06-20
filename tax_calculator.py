#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:52:08 2023

@author: ishita
"""

#don't forget double (()) after XX: int(input(XX)) 

#do not enter '2.0', or any number with .0, this will result in error since int is only non-decimal values
amount = int(input("Insert amount purchased: "))

#use float, since 0.04 isn't an integer. 4% sales tax converts to 0.04, which is a float value in python
tax = float(input("Insert sales tax of your area in decimal form: "))


#display using tax formula

total = amount + amount*tax

#always use f, then '' around ENTIRE string for string indentation
#i.e: f'the star is {variable}' 

#if condition that states if tax is less than 5%, the area you live in is ideal
if tax < 0.05:
    print(f'You are lucky to live where you do! Your total is only {total}')
    
#if tax is higher than 5%, then your tax is high :(
else: 
    print(f'Your tax is high! Your total is {total}')
    


#print(f'Your total is {total}')


#prints total price from float to int

#total = int(total)
#print(total)

#prints total price from int to float

#total = float(total)
#print(total)

