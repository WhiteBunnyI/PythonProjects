import math

WORD = 'Pentium'
BLOCKS_BITS = 32

def encode(word, block_bits):

    def checkBit(pos, startBitPos):
        bit_contolling = 2**(startBitPos + 1) #Кол-во контролируемых бит
        bit_contolling_true = bit_contolling / 2 #Биты которые нам подходят
        if pos >= startBitPos:
            return (((pos - startBitPos) % bit_contolling) / bit_contolling_true) == 0


    codes = [ord(c) for c in word]                  #ASNI code
    binary = [f'{c:08b}' for c in codes]            #binary code
    binary = ''.join(binary)                        #binary string

    blocks = []
    blocks_result = []

    сontrol_bits_count = int(math.log(block_bits, 2)) + 1 #Кол-во контрольных битов

    for i in range(1, math.ceil(len(binary) / block_bits) + 1):
        blocks.append(binary[(i - 1) * block_bits : i * block_bits])    #Разбиваем на блоки

    #print(blocks)

    for block in blocks:
        control_bits = dict()            #key = startPos, value = bits count, then his bit

        for i in range(сontrol_bits_count):
            control_bits[2**i - 1] = 0

        for i in range(len(block)):
            for o in control_bits:
                if checkBit(i, o):
                    control_bits[o] += int(block[i])
        print(control_bits)
        print(block)
        print()

        result = str()
        pos = 0
        for i in range(len(block)):
            if i in control_bits.keys():
                result += str(control_bits[i] % 2)
            else:
                result += block[pos]
        #01010000011001010110111001110100
        #110110100
        #11100101000100110010101101011001110100
        blocks_result.append(block)
        print(block)
        print()
        print()
        #print(controlBits)


#encode("habr", 16)
encode(WORD, BLOCKS_BITS)