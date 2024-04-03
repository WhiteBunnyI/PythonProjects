fileInput = 'input1.txt'
fileOut = 'output1.txt'
with open(fileInput, mode='r') as file:
    data = file.read().split()
    out = 1
    for i in data:
        out *= int(i)

with open(fileOut, mode='w') as file:
    file.write(str(out))