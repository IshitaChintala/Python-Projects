#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:08:27 2024

@author: ishita
"""

import pandas as pd
import matplotlib.pyplot as plt

#read excel file
df=pd.read_excel('Galaxy Data Infrared.xlsx')

#assign w_max: galactic rotational velocity to x variable
x = df['w_max']
#assign MW1 or MW2 for y variable
y = df['MW1'] 

#y error: derivative of TF relation of W1 or W2 devided by w_max
#TF_W2 = -19.76 -9.66(x - 2.4)
#TF_W2 = - 9.66x + 3.424
#yerr (W2) = -4.19528 / x
yerr = (4.11276) / x
#w_max error in csv file
xerr = df['w_max err']
#formatting
x_err = xerr 
y_err = yerr

#zero-point number for tully-fisher calibration gathered from paper
zp1 = -20.36

#slope number for tully-fisher calibration gathered from paper
m1 = -9.47

#calculated absolute magnitude via tully-fisher calibration from paper in W1
#w_max uncertainty
TF_W1 = zp1 + m1 * (x - 2.4)

xaxis = x
yaxis = TF_W1

#assigning font 'times new roman'
font = {'family':'Times New Roman'}

#create figure called 'ax'
fig, ax = plt.subplots(1,figsize = (7,7))

#adjusting size
plt.subplots_adjust(left=0.2,bottom=0.15)

#assign black box around graph w line width 2
plt.setp(ax.spines.values(), linewidth=2)

#assign x label as w_max with font and fontsize 23
ax.set_xlabel(r'W_Max',**font,fontsize=23)

#assign y label as w_max with font and fontsize 23
ax.set_ylabel(r'Abs. Mag. W1',**font,fontsize=23)

ax.set_title(r'Abs. Mag. W1 vs W_Max',**font,fontsize=23)


#invert so highest neg number is on top
plt.gca().invert_yaxis()

#making scatter plot
ax.scatter(x,y,c='black')

#tully fisher calibration
ax.plot(xaxis, yaxis)

#error bars
ax.errorbar(x,y,xerr=x_err,yerr=y_err,ecolor='black',fmt='none',lw=1.5)

#ticks on axes
ax.minorticks_on()

ax.tick_params(axis='both', which='minor', right=True, top=True, direction='in',width=2,labelsize=23,length=3)

ax.tick_params(axis='both', right=True, top=True, direction='in',width=2,labelsize=23,length=6)



plt.show()

#ax.scatter(x, y)
#ax.errorbar(x, y, yerr, xerr, color='black', fmt='')
#plt.title('Error Bars in Abs. Mag. W2 vs W_Max')
#plt.xlabel('W_Max')
#plt.ylabel('Abs. Mag. W2')
#plt.show()
#plt.errorbar(x, y, yerr, xerr, fmt='', ecolor='black', elinewidth=None, capsize=None, barsabove=False, 
             #lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None)



