def Func(a):                       #Проверяет, состоит ли строка только из нечетных чисел
    for i in range(len(a)):
        if a[i]%2 == 0:
            return False
    return True

n = int(input())
a = [1]
res = [a]
i = 0
while (i < n-1) or not Func(a):         #Генерирует треугольник Паскаля
    b = [1]
    for o in range(len(a)-1):
        b.append(a[o] + a[o+1])
    b.append(1)
    a=b
    res.append(a)
    i += 1

middle = len(res[-1])

for i in range(len(res)):               #Выводим результат в консоль
    l = len(res[i])
    print(' ' * (middle-l), end='')
    for o in range(l):
        if res[i][o]%2:
            print('* ', end='')
        else:
            print('  ', end='')
    print()