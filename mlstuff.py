import numpy as np
from matplotlib import pyplot as plt

a = np.linspace(0, np.pi * 2, 100)
b = a * np.exp(-a) - np.tan(a)

plt.plot(a, b)
plt.scatter(a, b, c='r')
plt.show()

c = [n ** 2 - 1 for n in range(0, 100)]

