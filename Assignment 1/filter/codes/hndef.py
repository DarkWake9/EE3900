import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if


k = 12
h = np.zeros(k)
h[0] = 1
h[1] = -0.5*h[0]
h[2] = -0.5*h[1] + 1

for n in range(3,k-1):
		h[n] = -0.5*h[n-1]

#subplots
plt.stem(range(0,k),h)
plt.title('Impulse Response Definition')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/hndef.pdf')
subprocess.run(shlex.split("termux-open ../figs/hndef.pdf"))
#else
#plt.show()
