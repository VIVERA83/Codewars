"""ISBN-10 Validation 5kuy"""

# SBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X,
# to indicate a value of 10.
# An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

# Идентификаторы ISBN-10 состоят из десяти цифр. Первые девять символов-это цифры 0-9.
# Последняя цифра может быть 0-9 или X, чтобы указать значение 10.
# Число ISBN-10 допустимо, если сумма цифр, умноженная на их положение по модулю 11, равна нулю.

# Пример:
# ISBN     : 1 1 1 2 2 2 3 3 3  9
# position : 1 2 3 4 5 6 7 8 9 10
#
# Это действительный ISBN, потому что:
# (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

import re

def valid_ISBN10(isbn):
    pattern = r"[\d]|(?:X$)"
    number_list = re.findall(pattern,isbn)
    if len(number_list) == 10:
        result_sum = 0
        for index, number in enumerate(map(lambda item: int(item) if item.isdigit() else 10, number_list), 1):
            result_sum += number * index
        if not result_sum % 11:
            return True
    return False


test_list = [('1112223339', True),
             ('048665088X', True),
             ('1293000000', True),
             ('1234554321', True),
             ('1234512345', False),
             ('1293', False),
             ('X123456788', False),
             ('ABCDEFGHIJ', False),
             ('XXXXXXXXXX', False)
             ]

color = ['\033[32m', '\033[31m', '\033[38m']

for string, correct in test_list:
    result = valid_ISBN10(string)
    if result == correct:
        print(
            f"{color[0]}Тест OK: {correct}{color[2]} а вышло так: {color[0]}{result}{color[2]}")
    else:
        print(
            f"{color[1]}Тест Fail:{color[2]}{color[0]} {correct}{color[2]} а вышло так: {color[1]}{result}{color[2]}")

