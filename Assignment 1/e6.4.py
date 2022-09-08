import numpy as np
import matplotlib.pyplot as plt
def x(n):
    #if n < 0:
    #    return 0
    if n >= 0 and n < 6:
        x_dict = {0:1,1:2,2:3,3:4,4:2,5:1}
        return x_dict[n]
    else:
        return 0

def h(n):
    if n < 0:
        return 0

    elif n == 0:
        return 1    #h(0) = 1
        
    elif n == 1:
        return -0.5 #h(1) = -1/2
    else:
        return 5.0 * ((-0.5)**n)
N=14
xn = []
hn = []
n = None
for i in range(0,N):
    xn.append(x(i))
    hn.append(h(i))



def fast_fourier(x, n, X = np.zeros(N),s = 1):
    if n == 1:
        X[0] = x[0]
    else:
        X[int(n/2) - 1] = fast_fourier(x, int(n/2), X,2 * s)
        X[int(n/2)] = fast_fourier(x[s:], int(n/2), X,2 * s)
        for k in range(int(n/2) - 1):
            p = X[k]
            q = np.exp(-1j * 2 * np.pi * k / n) * X[k+int(n/2)]
            X[k] = p + q 
            X[k+n/2] = p - q

    return X

def inv_fast_fourier(X, n, x = np.zeros(N),s = 1):
    if n == 1:
        x[0] = X[0]
    else:
        x[int(n/2) - 1] = fast_fourier(X, int(n/2), x,2 * s)
        x[int(n/2)] = fast_fourier(X[s:], int(n/2), x,2 * s)
        for k in range(int(n/2) - 1):
            p = x[k]
            q = np.exp(+1j * 2 * np.pi * k / n) * X[k+int(n/2)]
            x[k] = p + q 
            x[k+n/2] = p - q

    return x



X = [0]*N
Xo = fast_fourier(xn,N,X,1)
X = np.real(Xo)/N

print("\nRe{X}\n")
print(X)
#plots
plt.stem(range(0,N),X)
plt.title('Filter Output using DFT')
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.grid()
#plt.savefig('Assignment 1/filter/figs/Xkdft.jpg')
plt.show()    

H = [0]*N
Ho = fast_fourier(hn, N)
H = np.real(Ho)/N
print("\nRe{H}\n")
print(X)
#plots
plt.stem(range(0,N),H)
plt.title('Filter Output using DFT')
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.grid()
#plt.savefig('Assignment 1/filter/figs/Xkdft.jpg')
plt.show()    