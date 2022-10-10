import numpy as np
import matplotlib.pyplot as plt
import os
import scipy

def xn(n):
    if n >= 0:
        if n in [0,1]:
            return 1
        else:
            return xn(n-1) + xn(n-2)
    else:
        return 0

#e2.2a
alpha = float(0.5*(1+np.sqrt(5)))
beta = float(0.5*(1-np.sqrt(5)))
def an(n):
    if n > 0:
        return (alpha**n - beta**n)/(alpha - beta)
    else:
        return 0

n = np.array(range(0, 21))
x = [xn(i) for i in n]
a = [an(i+1) for i in n]
plt.subplot(2,1,1)
plt.stem(n , x)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.grid(True, which='both')

plt.subplot(2,1,2)
plt.stem(n , x)
plt.xlabel("n")
plt.ylabel("$a_{n+1}$")
plt.grid(True, which='both')

plt.savefig('/media/darkwake/VIB2/EE3900/pingala/figs/e2.3a.jpg')
plt.show()