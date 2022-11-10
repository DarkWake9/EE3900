import numpy as np
from matplotlib import pyplot as plt
import os
from scipy import signal

os.system('cat e5.3b.cir | ngspice')
A = np.loadtxt('e5.3b.txt')
plt.plot(A[:,0], A[:,1], '-.', markersize = 2)
plt.xlabel("t")
plt.ylabel("V")
plt.title("$V_{out}$ of Butterworth filter")
plt.grid(True)
plt.savefig('../figs/e5.3b.pdf')
os.system('xdg-open ../figs/e5.3b.pdf')
