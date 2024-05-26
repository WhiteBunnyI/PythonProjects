import numpy as np

filename = '1.txt'

with open(filename, 'r') as file:
    raw = [i.replace('\n', '') for i in file]
    data = list()
    for i in raw:
        data.append(list(map(int, i.split(','))))
    data = np.array(data, dtype=np.int32)
    #print(data)

print(f'Сумма всех элементов: {data.sum()}')
print(f'Максимальный элемент: {data.max()}')
print(f'Минимальный элемент: {data.min()}')
