import numpy as np
import matplotlib.pyplot as plt

#defining x(n) as shown in 3.2

def x(n):
    #if n < 0:
    #    return 0
    if n >= 0 and n < 6:
        x_dict = {0:1,1:2,2:3,3:4,4:2,5:1}
        return x_dict[n]
    else:
        return 0
N = 6
def Xx(N):
    X = [0]*N
    for k in range(len(X)):
        for n in range(N):
            X[k] += x(n)*np.exp(-1j * 2 * np.pi * k * n / N)  
    return X

#defining h(n) as shown in 5.6
def h(n):
    if n < 0:
        return 0

    elif n == 0:
        return 1    #h(0) = 1
        
    elif n == 1:
        return -0.5 #h(1) = -1/2
    else:
        return 5.0 * ((-0.5)**n)
#N = 15
def Hh(N):
    H = [0]*N
    for k in range(len(H)):
        for n in range(N):
            H[k] += h(n) * np.exp(-1j*2*np.pi * k * n / N)  
    return H
N = 20
X = Xx(N)
H = Hh(N)

Y = [X[k] * H[k] for k in range(N)]

Y = np.real(Y)/N
print("\nRe{Y}\n")
print(Y)
#plots
plt.stem(range(0,N),Y)
plt.title('Filter Output using DFT')
plt.xlabel('$k$')
plt.ylabel('$Y(k)$')
plt.grid()
plt.show()