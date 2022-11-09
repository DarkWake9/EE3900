import numpy as np
import matplotlib.pyplot as plt
import os

global tau
tau = 2e-6 / 3
T = 1e-7
def vn(n):
    if n > 0:
        p = 2 * tau / T
        pn = ((p - 1)/(p + 1))**n
        temp = 1 - p*pn/(1 + p)
        return 2*temp/3
    else:
        return 0
R1 = 1
R2 = 2
C0 = 1e-6
V2 = 2


n = np.arange(0, 101, 1)
t =  np.linspace(0, 1e-5, 101)
c=1e-6

def v2(n,vi):
    a = (4*C0/T -3)/(4*C0/T +3)
    b=4/(4*C0/T +3)
    if len(vi)==0: vi.append(0)
    else:
        vi.append(a*vi[-1]+b)
n2 = np.arange(1,101)/1e7

vi=[]
for i in n2:
    v2(i,vi)
        
vn_disc_theo = [vn(i) for i in n]
vt_cont_theo =  2*(1 - np.exp(-1.5e6*t))/3
#vdiff = [v(i) for i in n]
#print(vd)
v_simu = np.loadtxt('e4.txt')
#plt.plot(t, vd, 'C0*')
plt.plot(n2, vi, 'C2.')
#plt.plot()
plt.plot(t, vt_cont_theo, 'b')
plt.plot(t, vn_disc_theo, 'r-.', markersize=5)
plt.plot(v_simu[:,0], v_simu[:,1], 'C1x')
plt.xlabel('t')
plt.ylabel('V')
plt.legend(['Difference  equation','Theory (continuous)', 'Theory (discrete)', 'Simulation (ngspice)'])
plt.savefig("../figs/e4.7.pdf")
#plt.show()
os.system('xdg-open ../figs/e4.7.pdf')
