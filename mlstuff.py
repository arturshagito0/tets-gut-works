from matplotlib import pyplot as plt

import numpy as np

a = np.linspace(0, np.pi*2, 100)
b = a * np.exp(-a)

c = [n**2 - 1 for n in range(0, 100)]
print(c)


d = np.linspace(0, 10, 10)
e = d ** 2 - 1 + np.cos(d)
plt.scatter(d, e)
plt.show()
