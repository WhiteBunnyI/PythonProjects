from random import randint

n = int(input())
goods = ['Карандаш', 'Ручка', "Ластик", "Пенал", "Линейка"]
purchases = [[randint(1, 10), goods[randint(0, len(goods)-1)], randint(1, 5)] for _ in range(n)]

print(purchases)
s = dict()
for id, good, count in purchases:
    if not id in s:
        s[id] = dict()
    s[id][good] = s[id].get(good, 0) + count


for i in s:
    print(i, s[i])

