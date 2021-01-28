"""Simple Fun 135: Missing Alphabet 6"""


# Task
# Given string s, which contains only letters from a to z in lowercase.# A set of alphabet is given
# by abcdefghijklmnopqrstuvwxyz. 2 sets of alphabets mean 2 or more alphabets.  Your task is to find the missing
# letter(s). You may need to output them by the order a-z. It is possible that there is more than one missing letter
# from more than one set of alphabet. If the string contains all of the letters in the alphabet, return an empty string ""
#
# Example
# For s='abcdefghijklmnopqrstuvwxy'
# The result should be 'z'
# For s='aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy'
# The result should be 'zz'
# For s='abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy'
# The result should be 'ayzz'
# For s='codewars'
# The result should be 'bfghijklmnpqtuvxyz'
# Input/Output
# [input] string s
# Given string(s) contains one or more set of alphabets in lowercase.
# [output] a string
# Find the letters contained in each alphabet but not in the string(s). Output them by the order a-z.
# If missing alphabet is repeated, please repeat them like "bbccdd", not "bcdbcd"

# Дана строкаs, которая содержит только буквы из a to zнижнего регистра.
# Набор алфавита задается путем abcdefghijklmnopqrstuvwxyz.2 набора алфавитов означают 2 или более алфавитов.
# Ваша задача-найти недостающую букву(Ы). Возможно, вам придется вывести их в порядке a-z.возможно, что есть
# более чем одна пропущенная буква из более чем одного набора алфавита.#
# Если строка содержит все буквы алфавита, верните пустую строку ""

# Работает
# def missing_alphabets(s):
#     slavar_set = [chr(column) for column in range(97, 123)]
#     slovar =dict()
#     for column in slavar_set:
#         slovar.setdefault(column,0)
#
#     for column in s:
#         slovar[column] = slovar.get(column)+1
#     s=''
#     r = max(slovar.values())
#     for key, value in slovar.items():
#         if value != r:
#             s +=key*(r-value)
#     return s

def missing_alphabets(s):
    """После того как его оптимизировал самостоятельно"""
    slovar = dict.fromkeys([chr(i) for i in range(97, 123)], 0) #  slovar = {column: 0 for column in [chr(column) for column in range(97, 123)]}
    for i in s:
         slovar[i] = slovar.get(i) + 1
    return ''.join([(max(slovar.values()) - value) * key for key, value in slovar.items() if value != max(slovar.values())])


s = 'abcdefghijklmnopqrstuvwxy'  # z

print(missing_alphabets(s))

# ЧУЖОЙ КОД
def missing_alphabets(s):
  return ''.join(sorted(c * (max(s.count(x) for x in s) - s.count(c)) for c in 'abcdefghijklmnopqrstuvwxyz'))