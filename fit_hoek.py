"""
Created on Mon Sep 22 23:29:19 2025

@author: caspe
"""
#imports
import numpy as np
import math as math
#de formule om de optische weg lengten te bepalen.
def autopos(hoek_inval_g, d, g_len, n):
    hoek_inval_r= np.radians(hoek_inval_g)
    hoek_blok = np.arcsin(np.sin(hoek_inval_r) / n)
    d_op = (n * d / np.cos(hoek_blok)) - (n*d) 
    return 2*d_op / g_len ,hoek_blok
#eenheden opstelling.
d=3*10e-4
n=1.5
g_len=(550*10e-9)
hoek_inval_g=np.linspace(0,20,100)
#berekenen hoeveel franjes er zijn voor een bepaalde hoek.
N,theta_b2=autopos(hoek_inval_g,d,g_len,n)
#plotten van de grafiek.
plt.plot(hoek_inval_g,N)
plt.xlabel('graden')
plt.ylabel('franjes (N)')
plt.title(f'voor dikten({d}m)')
plt.grid()
plt.show()
