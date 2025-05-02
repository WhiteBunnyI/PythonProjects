import math

freq = [3, 3, 7, 8, 12, 20, 21, 26]
dl = [5,5,4,4,4,2,2,2]

s = 0
for i in range(len(freq)):
    s += freq[i] / 100 * dl[i]

print(s)