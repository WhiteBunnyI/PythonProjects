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

def huffman_pairs(letters):
    #Подготавливаем данные
    letters = list(letters.items())
    letters = sorted(letters, key=lambda x: x[1])
    print(letters)
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
        k = 0
        for i in range(2, len(letters[0][0]) + 1, 2):
            pooo = letters[0][0][k:i]
            code[pooo] += '1'
            k = i
        k = 0
        for i in range(2, len(letters[0][0]) + 1, 2):
            pooo = letters[0][0][k:i]
            code[pooo] += '0'
            k = i
        letters = n

    for i in code:
        code[i] = code[i][::-1]
        
    with open(filename, "r") as f:
        text = f.readlines()
    
    print(code)
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

if __name__ == "__main__":
    with open(filename, "r") as f:
        text = f.readlines()

    text = "".join(text)
    
    letters, pairs = task1.file_read(filename)
    huffman_pairs(pairs)
    exit()
    bits_enc, freq_shenon, freq_haffman, code = huffman(letters)
    bits_evenly = (len(text)) * 6
    print("Посимвольно:")
    print(f'Кол-во бит с равномерными кодами: {bits_evenly}')
    print(f'Кол-во бит закодированного текста: {bits_enc}')
    print(f'Шеннон: {freq_shenon:.2f}')
    print(f'Хаффман: {freq_haffman:.2f}')
    print(f'{freq_haffman:.2f} > {freq_shenon:.2f} - код не достигает теоритического минимума')
    print()
    print(code)
    
    print("Пары:")
    bits_enc, freq_shenon, freq_haffman, code = huffman(pairs)
    bits_evenly = (len(text)) * 6
    
    print(f'Кол-во бит с равномерными кодами: {bits_evenly}')
    print(f'Кол-во бит закодированного текста: {bits_enc}')
    print(f'Шеннон: {freq_shenon:.2f}')
    print(f'Хаффман: {freq_haffman:.2f}')
    print(f'{freq_haffman:.2f} > {freq_shenon:.2f} - код не достигает теоритического минимума')
    print()
    print(code)