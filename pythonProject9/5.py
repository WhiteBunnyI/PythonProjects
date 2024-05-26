import numpy as np
import time
from scipy.stats import multivariate_normal

def Multivariate_normal(X, m, C):
    N, D = X.shape
    diff = X - m

    # Вычисление обратной матрицы и логарифма определителя
    inv_C = np.linalg.inv(C)
    log_det_C = np.log(np.linalg.det(C))

    # Вычисление константы
    const = -0.5 * D * np.log(2 * np.pi) - 0.5 * log_det_C

    # Вычисление логарифма плотности
    log_density = const - 0.5 * np.sum(diff @ inv_C * diff, axis=1)

    return log_density


N = 1000
D = 3
m = np.random.rand(D)
C = np.random.rand(D, D)
print(C)
C = C @ C.T
print(C)

# Генерация случайных точек
X = np.random.multivariate_normal(m, C, N)

start_time = time.time()
log_density_my = Multivariate_normal(X, m, C)
my_duration = time.time() - start_time

start_time = time.time()
log_density_scipy = multivariate_normal(m, C).logpdf(X)
scipy_duration = time.time() - start_time

print("Максимальная абсолютная разница между логарифмами плотностей вероятности:",
      np.max(np.abs(log_density_my - log_density_scipy)))
print(f"Время выполнения моего алгоритма: {my_duration:.8f} сек")
print(f"Время выполнения алгоритма Scipy: {scipy_duration:.8f} сек")

