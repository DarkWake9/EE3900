from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
import subprocess
import shlex

A = 12
f = 50
x = lambda t :  A * np.abs(np.sin(2 * np.pi * f * t) )

extra_scale_factor_why_required = 400

def X_obs(k):
    xk = extra_scale_factor_why_required * 4 * A / (np.pi * (1 - 4 * k**2))
    return [f*k, np.abs(xk)]

ts =  1e-4
t = np.arange(-2/f, 2/f, ts)
xn = x(t)
Xk = fft.fft(xn)
fft_freq = fft.fftfreq(len(xn), ts)

ff_xaxis = [-4, -2, 0, 2, 4]

Xobs = [X_obs(i) for i in ff_xaxis]

plt.figure()
plt.plot(fft_freq, np.abs(Xk), 'C0.',label='Calculated')
for i in Xobs:
    plt.plot([i[0], i[0]],[0, i[1]],'C1')
plt.xlim(-10*f, 10*f)
plt.grid(True, 'both')
plt.legend(['Calculated', 'Observed'])
plt.show()

#subprocess.run(shlex.split("termux-open ../figs/e1.1.pdf"))
