import math


def encode(word, code):
    res = ''
    for i in word:
        res += code[i]
    return res


def decode(word, code):
    res = ''
    temp = ''
    for i in word:
        temp += i
        if temp in code.values():
            res += list(code.keys())[list(code.values()).index(temp)]
            temp = ''
    return res


d = {'A': 3,
     'B': 3,
     'C': 13,
     'D': 15,
     'E': 17,
     'F': 21,
     'G': 28}

code = {'A': '',
        'B': '',
        'C': '',
        'D': '',
        'E': '',
        'F': '',
        'G': ''}

# Находим коды для символов по их частоте
res = list(d.items())
while len(res) != 1:
    print(res)
    n = res[2:]
    n.append((res[0][0] + res[1][0], res[0][1] + res[1][1]))
    for i in res[0][0]:
        code[i] += '1'
    for i in res[1][0]:
        code[i] += '0'
    n = sorted(n, key=lambda x: x[1])
    res = n
print(res)

for i in code:
    code[i] = code[i][::-1]



word = 'GDEGFGFCGFGABGFGFAGGG'

enc = encode(word, code)
dec = decode(enc, code)

bits_evenly = math.ceil(math.log2(len(code.keys())))

bits_haffman = 0
freq_sum_1 = 0
freq_sum_2 = 0
for i in code:
    frequency = len(code[i]) * d[i]
    freq_sum_1 += d[i]
    freq_sum_2 += frequency

bits_haffman = freq_sum_2 / freq_sum_1
koef = bits_evenly / bits_haffman

print()
print(f'Коды для символов: {code}')
print()
print(f'Закодированное слово: {enc}')
print(f'Декодированное слово: {dec}')
print()
print(f'Коэффициент сжатия: {koef}')
print(f'Степень сжатия: {1/koef}')
