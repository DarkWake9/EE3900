import numpy as np
from scipy import fft, signal
from matplotlib import pyplot as plt
import os


def rect_uv(x):
    if np.abs(x) < 0.5:
        return 1
    elif np.abs(x) == 0.5:
        return 0.5
    else:
        return 0

#rect = np.vectorize(rect_uv, otypes=['double'])
rect = []
for i in np.linspace(-1, 1, 1000):
    rect.append(rect_uv(i))

    
fft_rect = (fft.fft(rect))
fft_freq = fft.fftfreq(len(fft_rect), 0.001)


plt.plot(fft_freq, fft_rect/max(fft_rect), "C1")
plt.plot(fft_freq, np.sinc(fft_freq))
plt.grid(True, 'both')
#plt.xlim(-40, 40)
plt.legend
plt.show()
