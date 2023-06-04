#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 12:14:33 2023

@author: ishita
"""
#ask user to input how much currency they have
yuan = int(input('What do you have left in yuan? '))
yen = int(input('What do you have left in yen? '))
won = int(input('What do you have left in won? '))

#assign currency value to variable to exchange from yuan to USD
x = yuan * 0.14
print(x)

#assign currency value to variable to exchange from yen to USD
y = yen * 0.0071
print(y)

#assign currency value to variable to exchange from won to USD
z = won * 0.00076
print(z)

#to calculate the total amount left in USD
totalUSD = x + y + z

#print total USD amount
print(totalUSD)

