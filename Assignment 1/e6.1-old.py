import numpy as np
import matplotlib.pyplot as plt

xn = [1,2,3,4,2,1]
N = 6
X = [0]*6
pi = np.pi
for k in range(N):
    for i in range(N):
        X[k] = xn[i] * np.exp(-1 * 1j * 2 * pi * k * i / float(N))
X = np.array(X)

plt.subplot(2, 1, 1)
plt.stem(range(0,N),xn)
plt.ylabel('$x$')
plt.grid()


plt.subplot(2, 1, 2)
plt.stem(range(0,N), abs(X))
plt.title('DFT')
plt.ylabel('$|X(k)|$')
plt.grid()


print(X)
print(abs(X))
plt.show()

