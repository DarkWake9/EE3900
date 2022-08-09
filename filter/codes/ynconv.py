import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if



n = np.arange(14)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

nh=len(h)
x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
nx = len(x)

y = np.zeros(nx+nh-1)

for k in range(0,nx+nh-1):
	for n in range(0,nx):
		if k-n >= 0 and k-n < nh:
			y[k]+=x[n]*h[k-n]

print(y)
#plots
plt.stem(range(0,nx+nh-1),y)
plt.title('Filter Output using Convolution')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/ynconv.pdf')
plt.savefig('../figs/ynconv.eps')
subprocess.run(shlex.split("termux-open ../figs/ynconv.pdf"))
#else
#plt.show()
