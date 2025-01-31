#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:35:45 2024

@author: ishita
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read excel file 'galactic extinctions'
df=pd.read_excel('Galactic Extinctions.xlsx')

w_max = df['wmax']

d = df['Distance (PC)']

#assign variables for corrected apparent magnitude by reading galactic extinctions excel file
mg = df['Corrected Apparent Magnitude: g']

#using distance modulus equation to find absolute magnitude for each filter
M_G = mg - 5*np.log10(d)+5

#used numpy.log because d is an array, not integer so math function doesn't work here

y = mg - 5 * np.log10(d) + 5


m = -7.37

zp = -20.15

# from Dr. Robinson:
# every TF relationship should be in the form y = zp + m(x - 2.5)
TF_G = zp + m*(w_max - 2.5)

#true-pred

xaxis = w_max
yaxis = TF_G

font = {'family':'Times New Roman'}

fig1 = plt.figure(1, figsize = (7,7.8))
plt.plot(w_max, y,'.w', markersize=10)
plt.plot(xaxis, yaxis, 'xkcd:pale purple', linestyle='-', lw=5)
plt.xlim(2.0, 3.0)
plt.gca().invert_yaxis()

plt.xlabel(r'$W^{\ i}_{mx}$', **font,fontsize=35, fontweight='bold', color='w')
plt.ylabel(r"$M_{g filter}$", **font,fontsize=35, fontweight='bold', color='w')
plt.title("Mg vs Wmax Plot", **font,fontsize=40, fontweight='bold', color='w')

plt.minorticks_on()
plt.tick_params(axis='both', which='minor', right=True, top=True, direction='in',width=2,labelsize=23,length=5)
plt.tick_params(axis='both', right=True, top=True, direction='in',width=2,labelsize=23,length=6)

ax = plt.gca()

ax.set_facecolor('black')
ax.set_facecolor((0.0, 0.0, 0.0))

fig1.set_facecolor('b')
fig1.set_facecolor((0.0, 0.0, 0.0))

plt.show()
