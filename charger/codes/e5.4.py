import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import signal

os.system('cat e5.4.cir | ngspice')
A = np.loadtxt('e5.4.txt')
n = 4
fc = 60
rp = 0.5
b, a = signal.cheby1(n, rp, fc, analog=True)
f, h = signal.freqs(b, a)
plt.plot(A[:,0], A[:,1], '.')
plt.semilogx(f, 19*np.log10(np.abs(h)) - 4)
plt.xlabel("f (Hz)")
plt.ylabel("V")
plt.grid(True)
plt.legend(['Simulation', 'Analysis'])
plt.savefig('../figs/e5.4.pdf')
os.system('xdg-open ../figs/e5.4.pdf')
