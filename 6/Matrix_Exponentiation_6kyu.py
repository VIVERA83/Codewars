"""Matrix_Exponentiation_6kyu.py"""
# Your task in this kata is to write a __function which will take matrix and integer as an input: eg. calc(matrix, n)
# and would return a matrix raised to the power of n. Be ready to handle big n.
# A =          [[1, 2], [1, 0]]
# calc(A, 2) = [[3, 2], [1, 2]]

# Ваша задача в этом ката состоит в том, чтобы написать функцию, которая будет принимать матрицу и целое число
# в качестве входных данных: например, calc(matrix, n) и вернет матрицу, возведенную в степень n.
# Будьте готовы справиться с большими числами.


def calc(matrix, n):
    def getMultiplyArray(array_one: list, array_two: list) -> list:
        res_array = []
        for key, string in enumerate(array_one):
            res_array.append([])
            for column in zip(*array_two):
                new_value_cell = 0
                for index in range(len(string)):
                    new_value_cell += string[index] * column[index]
                res_array[key].append(new_value_cell)
        return res_array

    res_matrix = matrix
    for _ in range(1, n // 2):
        res_matrix = getMultiplyArray(res_matrix, matrix)
    res_matrix = getMultiplyArray(res_matrix, res_matrix)
    if n % 2:
        res_matrix = getMultiplyArray(res_matrix, matrix)
    return res_matrix


lst = [[1, 2], [3, 4]]
n = 3
print(calc(lst, n))

# # чужой код
# Вроде как мое решение не самое короткое но покрайне мере его можно хоть как то понять.

# class Matrix(list):
#     def __matmul__(self, other):
#         return Matrix([[sum(map(int.__mul__, row, col)) for col in zip(*other)] for row in self])
#
#     def __pow__(self, n):
#         X, I = Matrix(self), Matrix([[i == j for i in range(len(self))] for j in range(len(self))])
#         while n:
#             if n % 2: I @= X
#             X @= X; n >>= 1
#         return I
#
# calc = Matrix.__pow__

