import numpy as np
from scipy import fft
from matplotlib import pyplot as plt
import os



def rect_uv(x):
    if np.abs(x) < 0.5:
        return 1
    #elif np.abs(x) == 0.5:
    #    return 0.5
    else:
        return 0

N = 100 # limits
ts = 0.02   # sampling interval

rect = []
for i in np.arange(-N, N, ts):
    rect.append(rect_uv(i))


fft_rect = fft.fftshift(fft.fft(rect))
fft_freq = fft.fftshift(fft.fftfreq(len(rect), ts))

#plt.plot(np.linspace(-10, 10, 1000), rect)
plt.plot(fft_freq, np.abs(fft_rect)/max(np.abs(fft_rect)), 'C1-*',label="Calculated")
plt.plot(fft_freq, np.abs(np.sinc(fft_freq)), label='Theoretical')
plt.grid(True, 'both')
plt.xlim(-6, 6)
plt.legend()
plt.title("Fourier Transform of rect(x)")
plt.savefig('../figs/e3.9.pdf')
os.system('xdg-open ../figs/e3.9.pdf')
