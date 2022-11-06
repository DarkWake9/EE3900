import os
import numpy as np
from matplotlib import pyplot as plt


#def H(s):
    #return (1/(s * 1e-6 + 3)

s = np.linspace(0,10000000, 10000)
H = 1/((2 * s * 1e-6) + 3)
plt.plot(s, H)
plt.ylabel("$H(s)$")
plt.xlabel("$s$")
plt.grid(True, 'both')
plt.savefig('../figs/e4.3.pdf')
#plt.show()
os.system('xdg-open ../figs/e4.3.pdf')
