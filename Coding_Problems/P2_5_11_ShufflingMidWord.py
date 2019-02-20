# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:43:45 2019

@author: Ken

Program title: middle lETTERS SHUFFLED RANDOMLY
"""
import random
import math

string = 'this is a function for suffling the letter in the middle'

def suffling(string):
    a = string.split(" ") # splitting string into a list 
    amount = len(a) # length of list 'a'
    mid_index = math.floor(amount/2 + 1) # ex. 1 2 3 4 5 --> 5/2 +1 = 3.5; floor(3.5) = 3 
    mid_letter = list(a[mid_index-1]) # the index in python need to be reduced by 1 
    random.shuffle(mid_letter) # this coding is wrong-->mid_letter = random.shuffle(mid_letter)
    mid_word = ''.join(mid_letter[:])
    a[mid_index-1] = mid_word
    suffled_string = ' '.join(a)
    return suffled_string

suffled_string = suffling(string)
#Done 10/2/2019 0:29
        
    
    
