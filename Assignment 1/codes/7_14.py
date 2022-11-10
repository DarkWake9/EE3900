import numpy as np
import scipy
from scipy import fft
from itertools import chain
import timeit
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

def nlgn(n, a): return a*n*np.log2(n)
def nsq(n, a): return a*n*n
def lgn(n, a): return a*np.log2(n);

def pmtx(n):
    col = range(n)
    row = list(chain(range(0, n, 2), range(1, n, 2)))
    data = np.ones(n)
    return scipy.sparse.csr_matrix((data, (row, col)), shape = (n,n))

def id_diag(n):
    w = np.exp(-1j*2*np.pi/n)**(np.arange(n//2))
    Id = scipy.sparse.identity(n//2)
    D = scipy.sparse.dia_matrix((w, [0]), shape=(n//2,n//2))
    return scipy.sparse.bmat([[Id, D], [Id, -D]])


def fftmtx(n):
    if (n == 1): return scipy.sparse.csr_matrix(([1]*1, ([0], [0])), shape=(1,1))
    P = pmtx(n)
    G = fftmtx(n//2)
    M = scipy.sparse.bmat([[G, None], [None, G]])
    L = id_diag(n)
    return L.dot(M).dot(P)

t1 = []
N = 11
x = 1<<np.arange(N)
X = np.arange(2**(N-1)+1)
x_t = np.linspace(10,1001,100)
eps = 1e-6
for i in range(0, N, 1):
    v = np.random.random(size=1<<i)
    st = timeit.default_timer()
    K = fftmtx(1<<i).dot(v)
    en = timeit.default_timer()
    t1.append(1000*(en - st))

t2 = np.loadtxt('fftw.txt')
t3 = np.loadtxt('conv.txt')
t4 = np.loadtxt('dft.txt')
t5 = np.loadtxt('dftmtx.txt')
plt.plot(x_t, t2, '.')
popt, pcov = curve_fit(nlgn, x_t, t2)
p1 = nlgn(X, *popt)
plt.plot(X, p1)
plt.plot(x_t, t3, '.')
popt, pcov = curve_fit(nsq, x_t, t3)
p1 = nsq(X, *popt)
plt.plot(X, p1)
plt.plot(x_t, t4, '.')
popt, pcov = curve_fit(nsq, x_t, t4)
p1 = nsq(X, *popt)
plt.plot(X, p1)
plt.plot(x_t, t5, '.')
popt, pcov = curve_fit(nsq, x_t, t5)
p1 = nsq(X, *popt)
plt.plot(X, p1)
plt.plot(x, t1, '.')
#plt.legend(['Simulation (FFT)', 'Analysis (FFT/$O$(n$\log$n))', 'Simulation (Convolution)', 'Analysis (Convolution/$O$(n$^2$))', 'Simulation (DFT)', 'Analysis (DFT/$O$(n$^2$))', 'Simulation (DFT Matrix)', 'Analysis (DFT Matrix/$O$(n$^2$))'])
plt.legend(['Simulation (FFT)', 'Analysis (FFT/$O$(n$\log$n))', 'Simulation (Convolution)', 'Analysis (Convolution/$O$(n$^2$))', 'Simulation (DFT)', 'Analysis (DFT/$O$(n$^2$))', 'Simulation (DFT Matrix)', 'Analysis (DFT Matrix/$O$(n$^2$))', 'Comparison (DFT Matrix/Python)'])
#plt.legend(['Simulation (FFT)', 'Analysis (FFT/$O$(n$\log$n))', 'Simulation (Convolution)', 'Analysis (Convolution/$O$(n$^2$))', 'Simulation (DFT Matrix)', 'Analysis (DFT Matrix/$O$(n$^2$))'])
plt.xlabel('n')
plt.ylabel('T(n) (ms)')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/complexity.png')
