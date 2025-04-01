import math


def countDecimalAfterDot(f: float):
    f = str(f)
    a = f.split('.')
    b = f.split('e-')
    if len(b) > 1:
        return int(b[1])
    if len(a) == 1:
        return 0
    return len(a[1])


def SumFloat(f1: float, f2: float):
    c1 = countDecimalAfterDot(f1)
    c2 = countDecimalAfterDot(f2)
    c = c1 + c2
    return round(f1 + f2, c)


def MulFloat(f1: float, f2: float):
    c1 = countDecimalAfterDot(f1)
    c2 = countDecimalAfterDot(f2)
    c = c1 + c2
    return round(f1 * f2, c)


def GetRange(index: chr):
    current_range = (0, 0)
    for i in d:
        current_range = (current_range[1], SumFloat(current_range[1], d[i]))
        if i == index:
            break

    return current_range


def CalculateRange(range, index: chr):
    abs_range = GetRange(index)
    # print(range, abs_range)
    l = SumFloat(range[1], -range[0])
    l = MulFloat(l, abs_range[0])
    l = SumFloat(l, range[0])

    r = SumFloat(range[1], -range[0])
    r = MulFloat(r, abs_range[1])
    r = SumFloat(r, range[0])
    return (l, r)


def CalculateWord(f: float):
    ks = list(d.keys())
    abs_range = (0, 1)
    result = str()
    while f != SumFloat(abs_range[0], abs_range[1]) / 2:
        for i in ks:
            current_range = CalculateRange(abs_range, i)
            if current_range[0] < f < current_range[1]:
                abs_range = current_range
                result += i
                #print(result, i, f, SumFloat(abs_range[0], abs_range[1]) / 2)
                break
        else:
            break
    return result


def convertToBin(f: float, accuracy: int = 0):
    result = ''
    for _ in range(accuracy):
        f = MulFloat(f, 2)
        zeloe = int(f)
        result += str(zeloe)
        if f == 1.0:
            break
        # print(f)
        f = SumFloat(f, -zeloe)

    return result


def countZeroAfterDot(f: float):
    f = str(f)
    a = f.split('.')
    b = f.split('e-')
    if len(b) > 1:
        return int(b[1])

    if len(a) == 1:
        return 0

    for i in range(len(a[1])):
        if a[1][i] != '0':
            return i
    return 0


def convertToBit(f: float):
    result = ''
    accuracy = countDecimalAfterDot(f) + 1

    e = 0.5
    while countZeroAfterDot(e) != accuracy:
        #print(countZeroAfterDot(e), e)
        if f >= e:
            result += '1'
            f -= e
        else:
            result += '0'
        e = MulFloat(e, 0.5)
    return result


def convertToFloat(b: str):
    decimal = 0
    for i, bit in enumerate(b, 1):
        decimal += int(bit) * (2 ** -i)
        # print(decimal, i, bit)
    return decimal


def truncate(number, decimals=0):
    factor = 10 ** decimals
    return math.trunc(number * factor) / factor


d = {
    'a': 0.10,
    'b': 0.10,
    'c': 0.05,
    'd': 0.55,
    'e': 0.10,
    'f': 0.10,
}

# d = {
#     'N': 0.250,
#     'P': 0.375,
#     'M': 0.250,
#     'E': 0.125,
# }

# Рассчет сжатия и коэффициента
dictCount = len(d.keys())
bitsEvenly = math.ceil(math.log2(dictCount)) * dictCount

s = 0
for k in d.keys():
    s += d[k] * math.log2(d[k])
s = -s

koef = s / bitsEvenly

print(f'Степень сжатия: {koef}\nКоэффициент сжатия: {1 / koef}')

word = 'aecdfb'
# word = 'NPPPNMME'

print(f'Исходное слово: {word}')
result = (0, 1)
for i in word:
    result = CalculateRange(result, i)
    # print(result)
result = SumFloat(result[1], result[0]) / 2
print(result)
accuracy = countDecimalAfterDot(result)
print(f'Accuracy: {accuracy}')
result = convertToBit(result)
print(f'Закодированно в: {result}')


bytes = (len(result) / 8.0)
bytesEvenly = len(word) * 8
koef = bytes / bytesEvenly
result = convertToFloat(result)
print(f'Декодированно в: {result}')
result = truncate(result, accuracy)
print(f'truncate: {result}')
print(f'{math.}')
print(f'Расшифрованное  слово: {CalculateWord(result)}')
print()
# Мааа гад булщит а не лаба