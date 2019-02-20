# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:24:11 2019

@author: Ken

name: calculating trace of matrix by list comprehension
"""
# trace of a matrix is the sum of diagonal elements

matrix = [[1,2,3],[4,5,6],[7,8,9]]
trace = 0
'''
for i in range(0,len(matrix)):
    dia_element = matrix[i][i]
    trace += dia_element
'''
trace = sum( [matrix[i][i] for i in range(0,len(matrix)) ] )

#done 14:00; i spend too much time ... = =