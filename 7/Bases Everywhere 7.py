"""Bases Everywhere 7"""
# Uh oh, Someone at the office has dropped all these sequences on the floor and forgotten to label them with their
# correct bases. We have to fix this before the boss gets back or we're all going to be fired!
# This is what your years of coding have been leading up to, now is your time to shine! Task
# You will have to create a __function which takes in a sequence of numbers in random order and you will have to return
# the correct base of those numbers. The base is the number of unique digits. For example, a base 10 number can have 10
# unique digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 and a base 2 number (Binary) can have 2 unique digits: 0 and 1.
#
# Constraints
# The sequence will always be 10 numbers long and we know that the base is going to be between 2 and 10 inclusive
# so no need to worry about any letters. When sorted, the sequence is made up of consecutive numbers.
#
# Задача
# Вам нужно будет создать функцию, которая принимает последовательность чисел в случайный порядок и вы должны будете
# вернуть правильную базу этих чисел. База - это количество уникальных цифр. Например, базовое число 10 может иметь 10
# уникальных цифр: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 а базовое число 2 (двоичное) может иметь 2 уникальные цифры: 0 и 1.
# # Ограничения
# Последовательность всегда будет состоять из 10 чисел, и мы знаем, что база будет между 2 и 10 включительно,
# так что не нужно беспокоиться ни о каких буквах. При сортировке последовательность состоит из последовательных чисел.
# Examples

# [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]     -->  10
# [ "1", "2", "3", "4", "5", "6", "10", "11", "12", "13" ]  -->   7

# лучшее решение, решил очень быстро
def base_finder(seq):
    return len(set(''.join(seq)))
#
seq = [ "1", "2", "3", "4", "5", "6", "10", "11", "12", "13" ]

print(base_finder(seq))