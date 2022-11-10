import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt
#If using termux
#import subprocess
#import shlex
#end if

def myfft(n, x):
    if (n == 1): return x
    g = myfft(n/2, x[0::2])
    g1 = np.copy(g)
    h = myfft(n/2, x[1::2])
    h1 = np.copy(h)
    g = np.concatenate((g, g1))
    h = np.concatenate((h, h1))
    w = np.exp(-1j*2*np.pi*np.arange(n)/n)
    return g + h*w

def myifft(n, x):
    if (n == 1): return x
    g = myifft(n/2, x[0::2])
    g1 = np.copy(g)
    h = myifft(n/2, x[1::2])
    h1 = np.copy(h)
    g = np.concatenate((g, g1))
    h = np.concatenate((h, h1))
    w = np.exp(1j*2*np.pi*np.arange(n)/n)
    return (g + h*w)/2

N = 14
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(xtemp, (0,10), 'constant', constant_values=(0))

X = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		X[k]+=x[n]*np.exp(-1j*2*np.pi*n*k/N)
H = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		H[k]+=h[n]*np.exp(-1j*2*np.pi*n*k/N)

Y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	Y[k] = X[k]*H[k]

y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		y[k]+=Y[n]*np.exp(1j*2*np.pi*n*k/N)

#print(X)
y = np.real(y)/N
y_prev = np.loadtxt('y.txt', dtype='double')

#plots
plt.stem(range(0,N),y,markerfmt='C0o')
plt.stem(range(0,N),y_prev[:14],markerfmt='C1o')

X_fft = fft(x)
H_fft = fft(h)
Y_fft = H_fft*X_fft
y_ifft = ifft(Y_fft).real

X_own = myfft(16, x)
H_own = myfft(16, h)
Y_own = X_own*H_own
y_own = myifft(16, Y_own)

#plots
plt.stem(range(0,14),y_ifft[:14],markerfmt='C2o')
plt.stem(range(0,14),y_own[:14],markerfmt='C3o')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
plt.legend(['From IDFT', 'From difference equation', 'From IFFT', 'From own implementation'])

#If using termux
plt.savefig('../figs/6_6.png')
#subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
#plt.show()

