import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создание данных
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = (X**2 + Y**2) / 2

fig = plt.figure(figsize=(14, 6))

# Первый график - обычная ось z
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('MSE с обычной осью z')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Второй график - ось z в логарифмическом масштабе
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_zscale('log')
ax2.set_title('MSE с осью z в логарифмическом масштабе')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z (log scale)')

plt.tight_layout()
plt.show()
