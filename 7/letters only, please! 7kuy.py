"""letters only, please! 7kuy"""
# Let's assume we need "clean" strings. Clean means a string should only contain letters a-z, A-Z and spaces. We assume
# that there are no double spaces or line breaks.
# Write a function that takes a string and returns a string without the unnecessary characters.


# Предположим, нам нужны "чистые" строки. Чистый означает, что строка должна содержать только буквы a-z, A-Z и пробелы.
# Мы предполагаем, что нет двойных пробелов или разрывов строк.
# Напишите функцию, которая принимает строку и возвращает строку без ненужных символов.
# Исходная строка ('.tree1')                                  ==> 'tree' результат
#                 ("that's a pie$ce o_f p#ie!")               ==> 'thats a piece of pie'
#                 ('john.dope@dopington.com')                 ==> 'johndopedopingtoncom'
#                 ('my_list = ["a","b","c"]')                 ==> 'mylist  abc'
#                 ('1 + 1 = 2')                               ==> '    ' (строка из 4 пробелов)
#                 ("0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_") ==> '' (пустая строка)

import re


def remove_chars(s):
    return re.sub(r"[^a-zA-Z ]*", '', s)


# проверка

text = ['.tree1', "that's a pie$ce o_f p#ie!", 'john.dope@dopington.com', 'my_list = ["a","b","c"]', '1 + 1 = 2',
        "0123456789(.)+,|[]{}=@/~;^$'<>?-!*&:#%_"]
standard = ['tree', 'thats a piece of pie', 'johndopedopingtoncom', 'mylist  abc', '    ', '']

pattern = r"[^a-zA-Z ]*"

for index, string in enumerate(text, 1):
    st = remove_chars(string)
    print(index, 'OK ' + st if st == standard[index - 1] else 'Fail')