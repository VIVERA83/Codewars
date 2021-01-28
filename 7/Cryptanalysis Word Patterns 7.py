"""Cryptanalysis Word Patterns 7"""

# In cryptanalysis, words patterns can be a useful tool in cracking simple ciphers.
# A word pattern is a description of the patterns of letters occurring in a word, where each letter is given an integer
# code in order of appearance. So the first letter is given the code 0, and second is then assigned 1 if it is different
# to the first letter or 0 otherwise, and so on.
# As an example, the word "hello" would become "0.1.2.2.3". For this task case-sensitivity is ignored,
# so "hello", "helLo" and "heLlo" will all return the same word pattern.
# Your task is to return the word pattern for a given word. All words provided will be non-empty strings of alphabetic
# characters only, column.e. matching the regex "[a-zA-Z]+".

# В криптоанализе словесные шаблоны могут быть полезным инструментом для взлома простых шифров.
# Шаблон слова-это описание шаблонов букв, встречающихся в слове, где каждой букве присваивается целочисленный код в
# порядке появления. Таким образом, первой букве присваивается код 0, а второй-1, если она отличается от первой буквы,
# или 0 в противном случае, и так далее.
# Например, слово "привет" станет "0.1.2.2.3". Для этой задачи чувствительность к регистру игнорируется,
# поэтому "hello", "helLo" и "heLlo" будут возвращать один и тот же шаблон слов.
# Ваша задача-вернуть шаблон слова для данного слова. Все предоставленные слова будут непустыми строками только
# буквенных символов, то есть совпадающими с регулярным выражением "[a-zA-Z]+" .

def word_pattern(word):
    a = {}
    return '.'.join(str(a.setdefault(i, len(a))) for i in word.lower())

word = 'hello' # 0.1.2.2.3

print(word_pattern(word))

# Чужой код   Походу у меня реально самое короткое и лучшее решение

def word_pattern(word):
    ret, box, i = [], {}, 0
    for e in word.lower():
        if e not in box:
            box[e] = str(i)
            i += 1
        print(f'e = {e}')
        print(f'box[e] = {box[e]}')
        print(f'box = {box}')
        ret.append(box[e])
        print(f'{ret}\n-------------------------------')

    return '.'.join(ret)

print(word_pattern(word))
