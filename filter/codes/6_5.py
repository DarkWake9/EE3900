import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt
#If using termux
#import subprocess
#import shlex
#end if

N = 14
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0,0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0,0))
h = hn1+hn2
xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(xtemp, (0,10), 'constant', constant_values=(0))
dftmtx = fft(np.eye(len(x)))
X = x@dftmtx
H = h@dftmtx
Y = H*X
invmtx = np.linalg.inv(dftmtx)
y = (Y@invmtx).real
#plots
plt.stem(range(0,16),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/6_5.png')
#subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
#plt.show()
