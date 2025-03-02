import math

WORD = 'Pentium'
BLOCKS_BITS = 32


def insert(word: str, index: int, value: str):
    return word[:index] + value + word[index:]


def replace(word: str, index: int, value: str):
    return word[:index] + value + word[index + 1:]


def invert_bit(word: str, index: int):
    bit = str(1 - int(word[index]))
    return replace(word, index, bit)


def checkBit(pos, startBitPos):
    bit_controlling_true = startBitPos + 1  # Биты которые нам подходят
    bit_controlling = bit_controlling_true * 2  # Кол-во контролируемых бит
    if pos > startBitPos:
        return int(((pos - startBitPos) % bit_controlling) / bit_controlling_true) == 0


def encode(word, block_bits):
    codes = [ord(c) for c in word]  # ASNI code
    binary = [f'{c:08b}' for c in codes]  # binary code
    binary = ''.join(binary)  # binary string

    blocks = []
    blocks_result = []

    for i in range(1, math.ceil(len(binary) / block_bits) + 1):
        blocks.append(binary[(i - 1) * block_bits: i * block_bits])  # Разбиваем на блоки

    for block in blocks:
        control_bits_count = int(math.log(len(block), 2)) + 1
        control_bits = dict()  # key = startPos, value = bits count, then his bit
        for i in range(control_bits_count):
            pos = 2 ** i - 1
            control_bits[pos] = 0
            block = insert(block, pos, '0')
        for i in range(len(block)):
            for o in control_bits:
                if checkBit(i, o):
                    control_bits[o] += int(block[i])

        for i in control_bits.keys():
            block = replace(block, i, str(control_bits[i] % 2))
        blocks_result.append(block)
        #print(block)

    return ''.join(blocks_result)


def decode(binary, block_bits):
    blocks = []
    blocks_result = []

    control_bits_count = int(math.log(block_bits, 2)) + 1  # Кол-во контрольных битов
    for i in range(1, math.ceil(len(binary) / (block_bits + control_bits_count)) + 1):
        blocks.append(binary[(i - 1) * (block_bits + control_bits_count): i * (block_bits + control_bits_count)])  # Разбиваем на блоки

    #print(blocks)
    for block in blocks:
        control_bits = dict()  # key = startPos, value = bits count, then his bit

        for i in range(control_bits_count):
            control_bits[2 ** i - 1] = 0

        for i in range(len(block)):
            for o in control_bits.keys():
                if checkBit(i, o):
                    control_bits[o] += int(block[i])

        error_pos = -1
        for i, v in control_bits.items():
            if i >= len(block):
                break
            if block[i] != str(int(v) % 2):
                error_pos += i + 1

        if error_pos != -1:
            #error_pos += 2
            block = invert_bit(block, error_pos)
        # print(block)
        print(error_pos)

        res = str()
        for i in range(len(block)):
            if i not in control_bits:
                res += block[i]
        block = res
        res = str()
        for i in range(math.ceil(len(block) / 8)):
            res += chr(int(block[i*8:(i+1)*8], 2))
        blocks_result.append(res)

    return ''.join(blocks_result)


control_bits_count = int(math.log(BLOCKS_BITS, 2)) + 1
# w = encode("habr", 16)
w = encode(WORD, BLOCKS_BITS)
w = invert_bit(w, 4)
w = invert_bit(w, (BLOCKS_BITS + control_bits_count) + 20)
w = decode(w, BLOCKS_BITS)
print(w)
