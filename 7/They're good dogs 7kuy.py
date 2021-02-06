"""They're good dogs.7kuy"""

# Description:
# At 'We Rate Dogs', we try our best to give dogs accurate ratings, which will always be above 10/10. Because they're
# good dogs. Over the weekend Bront has come in and hacked our system, lowering the ratings of dogs to below 10/10.
# Please help to fix Brant's bad system and give the dogs their original ratings. They're good dogs Brent.
# Task:
# The function weRateDogs(str, rating) takes a string and an integer as the inputs. Within the string is an
# incorrect rating x/y.
# You will need to change the incorrect rating x/y to the correct rating rating/10. The given string may
# contain numbers and letters, but no special characters other than /.
# For example (Пример):
# if you are given the following string:
# 'This is Max99. She has one ear that is always s1ightly higher than the other 4/10 wonky af'
# And the following rating:
# 11 return: 'This is Max99. She has one ear that is always s1ightly heigher than the other 11/10 wonky af'

# Функция WeRateDogs(str, rating) принимает в качестве входных данных строку и целое число. Внутри строки находится
# неверная оценка x/y. Вам нужно будет изменить неправильный рейтинг x/y на правильный рейтинг rating/10. Данная строка
# может содержит цифры и буквы, но никаких специальных символов, кроме /.

import re


def we_rate_dogs(string: str, rating: int) -> str:
    pattern = r"(\d{,2}/\d{,2})"
    replacement = f"{str(rating)}/10"
    return re.sub(pattern, replacement, string)


# Проверка

text = [('This is Tucker. He would like a hug. 3/10 someone hug him', 11),
        ('This is Charlie. He pouts until he gets to go on the swing. 5/10 manipulative af.', 12),
        ('This is Max99. She has one ear that is always s1ightly higher than the other 4/10 wonky af', 11)]

standard = ['This is Tucker. He would like a hug. 11/10 someone hug him',
            "This is Charlie. He pouts until he gets to go on the swing. 12/10 manipulative af.",
            'This is Max99. She has one ear that is always s1ightly higher than the other 11/10 wonky af']

color = ['\033[32m', '\033[31m', '\033[38m']

for index, (string, value) in enumerate(text):
    st = we_rate_dogs(string, value)
    if st == standard[index]:
        print(
            f"{color[0]}Тест OK: {standard[index]}{color[2]} а вышло так: {color[0]}{st}{color[2]}")
    else:
        print(len(st), len(standard[index]))
        print(
            f"{color[1]}Тест Fail:{color[2]}{color[0]} {standard[index]}{color[2]} а вышло так: {color[1]}{st}{color[2]}")
