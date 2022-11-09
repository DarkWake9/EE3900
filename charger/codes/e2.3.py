import numpy as np
import matplotlib.pyplot as plt
import os

A = 12
f = 50
x = lambda t : A * np.abs( np.sin(2 * np.pi * f * t) )
N = 1000
t = np.linspace(0, 4/f, N)


B = np.ones(N) + 1j*np.zeros(N)

def acc_cos(k):
    global B
    acc = (np.exp(-1j*2*np.pi*f*k*t) + np.exp(1j*2*np.pi*f*k*t))/(1 - k**2)
    B += acc

acc_vec = np.vectorize(acc_cos, otypes=['double'])
K = np.linspace(2, 100, 50)
acc_vec(K)
plt.plot(t, x(t), label='Theoretical - From $1.1$')
plt.plot(t, 2*A*B/np.pi, '.', label='Calculated - From $2.3$')
plt.legend()
plt.grid(True, which='both')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.savefig('../figs/e2.3.pdf')
#plt.show()
os.system('xdg-open ../figs/e2.3.pdf')
