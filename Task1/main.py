
def task3():
    n = int(input())
    ots = ''
    for i in range(n):
        s = ""

        for o in range(n - i, 0, -1):
            s += str(o)
        for o in range(2, n+1-i):
            s += str(o)
        print(ots + s)

        num = n-i
        c = 0
        while num > 0:
            num //= 10
            c += 1

        ots += ' ' * c


def task2():
    n = int(input())

    for i in range(n):
        s = ""
        for o in range(1, n - i + 1):
            s += str(o)
        print(s)


def task1():
    a = int(input())
    b = int(input())
    c = int(input())
    _max, _min = 0, 0
    if a > b:
        _max = a
        _min = b
    else:
        _max = b
        _min = a

    if _max < c:
        _max = c
    elif _min > c:
        _min = c
    print(f'max: {_max} min: {_min}')


if __name__ == '__main__':
    task2()
