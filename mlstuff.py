from matplotlib import pyplot as plt

import numpy as np

a = np.linspace(0, np.pi*2, 100)
b = a * np.exp(-a)

plt.plot(a,b)
plt.show()

