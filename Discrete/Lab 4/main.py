filename = 'text.txt'

freq = set()
with open(filename, mode='r') as file:
   for i in file.readlines():
       for j in i:
           if j != '\n':
               freq.add(j)

freq = sorted(freq)

# Находим коды для символов по их частоте
res = list(d.items())
while len(res) != 1:
    print(res)
    n = res[2:]
    n.append((res[0][0] + res[1][0], res[0][1] + res[1][1]))
    for i in res[0][0]:
        code[i] += '1'
    for i in res[1][0]:
        code[i] += '0'
    n = sorted(n, key=lambda x: x[1])
    res = n
print(res)

for i in code:
    code[i] = code[i][::-1]