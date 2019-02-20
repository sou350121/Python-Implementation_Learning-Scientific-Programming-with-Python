# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:28:26 2019

@author: Ken

name : Random Flight Model

"""
import math
import random

class Polymer:
    # initialization with arguments : N: the number of segments; a: the segment length.
    def __init__ (self,N,a):
        self.N, self.a = N, a 
        self.xyz = [(None, None, None)] * N # " * N " is aimming to attend N 3D-tuple into self.xyz
        self.R = None #End-to-end vector
        self.make_polymer() #make our polymer by assigning segment positions
        
    def make_polymer(self):
        self.xyz[0] = x, y, z = cx, cy, cz = 0., 0., 0.
        for i in range(1,self.N):
            # Pick a randim orientation for the next segment.
            theta = math.acos(2 * random.random() -1 ) # -1 < val < 1
            phi = random.random() *2. * math.pi
            x += self.a * math.sin(theta) * math.cos(phi)
            y += self.a * math.cos(theta) * math.sin(phi)
            z += self.a * math.cos(theta)
            self.xyz[i] = x ,y ,z 
            cx, cy, cz = cx + x, cy +y, cz + z 
        cx, cy, cz =cx/ self.N, cy/self.N , cz/self.N
        self.R = x ,y, z
        
        for i in range(self.N):
            self.xyz[i] = self.xyz[i][0] - cx , self.xyz[i][1] - cy ,self.xyz[i][2] - cz  
            
    def calc_Rg(self):
        self.Rg = 0
        for x, y, z in self.xyz:
            self.Rg += x**2 + y**2 + z**2
            self.Rg = math.sqrt(self.Rg/ self.N)
            return self.Rg
        
polymer = Polymer(1000, 0.5)
print("The end to end vector is ({0[0]:.3f}, {0[1]:.3f}, {0[2]:.3f}), \n and the radius\
 of gyration is {1:.3f}.".format(polymer.R , polymer.calc_Rg()))