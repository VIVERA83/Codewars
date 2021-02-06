"""replaceLletter 7kuy"""
# Egg Talk.
# Insert an "egg" after each consonant. If there are no consonants, there will be no eggs. Argument will consist of a
# string with only alphabetic characters and possibly some spaces.
# eg:
# hello => heggeleggleggo
# eggs => egegggeggsegg
# FUN KATA => FeggUNegg KeggATeggA

# Вставьте "яйцо" после каждого согласного. Если нет согласных, не будет и яиц. Аргумент будет состоять из строки,
# содержащей только алфавитные символы и, возможно, некоторые пробелы


import re


def heggeleggleggo(word: str) -> str:
    pattern = r"[^euioaEUIOA ]"
    replacement = 'egg'
    # словарь согласных букв и их количество
    letters = {letter: re.findall(pattern, word).count(letter) for letter in re.findall(pattern, word)}
    # если в словаре есть буква 'g' мы в исходной строке сразу делаем замену на 'gegg', и удаляем букву из словаря
    if letters.get('g'):
        word = re.sub('g', 'g' + replacement, word)
        del (letters['g'])
    # обходим словарь и заменяем
    for letter, count in letters.items():
        word = re.sub(letter, letter + replacement, word, count=count)
    return word

# проверка

text = ['hello', 'scrambled eggs']
TEST_standard = ['heggeleggleggo', 'seggceggreggameggbeggleggedegg egegggeggsegg']

for index, string in enumerate(text, 1):
    st = heggeleggleggo(string)
    if st == TEST_standard[index - 1]:
        print(f"Тест OK: Получилось так = {st} а надо было:  {TEST_standard[index - 1]}")
    else:
        print(
            f"Тест Fail: Получилось так = {st} {len(st)} а надо было:  {TEST_standard[index - 1]} {len(TEST_standard[index - 1])}")


# более удачные решения

def heggeleggleggo(word):
    return re.sub(r'(?i)([^aeiou\W])', r'\1egg', word)
# (?i) - флаг игнорирования верхнего регистра
# ([^aeiou\W]) - наш шаблон, ищем все буквы кроме описанных и символов \W
# r'\1egg' - это шаблон для замены, \1 = (?i)([^aeiou\W])
