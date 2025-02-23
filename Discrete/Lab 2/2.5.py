MAX_X = 20
MAX_Y = 17


def f1():
    t = [[0 for _ in range(MAX_Y)] for _ in range(MAX_X)]

    #t[MAX_X - 1][MAX_Y - 1] = 1
    # просчитать через динамическое программирование
    for x in range(MAX_X):
        for y in range(MAX_Y):
            if x == 0 and y == 0:
                t[x][y] = 1
                continue
            step_x, step_y = 0, 0
            if x - 1 >= 0:
                step_x = t[x - 1][y]
            if y - 1 >= 0:
                step_y = t[x][y - 1]
            t[x][y] = step_y + step_x

    for i in t:
        print(i)

    print(t[MAX_X-1][MAX_Y-1])


def f2(x, y):
    if x > MAX_X or y > MAX_Y:
        return 0
    if x == MAX_X and y == MAX_Y:
        return 1
    return f2(x + 1, y + 1) + f2(x + 1, y)


print(f1())
print(f2(0, 0))
