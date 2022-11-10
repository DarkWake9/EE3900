import numpy as np

N = np.arange(100)
N = 5*(-(1/2))**N
N[0] = 1
N[1] = -0.5
ans = 4/3
eps = 1e-6
if (abs(np.sum(N) - ans) < eps): print("Limit is verified.")
else: print("Limit is not verified.")
