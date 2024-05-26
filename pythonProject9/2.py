import numpy as np


def RunLengthEncoding(x):
    values = [x[0]]
    counts = []
    count = 0
    for i in x:
        if i != values[-1]:
            values.append(i)
            counts.append(count)
            count = 1
            continue
        count += 1
    counts.append(count)
    return np.array(values), np.array(counts)


x = np.array([2, 2, 2, 2, 3, 3, 3, 5, 22, 10, 0, 2, 2, 2, 4, 2, 2])
print(RunLengthEncoding(x))
