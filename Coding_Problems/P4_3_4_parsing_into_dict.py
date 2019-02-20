# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:29:27 2019

@author: Ken

name: achieve the same goal

"""


# creating a document
'''
import random
import string
f = open('iban_legths.txt','w')
for i in range(50):
    r1 , r2 = random.choice(string.ascii_uppercase), random.choice(string.ascii_uppercase)
    print("{}{} {}".format(r1,r2,random.randint(10,30)) ,file = f)
f.close()
'''

with open('iban_legths.txt') as f:
    iban_legths = {k: int(v) for k,v in [line.split() for line in f]}


# done, 13:29


