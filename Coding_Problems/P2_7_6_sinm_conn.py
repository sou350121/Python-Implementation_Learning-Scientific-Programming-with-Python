# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:29:51 2019

@author: Ken

program name : sinm_cosn
"""
import math
def double_factorial(inp):
    outcome =  1
    if inp >= 1 == True:
        if inp % 2 == 1:
            for i in range(1,int((inp+1)/2),2):
                outcome *= i
            
        else:
            for i in range(2,int(inp/2),2):
                outcome *= i
        return outcome
    else:
        print("Error: input is needed to larger than 1")
        
def sinm_cons(m,n):
    try: 
        if m % 2 and n % 2  == 1:
            result = (math.pi/2)*double_factorial(m-1)*double_factorial(n-1)/double_factorial(m+n)
        else:
            result = double_factorial(m-1)*double_factorial(n-1)/double_factorial(m+n)
        return result
    except:
        print("Error :m or n are needed to be larger than 1")
        
m, n = 10, 3
z = sinm_cons(m,n)

location = "D:\Python\LearningScienctificProg\.spyproject\\"
location = location.replace('\\','/')
f = open(location + "place_of_result.txt","w" )
print("the result is ",z, file = f)
f.close()

#done