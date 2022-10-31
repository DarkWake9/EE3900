import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if



x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
k = 20
y = np.zeros(20)


y[0] = x[0]
y[1] = -0.5*y[0]+x[1]

for n in range(2,k-1):
	if n < 6:
		y[n] = -0.5*y[n-1]+x[n]+x[n-2]
	elif n > 5 and n < 8:
		y[n] = -0.5*y[n-1]+x[n-2]
	else:
		y[n] = -0.5*y[n-1]
print(y)

#subplots
plt.subplot(2, 1, 1)
plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()# minor


plt.subplot(2, 1, 2)
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/xnyn.pdf')
plt.savefig('../figs/xnyn.eps')
subprocess.run(shlex.split("termux-open ../figs/xnyn.pdf"))
#else
#plt.show()
