#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:39:36 2024

@author: ishita
"""

#W1: -20.36 - 9.47(x - 2.4)
#W2: -19.76 - 9.66(x - 2.4)
#x is wmax

#M = -5logd + 5 + (extinction-corrected m)

#dev = MW1 - TFpredicted

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel('Galaxy Data Infrared.xlsx')

d = df['Distance (pc)']

galaxy = df['Galaxy']
print(galaxy)

#m_W1 = df['w1mpro corrected']

#calculated via distance modulus
#M_W1 = m_W1 - 5 * np.log10(d) + 5

m_W2 = df['w2mpro corrected']

#calculated via distance modulus
M_W2 = m_W2 - 5 * np.log10(d) + 5

w_max =df['w_max']

#assigning x variable to star formation rates of galaxies in sample
x = df['sfr']

#assigning x error from excel sheet
xerr = df['sfr_err']

#for error bar calculation
x_err = xerr

#apparent magnitudes in W1 uncertainties
mW1un = df['extinction values W1']

#calculating first half under sq root
M_W1_1 = (np.power(1, 2, out=None))*(np.power(mW1un, 2, out=None))

#calculating second half under sq root
M_W1_2 = (np.power(((-5)/np.log(d)), 2, out=None))*(np.power((np.log10(d)), 2, out=None))

#calculating entire value under root for DM error
M_W1_err = M_W1_1 + M_W1_2

#calculating tully-fisher predicted abs. mag. uncertainties; distance error
TFW1un = df['distance_err_pos']

#calculating entire value under root for TF error
TF_W1_err = np.power(((-4.11276)/x), 2, out=None)

#calculating y error for error bar
yerr = np.sqrt(M_W1_err + TF_W1_err)


#zp1 = -20.36
#m1 = -9.47

zp2 = -19.76
m2 = -9.66

#galaxy = df['Galaxy']

#galaxy names
#labels = ['NGC1052, NGC1566, NGC3147, NGC3227, NGC3783, NGC3786, NGC3982, NGC4051, NGC4138 ,NGC4151, NGC4258, NGC4303, NGC4395, NGC4438, NGC4565, NGC4639, NGC4939, NGC4945, NGC5055, NGC5194, NGC5643, NGC5728, NGC6814, NGC6951, NGC7674, M58, M104']

#calculated via tully-fisher
#TF_W1 = zp1 + m1 * (w_max - 2.4)

#calculated via tully-fisher

TF_W2 = zp2 + m2 * (w_max - 2.4)
print(TF_W2)

#calculating deviation of true M with predicted M
#dev_W1 = M_W1 - TF_W1

dev_W2 = M_W2 - TF_W2
print(dev_W2)

x = df['sfr']
y = dev_W2
y_err = yerr


font = {'family':'Times New Roman'}
fig, ax = plt.subplots(1,figsize = (5,5))
plt.plot(x, y, 'ko')


ax.set_xlabel(r'Star Formation Rate ($M_{\odot}$)', **font,fontsize=20)
ax.set_ylabel("Abs. Mag - TFPred. in W2 (M)",**font,fontsize=20)
ax.set_title("Abs. Mag. - TFPredicted vs SFR in WISE filter 2",**font,fontsize=20)
ax.errorbar(x,y,xerr=x_err,yerr=y_err,ecolor='black',fmt='none',lw=1.5)
#ax.set_ylim(-10,2)
ax.invert_yaxis()

ax.minorticks_on()
ax.tick_params(axis='both', which='minor', right=True, top=True, direction='in',width=2,labelsize=15,length=3)
ax.tick_params(axis='both', right=True, top=True, direction='in',width=2,labelsize=15,length=6)

ax.axhline(0.0, linestyle='--')

#plot error using SFR calculations code


plt.show()


