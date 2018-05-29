import numpy as np
import random
import matplotlib.pylab as plt


def scale(a):
    b = np.array([])
    t = np.array([])
    for i in range(N):
        if a[i] == 1:
            b = np.append(b, 0)
            b = np.append(b, -1)
            b = np.append(b, -1)
            b = np.append(b, 0)
        else :
            b = np.append(b, 0)
            b = np.append(b, 1)
            b = np.append(b, 1)
            b = np.append(b, 0)
        t = np.append(t, i)
        t = np.append(t, i)
        t = np.append(t, i)
        t = np.append(t, i)
    return b, t



N = 1024
t = np.arange(0, N)
a = np.array([])

random.seed(1)
for i in range(N):
    a = np.append(a, random.randint(0, 1))
print a

conv, t2 = scale(a)

print conv

F = np.fft.fft(conv)
F=np.abs(F)**2

plt.subplot(2, 1, 1)
plt.title('origin')
plt.ylim(-1.2, 1.2)
plt.xlim(0, N)
plt.bar(t2, conv, align = "center")


plt.subplot(2, 1, 2)
plt.plot(t2, F)

plt.show()
