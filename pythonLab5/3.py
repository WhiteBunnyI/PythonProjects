fileInput = 'input3.txt'
fileOut = 'output3.txt'
with open(fileInput, mode='r', encoding='UTF8') as file:
    data = file.readlines()
    out = []
    for i in data:
        i = i.split()
        out.append([i[0] + ' ' + i[1], i[2]])
    out = sorted(out, key=lambda x:x[1])
with open(fileOut, mode='w', encoding='UTF8') as file:
    file.write(out[0][0] + ' ' + out[0][1] + '\n')
    file.write(out[-1][0] + ' ' + out[-1][1])