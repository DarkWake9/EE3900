import numpy as np
import matplotlib.pyplot as plt

k = 20
fx = np.loadtxt("Assignment 1/x.dat")
fy = np.loadtxt("Assignment 1/y.dat")

print(fx)
print(fy)

plt.subplot(2, 1, 1)
plt.stem(range(0,6),fx)
plt.title('Digital Filter Input-Output\nFrom .dat files written from e3-3.c')
plt.ylabel('$x(n)$')
plt.grid()# minor


plt.subplot(2, 1, 2)
plt.stem(range(0,k),fy)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
#plt.savefig('../figs/xnyn.pdf')
#plt.savefig('../figs/xnyn.eps')
#subprocess.run(shlex.split("termux-open ../figs/xnyn.pdf"))
#else
plt.savefig('Assignment 1/fig/xnyn.jpg')
plt.show()
