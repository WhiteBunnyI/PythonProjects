word = 'aaaaaaaaaaaaadghttttttttttttyiklooooooop'

res = str()
count = 1
for i in range(1, len(word)):
    if word[i] == word[i-1]:
        if count < 1:
            res += '0' + str(abs(count))
            res += word[i - 1 + count: i - 1]
            count = 1
            continue
        count += 1
    elif count > 1:
        res += str(count) + word[i-1]
        count = 1
    else:
        if count == 1:
            count = 0
        count -= 1




print(res)