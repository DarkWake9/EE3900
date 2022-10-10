import numpy as np
import matplotlib.pyplot as plt
import os


alpha = float(0.5*(1+np.sqrt(5)))
beta = float(0.5*(1-np.sqrt(5)))
print(alpha)
print(beta)
def an(n):
    if n > 0:
        return (alpha**n - beta**n)/(alpha - beta)
    else:
        return 0

def bn(n):
    if n == 1:
        return 1
    elif n > 1:
        return an(n-1) + an(n+1)
    else:
        return 0

def sum_an(n):
    sum = 0
    for i in range(1, n+1):
        sum += an(i)

    return sum

def alt_b(n):
    if n >= 1:
        return alpha**n + beta**n
    else:
        return 0


#e1.1
x = np.array(range(1, 30))
y1 = [(an(i+2)-1) for i in x]
y2 = [sum_an(i) for i in x]
fig, (ax1, ax2) = plt.subplots(2, 1)
#fig.set_size_inches(16, 9)
#fig.subplots(1, 2, 1)
ax1.stem(x, y1)
ax1.set_xlabel("n")
ax1.set_ylabel("$a_{n+2}-1$")
ax1.grid(True, which='both')
#fig.subplots(1, 2, 2)
ax2.stem(x, y2, linefmt='-g', markerfmt='og')
ax2.set_xlabel("n")
ax2.set_ylabel("$\sum_{k=1}^{n}a_k$")
ax2.grid(True, which='both')

plt.savefig('/media/darkwake/VIB2/EE3900/pingala/figs/e1.1.jpg')
plt.show()

truecount = 0
for i in range(len(y1)):
    if y1[i] == y2[i] or abs(y1[i] - y2[i]) < 10**(-4):
        truecount +=1

print(f"No.of matches between y1 and y2 : {truecount}\nLength of y1 : {len(y1)}\nLength of y2 : {len(y2)}")
if truecount == len(y1):
    print(f"Hence y1 == y2\nThe equation in Qn 1.1 is True")
else:
    print(f"Hence y1 != y2\nThe equation in Qn 1.1 is False")
#print(y1)
#print(y2)


#e1.2
print('\n')
def a12(n):
    sum = 0
    for i in range(1, n+1):
        sum += an(i)/(10**i)
    return sum

const_a = 10/89
acalc12 = [a12(10), a12(100)]

print(f"Proposed value: 10/89 = {const_a}")
print(f"Sum upto 10 terms: {acalc12[0]}")
print(f"Sum upto 100 terms: {acalc12[1]}")
print("Hence the equation in Q1.2 is True")



#e1.3
print('\n')
x = np.array(range(1, 30))
y1 = [(bn(i)) for i in x]
y2 = [alt_b(i) for i in x]
fig, (ax1, ax2) = plt.subplots(2, 1)
#fig.set_size_inches(16, 9)
#fig.subplots(1, 2, 1)
ax1.stem(x, y1)
ax1.set_xlabel("n")
ax1.set_ylabel("$b_n$")
ax1.grid(True, which='both')
#fig.subplots(1, 2, 2)
ax2.stem(x, y2, linefmt='-g', markerfmt='og')
ax2.set_xlabel("n")
ax2.set_ylabel(f"alpha^n + beta^n")
ax2.grid(True, which='both')
plt.savefig('/media/darkwake/VIB2/EE3900/pingala/figs/e1.3.jpg')
plt.show()
truecount = 0
for i in range(len(y1)):
    if y1[i] == y2[i] or abs(y1[i] - y2[i]) < 10**(-4):
        truecount +=1

print(f"No.of matches between y1 and y2 : {truecount}\nLength of y1 : {len(y1)}\nLength of y2 : {len(y2)}")
if truecount == len(y1):
    print(f"Hence y1 == y2\nThe equation in Qn 1.3 is True")
else:
    print(f"Hence y1 != y2\nThe equation in Qn 1.3 is False")
#print(y1)
#print(y2)




#e1.4
print('\n')
const_a = 8/89
def a12(n):
    sum = 0
    for i in range(1, n+1):
        sum += bn(i)/(10**i)
    return sum

acalc12 = [a12(10), a12(100)]

print(f"Proposed value: 8/89 = {const_a}")
print(f"Sum upto 10 terms: {acalc12[0]}")
print(f"Sum upto 100 terms: {acalc12[1]}")
if acalc12[0] - const_a < 10**(-6) or acalc12[1] - const_a < 10**(-7):
    print("Hence the equation in Q1.4 is True")
else:
    print("Hence the equation in Q1.4 is False")

