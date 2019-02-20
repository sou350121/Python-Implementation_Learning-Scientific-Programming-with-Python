# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:50:21 2019

@author: Ken
"""

'''

# writtting up 'powers.txt'
f = open('powers.txt','w')

for i in range(1,1001):
    print(i,i**2,i**3,i**4, sep=', ',file = f )
    
f.close()
'''
location = 'D:/Python/LearningScienctificProg/.spyproject/'
f = open(location + 'powers.txt', 'r')
squares, cubes, fourths = [] , [] , []
for line in f :
    fields = line.split(',')
    squares.append(int(fields[1]))
    cubes.append(int(fields[2]))
    fourths.append(int(fields[3]))
f.close()
n = 123 
print(n , 'cubed is',cubes[n-1])
