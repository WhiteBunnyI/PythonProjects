import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 400)
plt.title('Полиномы Лежандра')

for n in range(1, 8):
    y = legendre(n)(x)
    plt.plot(x, y, label=f'n = {n}')

plt.legend()
plt.show()

