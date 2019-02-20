# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:15:26 2019

@author: Ken

name : Shoelace algorithm for calcuating the area of a simple polygon 

"""

# For calcuating the area of a simple polygon 
import datetime  
import os 
import sys
import numpy as np 

print('Today is {}'.format(datetime.date.today()))
print('the dir of this file is {}'.format(os.path.dirname(sys.argv[0] )))

Vertices_list = np.array([[0,0],[2,0],[2,2],[0,2]])

Vertices_list = np.vstack((Vertices_list,Vertices_list[0]))

S1 = np.sum(Vertices_list[0:-1,0] * Vertices_list[1:,1])
S2 = np.sum(Vertices_list[0:-1,1] * Vertices_list[1:,0])

S = (1/2)* np.abs(S1-S2)

print("the area of the given paragon is {:}".format(S))