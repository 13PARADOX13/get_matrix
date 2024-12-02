def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

get_matrix(3, 4, 7)
get_matrix(2, 2, 1)
