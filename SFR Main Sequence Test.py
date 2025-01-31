#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:21:07 2024

@author: ishita
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel('Galaxy Data Infrared.xlsx')

stellar_mass = df['stellar_mass']

stellar_mass_err = df['stellar_mass_err']

sfr = df['sfr']

sfr_err = df['sfr_err']

x = stellar_mass
y = sfr


font = {'family':'Times New Roman'}
fig, ax = plt.subplots(1,figsize = (5,5))

plt.plot(x, y)


plt.xlabel(r'$log_{MSTARS}$',**font,fontsize=20)
plt.ylabel("log SFR ($M_{\odot}$)",**font,fontsize=20)

#ax.invert_yaxis()

#ax.minorticks_on()
#ax.tick_params(axis='both', which='minor', right=True, top=True, direction='in',width=2,labelsize=15,length=3)
#ax.tick_params(axis='both', right=True, top=True, direction='in',width=2,labelsize=15,length=6)


plt.show()

