fileInput = 'input2.txt'
fileOut = 'output2.txt'
with open(fileInput, mode='r') as file:
    data = [int(i) for i in file.readlines()]

with open(fileOut, mode='w') as file:
    file.writelines(str(i)+'\n' for i in sorted(data))
