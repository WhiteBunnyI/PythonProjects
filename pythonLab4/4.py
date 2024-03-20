def func(str):
    s = dict()
    for i in str:
        count = s.get(i, 0)
        yield count
        s[i] = count + 1


#s = input().split()
s = 'one two one two three'.split()
a = func(s)
for _ in range(len(s)):
    print(next(a))


