import numpy as np
import random
import matplotlib.pyplot as plt


def SingleNRZ(a, conv):
    return conv - a

def MultiNRZ(a, conv):
    return conv - 2*a +1

N = 1024
t = np.arange(0, N)
a = np.array([])
conv = np.zeros(N)
random.seed(1)
for i in range(N):
    a = np.append(a, random.randint(0, 1))
print a

conv = SingleNRZ(a, conv)
print conv

F = np.fft.fft(conv)
F=np.abs(F)**2

plt.subplot(2, 1, 1)
plt.title('origin')
plt.ylim(-1.2, 1.2)
plt.xlim(0, N)
plt.bar(t, conv, align = "center")


plt.subplot(2, 1, 2)
plt.plot(t, F)

plt.show()
