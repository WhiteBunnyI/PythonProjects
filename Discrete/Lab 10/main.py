def nod(a: int, b: int):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


def is_int(a):
    s = str(a).split('.')
    if len(s) > 1:
        s = s[1]
        if len(s) == 1 and s == '0':
            return True
    return False


for x in range(-10**10, 10**10):
    y = (43111 * x - 1) / 54973
    if is_int(y):
        print(f'x: {x}, y: {y}')

print(nod(54973, 43111))

# y = (43111x - 1) / 54973
# x = (54973 + 1)*x