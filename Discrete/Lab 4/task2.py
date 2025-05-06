from config import filename
import task1
import math


def huffman(letters):
    #Подготавливаем данные
    letters = list(letters.items())
    letters = sorted(letters, key=lambda x: x[1])

    letters_copy = {}
    code = {}
    for i in letters:
        code[i[0]] = ""
        letters_copy[i[0]] = i[1]

    #Составляем коды Хаффмана
    while len(letters) != 1:
        n = letters[2:]
        n.append((letters[0][0] + letters[1][0], letters[0][1] + letters[1][1]))
        n = sorted(n, key=lambda x: x[1])
        for i in letters[0][0]:
            code[i] += '1'
        for i in letters[1][0]:
            code[i] += '0'
        letters = n

    for i in code:
        code[i] = code[i][::-1]
        
    with open(filename, "r") as f:
        text = f.readlines()

    #Кодируем текст по Хаффману
    text = "".join(text)
    encoded = ""
    for i in text:
        encoded += code[i]

    #Считаем биты
    bits_enc = len(encoded)

    #считаем кол-во информации
    freq_all = sum(letters_copy.values())
    freq_shenon = 0
    freq_haffman = 0

    for i in code:
        p = letters_copy[i] / freq_all
        freq_shenon -= p * math.log2(p)
        freq_haffman += p * len(code[i])

    return bits_enc, freq_shenon, freq_haffman, code

def huffman_pairs(pairs, sep='*'):
    pairs = list(pairs.items())
    pairs = sorted(pairs, key=lambda x: x[1])

    code = {}
    pairs_copy = {}
    for i in pairs:
        code[i[0]] = ""
        pairs_copy[i[0]] = i[1]

    while len(pairs) != 1:
        a, b = pairs[0], pairs[1]
        c = (f'{a[0]}{sep}{b[0]}', a[1] + b[1])
        pairs = pairs[2:]
        pairs.append(c)
        pairs = sorted(pairs, key=lambda x: x[1])

        for i in a[0].split(sep):
            code[i] += '1'
        for i in b[0].split(sep):
            code[i] += '0'

    for i in code:
        code[i] = code[i][::-1]

    #print(f'{len(pairs_copy)}: {pairs_copy}')
    #print(f'{len(code)}: {code}')

    with open(filename, "r") as f:
        text = f.readlines()

    text = "".join(text)
    encoded = ""
    for i in range(2, len(text), 2):
        chr = text[i-2:i]
        chr = chr.replace('\n', ' ')
        if chr not in code:
            print(f'{i}: {chr}')
        encoded += code[chr]

    # Считаем биты
    bits_enc = len(encoded)

    # считаем кол-во информации
    freq_all = sum(pairs_copy.values())
    freq_shenon = 0
    freq_haffman = 0

    for i in code:
        p = pairs_copy[i] / freq_all
        freq_shenon -= p * math.log2(p)
        freq_haffman += p * len(code[i])

    return bits_enc, freq_shenon, freq_haffman, code

if __name__ == "__main__":
    with open(filename, "r") as f:
        text = f.readlines()

    text = "".join(text)
    
    letters, pairs = task1.file_read(filename)

    bits_enc, freq_shenon, freq_haffman, code = huffman(letters)
    bits_evenly = (len(text)) * 6
    print("Посимвольно:")
    print(code)
    print(f'Кол-во бит с равномерными кодами: {bits_evenly}')
    print(f'Кол-во бит закодированного текста: {bits_enc}')
    print(f'Шеннон: {freq_shenon:.2f}')
    print(f'Хаффман: {freq_haffman:.2f}')
    print(f'{freq_haffman:.2f} > {freq_shenon:.2f} - код не достигает теоритического минимума')
    print()
    

    bits_enc, freq_shenon, freq_haffman, code = huffman_pairs(pairs)
    bits_evenly = (len(text)) * 6

    print("Пары:")
    print(code)
    print(f'Кол-во бит с равномерными кодами: {bits_evenly}')
    print(f'Кол-во бит закодированного текста: {bits_enc}')
    print(f'Шеннон: {freq_shenon:.2f}')
    print(f'Хаффман: {freq_haffman:.2f}')
    print(f'{freq_haffman:.2f} > {freq_shenon:.2f} - код не достигает теоритического минимума')
