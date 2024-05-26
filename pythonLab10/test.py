import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Генерация данных
np.random.seed(0)
X_data = np.linspace(-5, 5, 100)
Y_data = 2.0 * X_data + 1.0 + np.random.normal(0, 1, X_data.shape)

# Создание сетки параметров
a = np.linspace(0, 4, 100)
b = np.linspace(-2, 4, 100)
A, B = np.meshgrid(a, b)

# Вычисление MSE для каждого набора параметров
def calculate_mse(A, B, X, Y):
    mse = np.zeros_like(A)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            Y_pred = A[i, j] * X + B[i, j]
            mse[i, j] = np.mean((Y - Y_pred) ** 2)
    return mse

MSE = calculate_mse(A, B, X_data, Y_data)

# Создание фигуры
fig = plt.figure(figsize=(14, 6))

# Первый 3D график
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(A, B, MSE, cmap='viridis')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)
ax1.set_title('MSE Surface')
ax1.set_xlabel('a')
ax1.set_ylabel('b')
ax1.set_zlabel('MSE')

# Второй 3D график с логарифмической осью z
ax2 = fig.add_subplot(122, projection='3d')
# Чтобы логарифмическая шкала работала корректно, добавляем небольшой положительный сдвиг к MSE
MSE_log = np.log10(MSE + 1e-8)  # Добавляем 1e-8 чтобы избежать log(0)
surf2 = ax2.plot_surface(A, B, MSE_log, cmap='viridis')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)
ax2.set_title('MSE Surface (Log Scale)')
ax2.set_xlabel('a')
ax2.set_ylabel('b')
ax2.set_zlabel('log(MSE)')

# Показ графиков
plt.tight_layout()
plt.show()
