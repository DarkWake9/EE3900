import numpy as np
import matplotlib.pyplot as plt

xn = [1,2,3,4,2,1]
N = 6
X = [0]*6
pi = np.pi
for k in range(N):
    for i in range(N):
        X[k] = xn[i] * np.exp(-1 * 1j * 2 * pi * k * i / float(N))

plt.plot(xn, np.abs(X))
plt.title('DFT')
plt.xlabel('$x$')
plt.ylabel('$|X(k)|$')
plt.grid()
print(X)
plt.show()

