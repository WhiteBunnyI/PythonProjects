def Nod(a, b):
    d = max(a, b)
    f = min(a, b)

    prev_ost = -1
    ost = -1
    koef = []
    while ost != 0:
        prev_ost = ost
        ost = d % f
        koef.append(d // f)
        #print(f'{d} = {f * koef[-1]} + {ost}  ({f} * {koef[-1]})')
        d = f
        f = ost

    return koef, prev_ost

def Evklid(a, b):
    s_prev, s = 1, 0
    t_prev, t = 0, 1
    r_prev, r = a, b

    while r != 0:
        q = r_prev // r
        r_prev, r = r, r_prev - q * r
        s_prev, s = s, s_prev - q * s
        t_prev, t = t, t_prev - q * t

    # r_prev — gcd, s_prev и t_prev — коэффициенты
    return r_prev, s_prev, t_prev


def Chain(koef):
    table = [[-2, 0, 0, 1],
             [-1, 0, 1, 0]]

    for i in koef:
        last = table[-1]
        pre_last = table[-2]
        new = [last[0] + 1, i, i * last[2] + pre_last[2], i * last[3] + pre_last[3]]
        table.append(new)

    sign = (-1) ** (table[-1][0])
    x, y = table[-2][2] * sign, table[-2][3] * sign

    return x, y


a = 43111
b = 54973

#a,b = 157, 131

x, y = Chain(Nod(a, b)[0])

print(f'1 способ: цепные дроби')
print(f'Частное решение: x={x}, y={y}')
print(f'Общее решение: x={x}+{b}t, y={y}+{a}t')
print()

g, x, y = Evklid(a, b)
print(f'2 способ: расширенный алгоритм Евклида')
print(f'Частное решение: x={x}, y={-y}')
print(f'Общее решение: x={x}+{abs(b)}t, y={-y}+{abs(a)}t')

print(f"{a}*{x} + {b}*{y} = {g}")
