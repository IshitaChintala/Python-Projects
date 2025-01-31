#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 07:45:22 2024

@author: ishita
"""

import pandas as pd

df=pd.read_excel('Star Formation Data.xlsx')

log_lsf = df['logLSF']

log_lsf_err = df['E_logLSF']


l_mbb = 10.**(log_lsf)
l_mbb_err = 10.**(log_lsf+log_lsf_err) - 10.**(log_lsf)

#eq 6 from above paper, read in modified black body (MBB) component of luminosity, need to convert to
#star-forming luminosity: L_SF = (4/3)L_MBB

lsf = (4./3.)*l_mbb #units of L_sun (3.846 × 10^33 ergs/sec)

lsf_err = (4./3.)*l_mbb_err
#above paper references murphy 2011 (https://ui.adsabs.harvard.edu/abs/2011ApJ...737...67M/abstract)
#SFR_IR (M_sun / yr) = 3.88 × 10^−44 (L_IR) (ergs/sec)
#convert lsf to ergs/s using l_sun

l_ir = lsf*3.846e33
l_ir_err = lsf_err*3.846e33

sfr = 3.88e-44*l_ir
sfr_err = 3.88e-44*l_ir_err

print(sfr)
print(sfr_err)

