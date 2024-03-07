#a = input()
a = 'YYYYYYYYYYYYYYYYYggkeeeAAABVVVVVVVVVVVVVVVVVVV'
o = ""
_char = a[0]
count = 0
p = 0
while p < len(a) or count > 0:
    if p < len(a) and _char == a[p]:
        count += 1
    else:
        o += _char
        if count > 1:
            o += str(count)
        if p >= len(a):
            break
        _char = a[p]
        count = 1
    p += 1


print(o)

out = ''
_char = ''
count = 0
for i in range(len(o)):
    if o[i].isdigit():
        count *= 10
        count += int(o[i])
        continue

    if _char != '':
        out += _char + _char * (count-1)
    _char = o[i]
    count = 0

out += _char + _char * (count-1)
print(out)
