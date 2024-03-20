s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}

s1_1 = {1, 2, 3, 4, 5, 6, 7}
s2_1 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}

s1_2 = {1, 10, 223, 413, 2}
s2_2 = {1, 10, 223, 413, 2}

s1_3 = {1, 2, 3}
s2_3 = {1, 4, 5}

s1_4 = {1, 2}
s2_4 = {1, 4, 5}
def func(s1, s2):
    return s1.issubset(s2)
    # if len(s1) >= len(s2):
    #     return False
    # for i in s1:
    #     if not i in s2:
    #         return False
    # return True

print(func(s1, s2))
print(func(s1_1, s2_1))
print(func(s1_2, s2_2))
print(func(s1_3, s2_3))
print(func(s1_4, s2_4))