import math

d = {'A' : 3,
     'B' : 3,
     'C' : 13,
     'D' : 15,
     'E' : 17,
     'F' : 21,
     'G' : 28}

code = {'A' : '',
        'B' : '',
        'C' : '',
        'D' : '',
        'E' : '',
        'F' : '',
        'G' : ''}

#Находим коды для символов по их частоте
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
print(f'Коды для символов: {code}')
print()

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


word = 'GDEGFCABA'

enc = encode(word, code)
dec = decode(enc, code)
print(enc)
print(dec)

koef = (math.ceil(len(enc) / 8) * 8)/(len(word) * 8)
print(f'Степень сжатия: {koef}\nКоэффициент сжатия: {1 / koef}')
