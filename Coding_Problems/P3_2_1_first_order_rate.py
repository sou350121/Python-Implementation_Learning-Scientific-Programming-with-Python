# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:31:19 2019

@author: Ken

name: the reaction of first order rate in molecule

# conservation of matter requires : [A]0 - [A] -> [B] + [C]
# with k1 = 300s-1 , k2 = 100s-1 , [A]0 = 2 mol dm-3 

# plot the concentrations of A,C and C aginst time given an initial concentraion 

input : time , k1, k2, [A0]
output: graph with the concentration of A,B and C versus time 
"""

import math
import pylab
import numpy as np
time = pylab.linspace(0,0.05,num= 1001)
k1 = 300 # s-1
k2 = 100 # s-1
conc_A0 = 2.0 # mol dm-3

conc_B = (k1/(k1+k2))* conc_A0 * (1 - np.exp(-(k1+k2)*time))
conc_C = (k2/(k1+k2))* conc_A0 * (1 - np.exp(-(k1+k2)*time))
conc_A = conc_A0 - ( conc_B + conc_C )

pylab.plot(time, conc_B, color = 'b', linestyle ='-', label = 'conc_B')
pylab.plot(time, conc_C, color = 'b', linestyle ='-.',label = 'conc_C')
pylab.plot(time, conc_A, color = 'r', label = 'conc_A')
pylab.legend(fontsize = 16, loc ='best')
pylab.xlabel('time ( m )')
pylab.ylabel('concentration (mol dm-3)')
pylab.title('first order concentraion')
pylab.show()

# done 
