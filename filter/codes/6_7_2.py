import numpy as np
from scipy.fft import fft, ifft
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def nlgn(n, a): return a*n*np.log2(n)
def nsq(n, a): return a*n*n
def lgn(n, a): return a*np.log2(n)

x = np.linspace(10, 1001, 100)
a = np.loadtxt('conv.txt', dtype='double')
plt.plot(x, a, '.')
popt, pcov = curve_fit(nlgn, x, a)
p1 = nlgn(x, *popt)
plt.plot(np.insert(x, 0, 0), np.insert(p1, 0, 0))
popt, pcov = curve_fit(nsq, x, a)
p2 = nsq(x, *popt)
plt.plot(np.insert(x, 0, 0), np.insert(p2, 0, 0))
popt, pcov = curve_fit(lgn, x, a)
p3 = lgn(x, *popt)
plt.plot(np.insert(x, 0, 0), np.insert(p3, 0, 0))
plt.xlabel('n')
plt.ylabel('T(n) (s)')
plt.legend(["Simulation (convolution)", "Analysis (n$\log$n)", "Analysis (n$^2$)", "Analysis ($\log$n)"])
plt.grid()# minor

#If using termux
plt.savefig('../figs/6_7_2.png')
#subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
#plt.show()
