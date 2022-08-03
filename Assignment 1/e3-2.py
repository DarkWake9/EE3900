import numpy as np


x = (1,2,3,4,2,1)
y = [0]*6

for n in range(len(x)):
    if n-2 > 0:
        y[n] - y[n-2]/2.0 = x[n] + x[n-2]
