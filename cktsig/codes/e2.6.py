import numpy as np
from matplotlib import pyplot as plt
import os

os.system('cat e2.cir | ngspice')
def unitstep(t):
    if (t < 0): return 0
    elif (t == 0):return 0.5
    else: return 1

def v1(t):
    if (t >= 0): return 4/3*(1 - np.exp(-t*1.5e6))*unitstep(t)
    else: return 0

vc0 = np.vectorize(v1, otypes=['double'])
vc1 = np.loadtxt('e2.txt')
t = np.linspace(0, 1e-5, 1000000)

vc0 = np.vectorize(v1, otypes=['double'])
vc1 = np.loadtxt('e2.txt')
t = np.linspace(0, 1e-5, 1000000)
plt.plot(t, vc0(t), label='Theoretical')
plt.plot(vc1[:,0], vc1[:,1], '.', label='Simulated')
plt.xlabel('t (s)')
plt.ylabel('$v_{C_0}(t)$ (V)')
plt.grid(True, 'both')
plt.legend()
plt.savefig("../figs/e2.6.pdf")
#plt.show()
os.system('xdg-open ../figs/e2.6.pdf')


