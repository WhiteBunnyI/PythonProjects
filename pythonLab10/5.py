import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создание данных
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

# Функция для вычисления MSE
def mse(actual, predicted):
    return np.mean((actual - predicted)**2)

# Вычисление MSE для каждой точки сетки
mse_values = np.zeros_like(x)
for i in range(len(x)):
    for j in range(len(y)):
        mse_values[i, j] = mse(z[i, j], np.sin(x[i, j]) + np.cos(y[i, j]))

fig = plt.figure(figsize=(12, 6))

# Первый график
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, mse_values, cmap='viridis')
ax1.set_title('График MSE')

# Второй график
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x, y, mse_values, cmap='plasma')
ax2.set_title('График MSE(log)')
ax2.set_zscale('log')

plt.show()
