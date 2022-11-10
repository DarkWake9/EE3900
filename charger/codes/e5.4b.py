import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import signal

os.system('cat e5.4b.cir | ngspice')
A = np.loadtxt('e5.4b.txt')
plt.plot(A[:,0], A[:,1], '-.', markersize = 2)
plt.xlabel("t")
plt.ylabel("V")
plt.title("$V_{out}$ of Chebyshev filter")
plt.grid(True)
plt.savefig('../figs/e5.4b.pdf')
os.system('xdg-open ../figs/e5.4b.pdf')
