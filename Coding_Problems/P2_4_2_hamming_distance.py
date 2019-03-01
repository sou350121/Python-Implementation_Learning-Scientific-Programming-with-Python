# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:13:35 2019

@author: Ken

name : Hamming distance 

# the hamming distance between two equal string is
# the number of position at which the characters are different. 

input : s1, s2
output: hamming distance
"""


def hamming_distance(s1,s2):
    ''' the is a function   '''
    # check the length first
    if len(s1) != len(s2):
        print('the length of input sequences should be equivalent.')
        return 
    d = 0
    for element1,element2 in zip(s1,s2):
        print(element1,element2)
        if element1 != element2:
            d+=1
    return d

s1 = 'abcdefghiiii'
s2 = 'abcdefghijkl'
print('the HammingD of two sequence(the length is{})\
 is {}'.format(len(s1),hamming_distance(s1,s2) ))

#done
        
