# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:21:27 2019

@author: Ken

name: Question 6_4_1 

introducion : the expansion of the spherical ball of fire generated in an explosion 
    may be analyzed to deduce the initial energy 
    released by a nuclear weapon.
    the formula : 
            R(t)  = CE**(1/5)*Loair**(-1/5)*t**(-2/5)
            
        Use log-log plot to fit the data in Table to the 
        model and confirm the time-dependence of R.
        
        please find E if C~=1 
"""
import os, sys 
import numpy as np

dir_ = sys.argv[0]
dir_name = os.path.dirname(dir_)
with open(dir_name+ "/"+"new-mexico-blast-data.txt",'r') as f:
    f_list = [line.split() for line in f][1:]
    
f_list = np.array(f_list)
x, y = f_list[:,0].astype(np.float) , f_list[:,1].astype(np.float)

# since t**(-2/5) is not proper in numpy, we power -5/2 in both side. 
# therefor, y become :
y = y**(-5/2)

p = np.polynomial.Polynomial

p_fit = p.fit(x,y,deg = [1] ) #specifing coefficients as [0, c1]
c0,c1= p_fit 
print(' Fit : coef of t is  {:f}'.format(c1))

# therefore the E can be counted by putting coefficient inside the formula
#       R**-5/2 == E**-1/2 * Lo **1/2 ** t 
#       Between those, c1 = E**-1/2 * Lo**1/2
#       E = Lo**(1/2)/c1 **2, Lo= 1.25

E = (np.sqrt(1.25)/c1)**2

TNT = 4.184*10**9 / E
print(" the nuclear weapon's data was sampled as {:.3f} kilotons of TNT.".format(TNT))

# done
