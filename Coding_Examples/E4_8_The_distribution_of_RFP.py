# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:16:28 2019

@author: Ken

name : the distribution of random flight polymers

"""

import pylab
from E4_17_random_fligh_model import Polymer 
pi = pylab.pi

Np = 3000 # Calcuate R for Np polymers
N, a = 1000, 1.
R = [None] * Np
for i in range(Np):
    polymer = Polymer(N,a)
    Rx, Ry, Rz = polymer.R
    R[i] = pylab.sqrt(Rx**2+ Ry**2+ Rz**2)
    if not (i+1) % 100:
        print (i+1, ' / ', Np)

# Drawing the simulation result.
pylab.hist(R, 50, normed = 1)


r = pylab.linspace(0, 200, 1000) # x-axis range 
msr = N* a**2 # mean square position <r^2> = N * a^2
# y-axis : the theoretically predicted PDF of Radius
Pr = 4.*pi*r**2 *(2*pi*msr/3)**-1.5 * pylab.exp(-3*r**2/2/msr) 

# Drawing the theoretically result.
pylab.plot(r, Pr, lw=2, c='r')
pylab.xlabel('R')
pylab.ylabel('P(R)') 
pylab.savefig("Hist_Polymer.png",dpi = 256)
pylab.show()