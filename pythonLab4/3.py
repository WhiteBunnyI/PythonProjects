n = int(input("Введите кол-во названных городов: "))


def func(n):
    s = set()
    for _ in range(n):
        i = input()
        if not i in s:
            s.add(i)
        else:
            return "REPEAT"

    return "OK"


print(func(n))
