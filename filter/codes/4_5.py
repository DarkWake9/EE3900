import numpy as np
import matplotlib.pyplot as plt
#if using termux
#import subprocess
#import shlex
#end if

#DTFT
def H(z):
	num = np.polyval([1,0,1],z**(-1))
	den = np.polyval([0.5,1],z**(-1))
	H = num/den
	return H
		
#Input and Output
omega = np.linspace(-3*np.pi,3*np.pi,100)

#subplots
plt.plot(omega, abs(H(np.exp(1j*omega))))
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})| $')
plt.grid()# minor

#if using termux
plt.savefig('../figs/4_5.png')
#subprocess.run(shlex.split("termux-open ../figs/dtft.pdf"))
#else
#plt.show()
