# -*- coding: utf-8 -*-
import sys
import os

path = sys.argv[0]
dir_ = os.path.dirname(path)


f = open(dir_+'/'+'redwood-data.txt','r')

content= []
name = []
tree =[]
height=[]
for line in f:
    content.append(line.split()) # do not put any arg inside split so it can split all.

for h in content[:]:
    height.append(h[-1])
    if h[2] in {'Redwoods','Humboldt'}: 
        # there are only two location. I use it as the condition for naming. 
        name.append(h[0]+' '+h[1])
    else:
        name.append(h[0])
    
tallest = max(height)
index = height.index(tallest)

print('the tallest tree is {0}, which tall {1} (m).'.format(name[index],tallest))

#done