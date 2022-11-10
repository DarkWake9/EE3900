import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import convolution_matrix as cm
#If using termux
#import subprocess
#import shlex
#end if

n = np.arange(14)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

nh=len(h)
x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
nx = len(x)
th = cm(h,nx,mode='full')
y = th@x
print(y)

#plots
plt.stem(range(0,nx+nh-1),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/5_5.png')
#subprocess.run(shlex.split("termux-open ../figs/ynconv.pdf"))
#else
#plt.show()
