import numpy as np
import matplotlib.pyplot as plt
#If using termux
#import subprocess
#import shlex
#end if

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
y=np.loadtxt('y.txt', dtype='double')
k = 20

#subplots
plt.subplot(2, 1, 1)
plt.stem(range(0,6),x)
plt.ylabel('$x(n)$')
plt.grid()# minor

plt.subplot(2, 1, 2)
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/3_2.png')
#subprocess.run(shlex.split("termux-open ../figs/xnyn.pdf"))
#else
#plt.show()
