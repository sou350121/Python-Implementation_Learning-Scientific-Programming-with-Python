# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:22:29 2019

@author: Ken

name : ROT13 

"""

# the ROT 13 substitution cipher encodes a string by replacing each letter with 
# the letter 13 letters after it in the alphabet.
# for example a -> n, p -> c

import numpy as np
inp = 'ken'

inp = inp.lower()

# the Unicode of number can be converted by function ord()
# 'a' : 97, 'z" : 122
# Since 'a' : 97, 'z" : 122, we need to add other 13 behind 'z':122.
ord_list =  [ ord(x) for x in inp ]
func1 = lambda x : x+13 if x < 122 -13 else x-26+13
outp = [ func1(x) for x in ord_list ]
print([chr(x) for x in outp])

# done
