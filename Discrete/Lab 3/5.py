import math

def IsEqual(a: float, b: float) -> bool:
    return math.isclose(a, b, rel_tol=REL_TOL)

def GetRange(index: chr):
    current_range = (0, 0)
    for i in d:
        current_range = (current_range[1], current_range[1] + d[i])
        if i == index:
            break

    return current_range

def CalculateRange(range, index: chr):
    abs_range = GetRange(index)
    #print(range, abs_range)
    return (range[0] + (range[1] - range[0]) * abs_range[0], range[0] + (range[1] - range[0]) * abs_range[1])

def CalculateWord(f: float):
    ks = list(d.keys())
    abs_range = (0, 1)
    result = str()
    while not IsEqual(f, ((abs_range[0] + abs_range[1]) / 2.0)):
        for i in ks:
            current_range = CalculateRange(abs_range, i)
            if current_range[0] < f < current_range[1]:
                abs_range = current_range
                result += i
                #print(result, i, f, ((abs_range[0] + abs_range[1]) / 2.0))
                break
    return result


def convertToBin(f: float):
    result = ''
    while True:
        f *= 2
        zeloe = int(f)
        result += str(zeloe)
        if IsEqual(f, 1.0):
            break
        #print(f)
        f -= zeloe

    return result

def convertToFloat(b: str):
    decimal = 0
    for i, bit in enumerate(b, 1):
        decimal += int(bit) * (2 ** -i)
        #print(decimal, i, bit)
    return decimal



d = {
    'a': 0.20,
    'b': 0.10,
    'c': 0.05,
    'd': 0.45,
    'e': 0.10,
    'f': 0.10,
}

# d = {
#     'N': 0.250,
#     'P': 0.375,
#     'M': 0.250,
#     'E': 0.125,
# }

word = 'aecdfb'
#word = 'NPPPNMME'

REL_TOL = 10**-min(3, (len(word) - 1))

print(f'Исходное слово: {word}')
result = (0, 1)
for i in word:
    result = CalculateRange(result, i)
    #print(result)
result = (result[1] + result[0]) / 2
print(result)
result = convertToBin(result)
print(f'Закодированно в: {result}')

bytes = (len(result) / 8.0)
print(f'Степень сжатия: {bytes/len(word)}\nКоэффициент сжатия: {len(word)/bytes}')

result = convertToFloat(result)
#print(result)
print(f'Расшифрованное  слово: {CalculateWord(result)}')
