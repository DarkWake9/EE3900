import numpy as np

#defining h(n) as shown in 5.6
def h(n):
    if n < 0:
        return 0

    elif n == 0:
        return 1    #h(0) = 1
        
    elif n == 1:
        return -0.5 #h(1) = -1/2
    else:
        return 5.0 * ((-0.5)**n)

sum = [0,0,0]
for n in range(1000000):
    sum[0] += h(n)

sum[1] = sum[0]
for n in range(1000000,10000000):
    sum[1] += h(n)


print(f'SUM UPTO n = 1000000: {sum[0]}\nSUM UPTO n = 10000000: {sum[1]}')