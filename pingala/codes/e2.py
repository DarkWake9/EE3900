import numpy as np
import matplotlib.pyplot as plt
import os


def xn(n):
    if n >= 0:
        if n in [0,1]:
            return 1
        else:
            return xn(n-1) + xn(n-2)
    else:
        return 0

#e2.1
n = np.array(range(0, 21))
x = [xn(i) for i in n]
plt.figure()
plt.stem(n , x)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.grid(True, which='both')
plt.savefig('/media/darkwake/VIB2/EE3900/pingala/figs/e2.1.jpg')
plt.show()

def Xplus(n, x):
    temp = []
    for i in range(n):
        for j in range(1000):
            x[i]
