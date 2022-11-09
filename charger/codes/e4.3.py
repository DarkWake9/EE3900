import numpy as np
from matplotlib import pyplot as plt
import os

A0 = 12
V0 = 5
f0 = 50
N = 100000

t = np.linspace(-N, N, N)

h = lambda t : np.pi * V0 * f0 * np.sinc(2*f0*t) / A0

x = lambda t : A0 * np.abs( np.sin(2 * np.pi * f0 * t))

y = np.convolve(x(t), h(t), mode='same')

plt.plot(t, y)
plt.grid(True, 'both')
plt.xlabel('t')
plt.ylabel('V')
plt.savefig('../figs/e4.3.pdf')
#plt.show()
os.system('xdg-open ../figs/e4.3.pdf')



#subprocess.run(shlex.split("termux-open ../figs/e4.3.pdf"))
