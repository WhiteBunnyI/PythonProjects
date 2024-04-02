n = int(input("Введите кол-во названных городов: "))


def func(n):
    s = set()
    for _ in range(n):
        i = input()
        if i in s:
            return "REPEAT"
        s.add(i)
    return "OK"


print(func(n))
