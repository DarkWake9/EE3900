import numpy as np
import matplotlib.pyplot as plt
import os

global tau
tau = 2e-6 / 3
T = 1e-7
def vn(n):
    temp = 2 * tau * (((2*tau - T)/(2*tau + T)) ** n) /((2*tau + T)*3)
    return 2/3 - temp
R1 = 1
R2 = 2
C0 = 1e-6
V2 = 2
n = np.arange(1e-9, 101, 1)
t =  np.linspace(0, 1e-5, 101)
vn_disc_theo = vn(n)
vt_cont_theo =  2*(1 - np.exp(-1e6*t))/3
v_simu = np.loadtxt('e4.txt')
plt.plot(t, vt_cont_theo, 'b')
plt.plot(t, vn_disc_theo, 'r.', markersize=1.75)
plt.plot(v_simu[:,0], v_simu[:,1], 'C1-.')
plt.xlabel('t')
plt.ylabel('V')
plt.legend(['Theory (continuous)', 'Theory (discrete)', 'Simulation (ngspice)'])
plt.savefig("../figs/e4.7.pdf")
os.system('xdg-open ../figs/e4.7.pdf')
