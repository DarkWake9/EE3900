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

#e2.5
n = np.array(range(0, 21))
x = [xn(i) for i in n]


yn= lambda n: xn(n-1) + xn(n+1)
y = [yn(i) for i in n]


plt.figure()
plt.stem(n , y)
plt.xlabel("n")
plt.ylabel("y(n)")
plt.grid(True, which='both')
plt.savefig('/media/darkwake/VIB2/EE3900/pingala/figs/e2.5.jpg')
plt.show()