import numpy as np
from scipy import fft
from matplotlib import pyplot as plt
import os



ts = 2e-4   # sampling interval
N = 100

def rect_uv(x):
    if np.abs(x) < 0.5:
        return 1
    #elif np.abs(x) == 0.5:
    #    return 0.5
    else:
        return 0


rect = []


t = np.arange(-N, N, ts)  # time vector

xn = np.sinc(t)

Xk_theo = fft.fftshift(fft.fft(xn))
Xk_theo /= np.max(Xk_theo)
Xk_freq = fft.fftshift(fft.fftfreq(len(xn), ts))
for i in t:
    rect.append(rect_uv(i))

plt.plot(t, rect, label='Theoretical')
plt.plot(Xk_freq, np.abs(Xk_theo), 'C1.',label="Calculated")
plt.grid(True, 'both')
plt.xlim(-6, 6)
plt.legend()
plt.xlabel(' f[Hz]')
plt.ylabel('X(f)')
plt.title("Fourier Transform of sinc(x)")
plt.savefig('../figs/e3.10.png')
#plt.show()
#subprocess.run(shlex.split("termux-open ../figs/e3.10.png"))
os.system('xdg-open ../figs/e3.10.pdf')
