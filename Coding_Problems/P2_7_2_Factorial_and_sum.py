# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:42:20 2019

@author: Ken

name : find the smallest positive integer whose fatorial is not divisible 
"""

import math

n = 0
stop = 500
while n<stop:
    factorial = math.factorial(n)
    digit_sum = sum( [int(element) for element in str(factorial)])
    if factorial % digit_sum != 0:
        result = n
        break
    n += 1

print('the smallest positive integer, whose fatorial is not divisible by the sum of \
its digit, is : {}'.format(result))

# done