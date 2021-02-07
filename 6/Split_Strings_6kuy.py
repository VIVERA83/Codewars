"""Split Strings 6kuy"""

# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number
# of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Завершите решение так, чтобы оно разбило строку на пары из двух символов.
# Если строка содержит нечетное число символов, то она должна заменить отсутствующий второй символ последней
# пары символом подчеркивания ('_').
# Пример:
# 'abc'    -> ['ab', 'c_']
# 'abcdef' -> ['ab', 'cd', 'ef']

import re


def solution(s: str) -> list:  # [str,str]
    pattern = r"(\w{2})|(\w{1})"
    return [item[0] if len(item[0]) > 1 else item[0] + '_' for item in re.finditer(pattern, s)]


text = ["asdfadsf", "adsfads", "", "x", "abc", "abcdef"]
standard = [['as', 'df', 'ad', 'sf'], ['ad', 'sf', 'ad', 's_'], [], ["x_"], ['ab', 'c_'], ['ab', 'cd', 'ef']]

color = ['\033[32m', '\033[31m', '\033[38m']

for index, item in enumerate(text):
    st = solution(item)
    if st == standard[index]:
        print(
            f"{color[0]}Тест OK: {standard[index]}{color[2]} а вышло так: {color[0]}{st}{color[2]}")
    else:
        print(
            f"{color[1]}Тест Fail:{color[2]}{color[0]} {standard[index]}{color[2]} а вышло так: {color[1]}{st}{color[2]}")

# еще одно решение
def solution(s):
    return re.findall(".{2}", s + "_")

