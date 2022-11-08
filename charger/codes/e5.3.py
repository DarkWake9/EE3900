import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import signal

os.system('cat e5.3.cir | ngspice')
A = np.loadtxt('e5.3.txt')
n = 5
fc = 60
b, a = signal.butter(n, fc, analog=True)
f, h = signal.freqs(b, a)
plt.plot(A[:,0], A[:,1], '.')
plt.semilogx(f, 20*np.log10(np.abs(h)) - 6)
plt.xlabel("f (Hz)")
plt.ylabel("V")
plt.grid(True)
plt.legend(['Simulation', 'Analysis'])
plt.savefig('../figs/e5.3.pdf')
os.system('xdg-open ../figs/e5.3.pdf')








