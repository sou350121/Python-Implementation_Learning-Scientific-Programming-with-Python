# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:37:29 2019

@author: Ken

Name : E3.3 to plot the functions fn(x) = X^n * sin(x) for n = 1,2,3,4

"""
import pylab

xmin , xmax = -10, 10 
n = 500
x = pylab.linspace(xmin,xmax, n)
for n in range(1,5):
    y = x**n *pylab.sin(x) #pylab.sin can convert a list of x to y, which is sin x)
                            # However, math.sin() can only count size-1 arrays every time
    y /= max(y) # it is equavalent to y = y / max(y), which is normalizating y.)
    pylab.plot(x,y,label = r'$x^{}\sin x$'.format(n))
pylab.legend(loc='lower center')
pylab.show()
pylab.savefig('E3_3.pdf')
