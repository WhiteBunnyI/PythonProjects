from config import filename

def file_read(filename):
    letters = dict()
    pairs = dict()
    with open(filename, 'r', encoding='utf-8') as file:
        line = 1
        while line:
            line = file.readline()
            for char in line:
                if char not in letters:
                    letters[char] = 1
                else:
                    letters[char] += 1
            for ind in range(1, len(line)):
                pair = line[ind-1:ind+1]
                if pair not in pairs:
                    pairs[pair] = 1
                else:
                    pairs[pair] += 1
    return letters, pairs


def print_info(dick):
    t = 0
    for key in dick.keys():
        print(f'{key}: {dick[key]}', end='\t')
        t += 1
        if t > 8:
            print()
            t = 0


if __name__ == '__main__':
    letters, pairs = file_read(filename)
    print_info(letters)
    print('\n-------------------------------------------\n')
    print_info(pairs)