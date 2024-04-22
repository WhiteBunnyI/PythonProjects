import csv
import os
import random

class CSVReader:
    m_data = list()
    def __init__(self, filename):
        with open(filename, 'r') as file:
            _reader = csv.reader(file)
            for row in _reader:
                self.m_data.append(row)

    def Show(self, typeOut="top", count=5, separator=','):
        _iter = (self.m_data[n] for n in range(1, len(self.m_data)))
        if typeOut == 'bottom':
            _iter = (self.m_data[n] for n in range(len(self.m_data)-1, 0, -1))
        if typeOut == 'random':
            _iter = (i for i in random.sample(self.m_data[1:], count))

        print(' '.join(self.m_data[0]))
        for row in range(count):
            print(separator.join(next(_iter)))


    def Info(self):
        row = len(self.m_data)-1
        column = len(self.m_data[0])
        print(f'{row}x{column}')
        _max = max([len(field) for field in self.m_data[0]])
        for field in range(column):
            non_empty = sum(1 for i in self.m_data[1:] if i[field])
            field_type = type(self.m_data[1][field]).__name__
            print(f'{self.m_data[0][field] + ' '*(_max-len(self.m_data[0][field]))}\t{non_empty}\t{field_type}')

    def DelNan(self):
        self.m_data = [row for row in self.m_data if all(row)]

    def MakeDS(self):
        learning = random.sample(self.m_data[1:], int(0.7*(len(self.m_data)-1)))
        testing = [row for row in self.m_data[1:] if row not in learning]

        os.makedirs('workdata/learning', exist_ok=True)
        os.makedirs('workdata/testing', exist_ok=True)

        with open('workdata/learning/train.csv', mode='w') as file:
            output = [','.join(row) for row in learning]
            for i in range(len(output)):
                file.write(f"{output[i]}\n")

        with open('workdata/testing/test.csv', mode='w') as file:
            output = [','.join(row) for row in testing]
            for i in range(len(output)):
                file.write(f"{output[i]}\n")


reader = CSVReader("Titanic.csv")
reader.Show()
reader.Show(typeOut="bottom")
reader.Show(typeOut="random")
reader.Info()
reader.DelNan()
reader.Info()
reader.MakeDS()
