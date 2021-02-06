"""Uncollapse Digits 6kuy"""
# Task
# You will be given a string of English digits "stuck" together, like this:
# "zeronineoneoneeighttwoseventhreesixfourtwofive"
# Your task is to split the string into separate digits:
# "zero nine one one eight two seven three six four two five"

# Задание
# Вам будет дана строка английских цифр, "склеенных" вместе
# Ваша задача состоит в том, чтобы разделить строку на отдельные цифры

import re

def we_rate_dogs(string: str) -> str:
    string_numbered = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    pattern = f"({'|'.join(string_numbered)})"
    return ' '.join(re.findall(pattern, string))


text = ["three", "eightsix", "fivefourseven", "ninethreesixthree", "fivethreefivesixthreenineonesevenoneeight"]

standard = ["three", "eight six", "five four seven", "nine three six three",
            "five three five six three nine one seven one eight"]

color = ['\033[32m', '\033[31m', '\033[38m']

for index, string in enumerate(text):
    st = we_rate_dogs(string)
    if st == standard[index]:
        print(
            f"{color[0]}Тест OK: {standard[index]}{color[2]} а вышло так: {color[0]}{st}{color[2]}")
    else:
        print(
            f"{color[1]}Тест Fail:{color[2]}{color[0]} {standard[index]}{color[2]} а вышло так: {color[1]}{st}{color[2]}")
