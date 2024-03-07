a = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']

d = {}

for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in d:
    print(d[i])