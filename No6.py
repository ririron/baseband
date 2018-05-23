import numpy as np
import random
#import matplotlib.pyplot as plt


#def SingleNRZ():

a = np.array([]);
random.seed(1)
for i in range(1024):
    a = np.append(a, random.randint(0, 1))

print a
