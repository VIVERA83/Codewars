"""Encrypt this! 6kuy"""
# Description:
# Encrypt this!
# 1. You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
#    Your text is a string containing space separated words.
# 2. You need to encrypt each word in the text using the following rules:
#       = The first letter needs to be converted to its ASCII code.
#       = The second letter needs to be switched with the last letter
# 3. Keepin' it simple: There are no special characters in input.

# Ваше сообщение-это строка, содержащая слова, разделенные пробелом.
# 1. Вам нужно зашифровать каждое слово в сообщении, используя следующие правила:
#    * Первая буква должна быть преобразована в свой ASCII-код.
#    * Вторая буква должна быть заменена последней буквой
# 2. Во входных данных нет специальных символов.
# Примеры
# "Hello" == "72olle"
# "good" == "103doo"
# "hello world" == "104olle 119drlo"

import re



def encrypt_this(text: str) -> str:
    # pattern = r"(?:\b(\w)(\w)?(.*?)(\w)?\b)+"
    # С начало  меняем вторую букву с последней в слове
    pattern = r"\b(\w)(\w?)(\w*?)(\w)?\b"
    replacement = r"\1\4\3\2"
    text = re.sub(pattern, replacement, text)

    # Находим все первые буквы в словах и их индексы в строке
    pattern = r"\b(\w)"
    rep_char = []
    for index in re.finditer(pattern, text):
        rep_char.append((index.group(), index.start()))
    # реверсируем список, для того что бы начать замену букв на их код с конца
    rep_char.reverse()
    # замена первой буквы в слове на ее код
    for char, index in rep_char:
        text = text[:index] + str(ord(char)) + text[index + 1:]
    return text


# Проверка

color = ['\033[32m', '\033[31m', '\033[38m']
text = ["Hello", "good", "hello world",
        "A wise old owl lived in an oak",
        "The more he saw the less he spoke",
        "The less he spoke the more he heard",
        "Why can we not all be like that wise old bird",
        "Thank you Piotr for all your help", ""]

standard = ["72olle", "103doo", "104olle 119drlo",
            "65 119esi 111dl 111lw 108dvei 105n 97n 111ka", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp",
            "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare",
            "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri",
            "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple",""]
print()
for index, string in enumerate(text):
    st = encrypt_this(string)
    if st == standard[index]:
        print(
            f"{color[0]}Тест OK: {standard[index]}{color[2]} а вышло так: {color[0]}{st}{color[2]}")
    else:
        print(
            f"{color[1]}Тест Fail:{color[2]}{color[0]} {standard[index]}{color[2]} а вышло так: {color[1]}{st}{color[2]}")


# Интересные решения
        pattern = r"(?:\b(\w)(\w?)(\w*?)(\w)?\b)+"
def encrypt_this(text):
    return re.sub(r'\b(\w)(\w?)(\w*?)(\w?)\b', lambda m: '{}'.format(str(ord(m.group(1))) + m.group(4) + m.group(3) + m.group(2)), text).replace('   ', ' ').replace('  ', ' ')