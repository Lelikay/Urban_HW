def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


print('давайте создадовать матрицы')
while True:
    n = int(input('введите кол-во строк: '))
    m = int(input('введите кол-во столбцов: '))
    value = int(input('введите значение: '))
    result = get_matrix(n, m, value)
    print(result)
