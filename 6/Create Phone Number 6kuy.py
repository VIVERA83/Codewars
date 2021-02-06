"""Create Phone Number 6"""


# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
#
# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!
# Test.describe("Basic tests")
# Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
# Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
# Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
# Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
# Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

import re

def create_phone_number(n: list) -> str:
    """Функция принимает (n - list в котором все элементы целые числа от 0 до 9) и возвращает строку в виде
    телефонного номера например '(123) 456-7890' """
    string = ''.join(map(str,n))
    pattern = r"(\d{3})(\d{3})(\d{4})"
    insert_element = r"(\1) \2-\3"
    return re.sub(pattern,insert_element,string)


# Проверка

color = ['\033[32m', '\033[31m', '\033[38m']
text = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        [0, 2, 3, 0, 5, 6, 0, 8, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

standard = ["(123) 456-7890",
            "(111) 111-1111",
            "(123) 456-7890",
            "(023) 056-0890",
            "(000) 000-0000"]

for index, item in enumerate(text):
    st = create_phone_number(item)
    if st == standard[index]:
        print(
            f"{color[0]}Тест OK: {standard[index]}{color[2]} а вышло так: {color[0]}{st}{color[2]}")
    else:
        print(
            f"{color[1]}Тест Fail:{color[2]}{color[0]} {standard[index]}{color[2]} а вышло так: {color[1]}{st}{color[2]}")

# интересный вариант
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)