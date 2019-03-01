# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:34:26 2019

@author: Ken

Name: 
    calculate the first derivative of normalized gaussian function with numpy
    without a single loop

input:
    mu = 0
    std = 0.5 , 1., 1.5 
    interval -10<=x<=10 with 1000 points
    small h ~= 0.001
    Verify that the function are normalized with area 1. 
    
output:
    the plot of normalized guassian function with mu = 0 and std= 0.5, 1, 1.5
    
*** the formular inside the book miss the minus of the  power of the exp.
"""

import numpy as np
import pylab as plt
# input 
mu = 0
std_0, std_1,std_2 = 0.5 , 1.0, 1.5
x = np.linspace(-10,10,num = 1000)
h = 0.001

def gaussian_pdf( x , mu, std  ):
    ''' the input must be a array'''
    try: 
        return   (1/(std*np.sqrt(2*np.pi)))* np.exp( -(x-mu)**2/(2*std**2))
    except (ValueError,TypeError):
        print('the input sequence must all be int or float.')
    
def gaussian_first_derivative(x,mu, std,h):
    return ( gaussian_pdf(x+h,mu,std) - gaussian_pdf(x-h,mu,std) ) /2*h

g1 = gaussian_pdf(x,mu, std_0)
g2 = gaussian_pdf(x,mu, std_1)
g3 = gaussian_pdf(x,mu, std_2)

# verify the area 
area1 = sum(g1*abs(x[0]-x[1]))
area2 = sum(g2*abs(x[0]-x[1]))
area3 = sum(g3*abs(x[0]-x[1]))
if float(1) ==  round( area1,5) == round( area2,5) == round( area3,5)  :
    print('verify correctly')
    
g1_1 = gaussian_first_derivative(x,mu,std_0,h)
g2_1 = gaussian_first_derivative(x,mu,std_1,h)
g3_1 = gaussian_first_derivative(x,mu,std_2,h)

plt.plot(x, g1 ,color = 'r', label ='std = 0.5',linestyle = '--' )
plt.plot(x, g2, color = 'r', label ='std = 1.0',linestyle = '-.')
plt.plot(x, g3, color = 'r', label ='std = 1.5')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('gaussian distribution')
plt.legend('best')
plt.show()
plt.plot(x, g1_1, color = 'g', label = '1st mu = 0, std = 1.5',linestyle = '--' )
plt.plot(x, g2_1, color = 'g', label = '1st mu = 0, std = 1.5',linestyle = '-.')
plt.plot(x, g3_1, color = 'g', label = '1st mu = 0, std = 1.5')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('gaussian distribution')
plt.legend('best')
plt.show()

#done


