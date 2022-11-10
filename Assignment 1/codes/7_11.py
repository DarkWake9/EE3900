import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt
#If using termux
#import subprocess
#import shlex
#end if

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
dftmtx = fft(np.eye(len(x)))
X = x@dftmtx
print(X)
