import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

A = 12
f = 50
x = lambda t = A * np.abs(np.sin(2 * np.pi * f * t))
    
t = np.linspace(0, 2/f, 1000)
plt.plot(t, x(t, A, f)*)
plt.grid(True, 'both')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.savefig("../figs/e1.1.pdf")
#subprocess.run(shlex.split("termux-open ../figs/e1.1.pdf"))
plt.show()

