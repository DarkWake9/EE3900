import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
import subprocess
import shlex

A = 12
f = 50
x = lambda t :  A * np.abs(np.sin(2 * np.pi * f * t) )

ts =  1e-4
t = np.arange(-2/f, 2/f, ts)
xn = x(t)
Xk_theo = fft.fft(xn)
fft_freq = fft.fftfreq(len(xn), ts)


