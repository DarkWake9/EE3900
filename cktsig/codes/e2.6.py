import os
import numpy as np
from matplotlib import pyplot as plt


def u(t):
    if t < 0: 
        return 0

    elif t == 0:
        return 0.5
    
    else: 
        return 1

vc0 = lambda t: (4/3) * 1 - np.exp(-1.5 * 10**6 * t) * u(t)
vco_spice = np.loadtxt('e2.txt')
k = np.linspace(1e-14,1e-5,100000, len(vco_spice))
t = np.linspace(1e-14,1e-5,100000, len(vco_spice))
vvco = [vc0(i) for i in t]
plt.figure(figsize=(5.4,4))
plt.plot(k,vvco, label='Theoretical')
plt.plot(vco_spice[:,0],vco_spice[:,1],'.', label='Simulated')
plt.xlabel("$t(s)$'")
plt.ylabel("$V_{C_{0}}(t) (V)$'")
plt.legend()
plt.grid(True, 'both')
plt.savefig("../figs/e2.6.pdf")
#plt.show()
os.system('xdg-open ../figs/e2.6.pdf')
