import numpy as np
from scipy.fft import fft, ifft
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def nlgn(n, a): return a*n*np.log2(n)
def nsq(n, a): return a*(n**2)
def lgn(n, a): return a*np.log2(n);

a = 2**(np.arange(21))
a1 = np.loadtxt('fft.txt', dtype='double')
a2 = np.loadtxt('ifft.txt', dtype='double')
plt.plot(a, a1, 'o')
plt.plot(a, a2, 'o')
b = np.linspace(1, 2**20 + 1, 2**20)
popt, pcov = curve_fit(nlgn, a, a2)
p1 = nlgn(b, *popt)
plt.plot(b, p1)
popt, pcov = curve_fit(nsq, a, a2)
p2 = nsq(b, *popt)
plt.plot(b, p2)
popt, pcov = curve_fit(lgn, a, a2)
p3 = lgn(b, *popt)
plt.plot(b, p3)
#plots
plt.legend(["Simulation (FFT)", "Simulation (IFFT)", "Analysis (n$\log$n)", "Analysis (n$^2$)", "Analysis ($\log$n)"])
plt.xlabel('n')
plt.ylabel('T(n) (ms)')
plt.grid()# minor

#If using termux
plt.savefig('../figs/6_7_1.png')
#subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
#plt.show()
