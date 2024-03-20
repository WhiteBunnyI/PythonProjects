n = int(input("Введите кол-во чисел: "))
lst = [int(input()) for _ in range(n)]
s = set()

for i in lst:
    if not i in s:
        s.add(i)

print(len(s))