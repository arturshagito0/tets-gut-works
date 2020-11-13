import numpy as np
from matplotlib import pyplot as plt

a = np.linspace(0.1, np.pi * 2, 100)
ys = a * np.log(a)

plt.plot(a, ys)
plt.scatter(a, ys, c='r')
plt.show()

c = [n ** 2 - 1 for n in range(0, 100)]
