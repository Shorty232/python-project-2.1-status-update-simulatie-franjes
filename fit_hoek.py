
"""
Created on Mon Sep 22 23:29:19 2025

@author: caspe
"""

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as math
def autopos(hoek_inval_g, d, g_len, n):
   
    hoek_inval_r= np.radians(hoek_inval_g)
    hoek_blok = np.arcsin(np.sin(hoek_inval_r) / n)
    d_op = (n * d / np.cos(hoek_blok)) - (n*d) 
    return 2*d_op / g_len ,hoek_blok



d=3*10e-4
n=1.5
hoek_inval_g=np.linspace(0,10,100)

g_len=(550*10e-9)

N,theta_b2=autopos(hoek_inval_g,d,g_len,n)

plt.plot(hoek_inval_g,N)
plt.xlabel('graden')
plt.ylabel('franjes (N)')
plt.title(f'voor dikten({d}m)')
plt.show()
