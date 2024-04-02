n = int(input("Введите кол-во чисел: "))
s = set([int(input()) for _ in range(n)])

print(len(s))