"""Regex Password Validation 5"""

"""Требуется изучение Регулярных Выражений"""
# ДОДЕЛАЙ !!!!!!

# You need to write regex that will validate a password to make sure it meets the following criteria:
#
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.

# Вам нужно написать регулярное выражение, которое будет проверять пароль, чтобы убедиться, что он соответствует
# следующим критериям:
#    По крайней мере шесть символов длиной  - 6
#    Содержит строчную букву                - a
#    Содержит заглавную букву               - A
#    Содержать число                        - 1
#    Допустимыми паролями будут только буквенно-цифровые символы.  ТОЛЬКО цифры и буква

regex = ""


# функция проверки
def check_password(st):
    d = all([True if len(st) > 5 else False,
             any(True if ord(i) in range(97, 123) else False for i in st),
             any(True if ord(i) in range(65, 91) else False for i in st),
             any(True if ord(i) in range(48, 57) else False for i in st),
             all(True if ord(i) in ((range(97, 123)) or (range(48, 57)) or (range(65, 91))) else False for i in st)])
    return d


a = lambda st: all([True if len(st) > 5 else False,
               any(True if ord(i) in range(97, 123) else False for i in st),
               any(True if ord(i) in range(65, 91) else False for i in st),
               any(True if ord(i) in range(48, 57) else False for i in st),
               all(True if ord(i) in ((range(97, 123)) or (range(48, 57)) or (range(65, 91))) else False for i in st)])

print(a('a2.d412'))
print(a('fjd3  IR9'))
