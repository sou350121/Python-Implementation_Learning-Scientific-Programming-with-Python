# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:41:51 2019

@author: Ken'

name : A DNA sequece encodes 
"""

# AGTCTTATATCT includes (AGT,CTT,ATA,TCT) if we read it in first frame 
# it includes( GTC, TTA ,TAT) in its second frame, and so on...

# write a program to extract the codons into a list of 3-letter strings 
# given a sequence and frame as an integer valuse (0,1,2)

import sys 
import math

#DNA= sys.argv[1]
DNA = "AGTCTTATATCT"
frame = 1
interval = 3
seq = []
seq_list = []
try:
    DNA = DNA
except ValueError:
    print("please input a string of DNA but not the other.")
    
start = frame -1 

for j in range(  math.floor((len(DNA)-frame+1)/3) ):
    for i in range(3):
        seq = DNA[start:start+3]
    seq_list.append(seq)
    seq = []
    start = start +3
    
print("the sequencing result is {0} from DNA ({1})".format(tuple(seq_list),DNA))