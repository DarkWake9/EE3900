import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if


x1 = np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(x1,(0,5),'constant')
a=np.array([1.0,0.5])
b=np.array([1.0,0.0,1.0])
y = signal.lfilter(b, a, x)
k = x.shape[0]

#subplots
plt.subplot(2, 1, 1)
plt.stem(range(0,k),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()# minor


plt.subplot(2, 1, 2)
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/xnynfilt.pdf')
plt.savefig('../figs/xnynfilt.eps')
subprocess.run(shlex.split("termux-open ../figs/xnynfilt.pdf"))
#else
#plt.show()
