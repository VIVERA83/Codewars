"""Numbers in strings 7"""


# В этой Кате вам будет дана строка, содержащая строчные буквы и цифры. Ваша задача-сравнить группы чисел и вернуть наибольшее число.
# Напримерsolve("gh12cdy695m1") = 695, потому, что это самая большая из всех групп чисел.
# Удачи вам! Пожалуйста, также попробуйте просто удалить дубликаты

def solve(s):
    s += ' '
    lst = []
    ch = ' '
    for i in s:
        if i.isdigit():
            ch += i
        else:
            lst.extend([ch])
            ch = ' '
    s = max(list(map(int, ' '.join(lst).split())))
    return s


def solve(s):  # после
    s = ''.join(['*' if x.isalpha() else x for x in s])
    s = [int(x) if x.isdigit() else 0 for x in s.split('*')]
    return max(s)


# # Чужой код
# def solve(s):
#     a = ''.join(['*' if x.isalpha() else x for x in list(s)])
#     print(a)
#     b = [int(x) if x.isdigit() else 0 for x in a.split('*')]
#     print(b)
#     return max(b)

s = 'gh12cdy695m1'  # 695
s = 'lu1j8qbbb85'  # ,85)
print(solve(s))
# print(fil(s))
