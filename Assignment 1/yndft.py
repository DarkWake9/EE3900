import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if


N = 16
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(xtemp, (0,N-6), 'constant', constant_values=(0))

X = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		X[k]+=x[n]*np.exp(-1j*2*np.pi*n*k/N)
H = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		H[k]+=h[n]*np.exp(-1j*2*np.pi*n*k/N)

Y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	Y[k] = X[k]*H[k]

y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		y[k]+=Y[n]*np.exp(1j*2*np.pi*n*k/N)

print("X\n")
print(X)
print("\ny\n")
print(y)
X = np.real(X)
plt.stem(range(0,N),X)
plt.title('$X(k)$ with DFT')
plt.xlabel('$n$')
plt.ylabel('$X(k)$')
plt.grid(True, which='both')# minor
plt.savefig("Assignment 1/filter/figs/Xkdft.jpg")
plt.show()
H = np.real(H)
plt.stem(range(0,N),H)
plt.title('$H(k)$ with DFT')
plt.xlabel('$n$')
plt.ylabel('$H(k)$')
plt.grid(True, which='both')# minor
plt.savefig("Assignment 1/filter/figs/Hkdft.jpg")
plt.show()



fig = plt.figure(figsize=(8,6))
plt.subplot(2,1,1)
plt.stem(range(0,N),X)
plt.ylabel('$y(n)$')
plt.grid()
plt.title('X(k) using DFT')

plt.subplot(2,1,2)
plt.stem(range(0,N),H)
plt.xlabel('$k$')
plt.ylabel('$y(n)$')
plt.title('H(k) using DFT')
plt.grid()
plt.savefig('Assignment 1/filter/figs/e6.1DFT.jpg',facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()



Y = np.real(Y)
plt.stem(range(0,N),Y)
plt.title('$Y(k)$ with DFT')
plt.xlabel('$n$')
plt.ylabel('$Y(k)$')
plt.grid(True, which='both')# minor
plt.savefig("Assignment 1/filter/figs/Ykdft.jpg")
plt.show()

y = np.real(y)/N
print("\nRe{y}\n")
print(y)
#plots
plt.stem(range(0,N),y)
plt.title('Filter Output using DFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#
#If using termux
#plt.savefig('../figs/yndft.pdf')
#subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
plt.savefig('Assignment 1/fig/yndft.jpg')
plt.show()
