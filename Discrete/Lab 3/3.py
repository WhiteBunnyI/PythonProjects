word = 'aaaaaaaaaaaaadghttttttttyklooooooop'

#print(chr(49))
#exit()
res = str()
count = 1

for i in range(1, len(word)):
    if word[i] == word[i-1]:
        if count < 1:
            res += chr(0) + chr(abs(count))
            res += word[i - 1 + count: i - 1]
            count = 2
            continue
        count += 1
    elif count > 1:
        res += chr(count) + word[i-1]
        count = 1
    else:
        if count == 1:
            count = 0
        count -= 1

    if i == len(word) - 1:
        if count == 1:
            res += chr(0) + chr(1) + word[i]
        elif count > 1:
            res += chr(count) + word[i]
        elif count < 1:
            res += chr(0) + chr(abs(count - 1))
            res += word[i + count: i + 1]

print(res)

for i in res:
    print(ord(i))

print(f'Степень сжатия: {len(res)/len(word)}\nКоэффициент сжатия: {len(word)/len(res)}')