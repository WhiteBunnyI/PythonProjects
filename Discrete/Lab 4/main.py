filename = 'text.txt'

freq = dict()
with open(filename, mode='r') as file:
   for i in file:
       if i != '\n':
           freq[i] += 1