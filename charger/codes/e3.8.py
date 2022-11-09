import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
import os

A = 12
f0 = 50
x = lambda t :  A * np.abs(np.sin(2 * np.pi * f0 * t) )

ts =  1e-4  # sampling interval
t = np.arange(-2/f0, 2/f0, ts)
fs = np.arange(-10*f0, 10*f0, f0/2)
xn = x(t)

Xk_theo = (fft.fft(xn))
fft_freq = fft.fftfreq(xn.size, d=ts)

def coeff_calc(k):#Fourier coeff of a|sin(2pi*f0*t)|
    global A
    return 2 * A /(np.pi * (1 - 4*k**2))

def XKfft_calc(f):#Fourier transformed fn of a|sin(2pi*f0*t)|
    if np.abs(f)%(2*f0)==0:
        return 800*coeff_calc(f/(2*f0))
    else:
        return 0
xk_cal = []

for i in fs:
    #xk_cal.append([[i, i],[0, XK_calc(i)]])
    xk_cal.append(XKfft_calc(i))

stm = plt.stem(fs,np.abs(xk_cal), 'C1', label='Calculated')
plt.setp(stm[0],  markersize = 3.5)
plt.plot(fft_freq, np.abs(Xk_theo), 'C2x', label='Theroetical')
plt.xlim(-10*f0, 10*f0)
plt.xlabel('f')
plt.ylabel('X(f)')
plt.legend()
plt.grid(True, 'both')
plt.title("Fourier Transform of x(t) = $A |sin(2 \pi f t)|$")
plt.savefig('../figs/e3.8.pdf')
#plt.show()
os.system('xdg-open ../figs/e3.8.pdf')
#subprocess.run(shlex.split("termux-open ../figs/e2.3.pdf"))<F5>
