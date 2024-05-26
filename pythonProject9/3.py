import numpy as np

n = 10
m = 4
data = np.random.normal(size=n * m).reshape((n, m))
print(f'Минимальный элемент: {data.min()}')
print(f'Максимальный элемент: {data.max()}')
print(f'Среднее значение: {data.mean()}')
print(f'Стандартное отклонение: {data.std()}')
save = data[0:5, :]
print(data)
print()
print(save)