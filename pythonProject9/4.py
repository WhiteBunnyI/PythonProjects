import numpy as np


x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
elem = np.where(x == 0)[0]
index = np.where(elem != x.size)[0]
elem = elem[0:index[-1]]                        #Индекс нулевых эл-ов в x, причем если нуль в конце вектора x, то он не включается
print(max(list(map(lambda y: x[y+1], elem))))