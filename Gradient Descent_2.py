# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 21:14:06 2019

@author: Tazrin
"""

import numpy as np
import matplotlib.pyplot as plt
import math

initial = 2.4  # The algorithm starts at x
rate = 0.5 #Learning rate
i: int = 0
X = []
Y = []
convergence = 0.0005  # This tells us when to stop the algorithm
previous_step_size = 1  
maximumIteration = 1000  # maximum number of iterations
i = 0  # iteration counter
main = lambda x: math.sin(10*math.pi*x)/(2*x)+(x-1)**4
derivative = lambda x: ((10*math.pi*x*math.cos(10*math.pi*x))-math.sin(10*math.pi*x))/(2*x**2)+3*(x-1)

while previous_step_size > convergence and i < maximumIteration:
    prev_x = initial
    initial = initial - rate * derivative(prev_x)
    previous_step_size = abs(initial - prev_x)
    i = i + 1
    print("Iteration", i, "\nX value is", initial)
    X.insert(i, initial)
    Y.insert(i, main(initial))
    i= i+1
plt.scatter(X, Y)
plt.show()