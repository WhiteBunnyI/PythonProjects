def ratio(a):
    if(a[0][0] / a[0][1] == a[1][0] / a[1][1] == a[2][0] / a[2][1]):
        return True
    if(a[0][0] / a[0][2] == a[1][0] / a[1][2] == a[2][0] / a[2][2]):
        return True
    return False

def func(mat):
    if ratio(mat):
        print('Столбцы матрицы линейно зависимые')
    else:
        print('Столбцы матрицы линейно независимые')

    for i in mat:
        print(i)


mat = [
    [10,20,30],
    [40,80,60],
    [70,140,90]
]

mat1 = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]


mat2 = [
    [10,20,30],
    [40,50,120],
    [70,80,210]
]

func(mat)
func(mat1)
func(mat2)

