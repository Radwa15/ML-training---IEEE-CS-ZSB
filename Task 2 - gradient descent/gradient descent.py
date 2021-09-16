# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 02:09:40 2021

@author: Ahmed
"""


import matplotlib.pyplot as plt
import numpy as np

def cost_fun(th0,th1,x,y):
    m = len(x)
    errors =0
    for i in range(0,m):
        y_predicted = th0 * x + th1
        errors =+ (y_predicted - y)**2
    res = (1/(2*m)) * errors
    print (res[1])
    
def gradient_descent(x,y):
    th0 = th1 = 0
    rate = 0.01
    n = len(x)
    plt.scatter(x,y,color='red',marker='+',linewidth='5')
    for i in range(20):
        y_predicted = th0 * x + th1
        cost = (1/(2*n)) * sum([val**2 for val in (y-y_predicted)])
        plt.plot(x,y_predicted,color='blue')
        xd = -(2/n)*sum(x*(y-y_predicted))
        yd = -(2/n)*sum(y-y_predicted)
        th0 = th0 - rate * xd
        th1 = th1 - rate * yd
    print (th0,th1,cost)
 
#x = np.array([1,2,5,7,9,10,13,14,17,19,21,22,26,27,28,2,30,34,35,38])
#y = np.array([10.4,56,1.4,9.4,41.8,46,38,72,77,42.8,71,82.2,81.6,56.8,102,77,88.8,69,68.2,95.8])    
x = np.array([1,2,3,4])
y = np.array([0,1,2,3])
gradient_descent(x,y)