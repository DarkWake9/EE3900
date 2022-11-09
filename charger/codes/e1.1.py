import numpy as np
import matplotlib.pyplot as plt
import os

A = 12
f = 50
def x(t, A0 = 12, f0 = 50):
    return A0 * np.abs(np.sin(2 * np.pi * f0 * t))
t = np.linspace(0, 2/f, 1000)
plt.plot(t, x(t, A, f))
plt.grid(True, 'both')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.savefig("../figs/e1.1.pdf")
os.system('xdg-open ../figs/e1.1.pdf')

