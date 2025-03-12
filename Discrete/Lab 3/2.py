import itertools


def distance(a, b):
    dist = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dist += 1
    return dist

def dict_test(dict, minLen):
    for i in range(len(dict)):
        k1 = list(dict.keys())[i]
        for o in range(i+1, len(dict)):
            k2 = list(dict.keys())[o]
            dist = distance(dict[k1], dict[k2])
            if dist < minLen:
                print(f'\'{k1}\' и', f'\'{k2}\'', 'имеют расстояние:', dist)

def check_error(code, d):
    if code not in d.values():
        print(f'В коде ошибка!')
        return True
    else:
        print(f'В коде нет ошибки')
        return False


def find_error(code, d: dict, minLen):
    if code not in d.values():
        keys = [list(d.keys())[0]]
        minDist = distance(code, d[keys[0]])
        for i in range(1, len(d)):
            k = list(d.keys())[i]
            dist = distance(code, d[k])
            if dist < minDist:
                keys.clear()
                keys.append(k)
                minDist = dist
            elif dist == minDist:
                keys.append(k)
        print(f'Ближайший коды: {keys}, расстояние: {minDist}')
        return
    print(f'В двоичном коде не требуется исправление ошибки')

def test(d, code, min_len):
    dict_test(d, min_len)

    if check_error(code, d):
        find_error(code, d, min_len)

def getCodes(min_len, count):
    for i in range(3, 10):
        codes = list(map(''.join, list(itertools.product('01', repeat=i))))
        res = [codes[0]]
        for o in range(1, len(codes)):
            b = True
            for p in res:
                if codes[o] not in res and distance(p, codes[o]) < min_len:
                    b = False
            if b:
                res.append(codes[o])
        if len(res) >= count:
            return res

#print(getCodes(3, 8))

d = {'и': '0000',
     'к': '0011',
     'л': '0101',
     'м': '0110',
     'н': '1001',
     'о': '1010',
     'п': '1100',
     'р': '1111'}

test(d, '0001', 2)

d = {'и': '000000',
     'к': '000111',
     'л': '011001',
     'м': '011110',
     'н': '101010',
     'о': '101101',
     'п': '110011',
     'р': '110100'}

#test(d, '110100', 3)
test(d, '000101', 3)

