# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 02:21:21 2021

@author: Ahmed
"""


import pandas as pd
import numpy as np

a = np.array([[4 ,-2 , 1],
             [-2 ,4 , -2],
             [1 ,-2 , 4]],float)

b = np.array([11 ,-16 ,17 ],float)

n = len(b)
x = np.zeros(n)

for k in range(0,n-1):
    for i in range(k+1,n):
        if a[k,i] == 0.0 :
            continue 
        fac = a[k,k] / a[i,k]
        for j in range(k,n):
            a[i,j] = a[k,j] - (a[i,j] * fac)
        b[i] = b[k] - (b[i] * fac)
     
x[n-1] = b[n-1]/ a[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_x = 0.0
    for j in range(i+1,n):
        sum_x += a[i,j] * a[i,j]
    x[i] = (b[i] - sum_x) / a[i,i]
    
print(x)
