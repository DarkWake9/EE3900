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
N = 14


X = [0]*N
for k in range(len(X)):
    for n in range(N):
        X[k] += x(n)*np.exp(-1j*2*np.pi * k * n / N)  

X = np.real(X)/N
print("\nRe{X}\n")
print(X)
#plots
plt.stem(range(0,N),X)
plt.title('Filter Output using DFT')
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.grid()
plt.savefig('Assignment 1/filter/figs/Xkdft.jpg')
plt.show()

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
H = [0]*N
for k in range(len(H)):
    for n in range(N):
        H[k] += h(n) * np.exp(-1j*2*np.pi * k * n / N)  

#print(f'X(k) = {X}\nH(k) = {H}')
H = np.real(H)/N
print("\nRe{H}\n")
print(H)
#plots
plt.stem(range(0,N),H)
plt.title('Filter Output using DFT')
plt.xlabel('$k$')
plt.ylabel('$H(k)$')
plt.grid()
plt.savefig('Assignment 1/filter/figs/Hkdft.jpg')
plt.show()