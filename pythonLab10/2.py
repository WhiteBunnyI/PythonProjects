import numpy as np
import matplotlib.pyplot as plt

def f(a, b):
    t = np.linspace(-2*np.pi, 2*np.pi, 600)
    x = np.sin(a * t)
    y = np.sin(b * t)
    return x, y


freq = [(3, 2), (3, 4), (5, 4), (5, 6)]

plt.figure(figsize=(12, 8))

for i in range(len(freq)):
    x, y = f(freq[i][0], freq[i][1])
    plt.subplot(2, 2, i+1)
    plt.plot(x, y)
    plt.title(f"{freq[i][0]}:{freq[i][1]}")


plt.suptitle("Фигуры Лиссажу")
plt.show()