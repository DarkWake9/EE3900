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

def vc0(t):
    if t >= 0:
        return (2/3) * (1 + np.exp(-1.5 * 10**6 * t) )* u(t)
    else:
        return 0



k = np.linspace(1e-10,1e-5,100000)
vvco = [vc0(i) for i in k]

vspice = np.loadtxt('e3.txt')

plt.plot(k,vvco, label = 'Theoretical')
plt.plot(vspice[:,0],vspice[:,1],'.', label = 'Simulation')
plt.ylabel("$V_{C_{0}}(t) (V)$")
plt.xlabel("$t(s)")
plt.grid(True, 'both')
plt.legend()
plt.savefig('../figs/e3.4.pdf')
#plt.show()
os.system('xdg-open ../figs/e3.4.pdf')
