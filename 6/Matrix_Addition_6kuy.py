"""Matrix_Addition_6kuy"""


# Write a __function that accepts two square matrices (N x N two dimensional arrays), and return the sum of the two. Both
# matrices being passed into the __function will be of size N x N (square), containing only integers.
# How to sum two matrices:
# Take each cell [n][m] from the first matrix, and add it with the same [n][m] cell from the second matrix.
# This will be cell [n][m] of the solution matrix.
#
# Visualization:
# |1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
# |3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
# |1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|

# Напишите функцию, которая принимает две квадратные матрицы (N x N двумерных массивов) и возвращает их сумму.
# Обе матрицы, передаваемые в функцию, будут иметь размер N x N (квадрат), содержащий только целые числа.
# Как суммировать две матрицы:
# Возьмите каждую ячейку [n][m] из первой Матрицы и добавьте ее с той же ячейкой [n] [m] из второй Матрицы.
# Это будет ячейка [n][m] матрицы решения.

def matrix_addition(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


test_list_1 = [[j + i * 3 for j in range(1, 4)] for i in range(3)]

for i in range(3):
    for j in range(3):
        print(test_list_1[i][j], end=' ')
    print()

print(matrix_addition(test_list_1, test_list_1))

# чужой код
# def matrix_addition(a, b):
#     return [[sum(xs) for xs in zip(ra, rb)] for ra, rb in zip(a, b)]

# def matrix_addition(a, b):
#     return [[y1[i]+x2 for i, x2 in enumerate(x1)] for x1, y1 in zip(a, b)]