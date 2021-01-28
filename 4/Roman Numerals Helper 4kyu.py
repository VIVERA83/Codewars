"""Roman Numerals Helper 4kyu"""
# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API
# demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
# any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Examples
# RomanNumerals.to_roman(1000) # should return 'M'
# RomanNumerals.from_roman('M') # should return 1000

# Создайте класс RomanNumerals, который может преобразовывать римскую цифру в целочисленное значение и обратно. Он
# должен следовать API, показанному в приведенных ниже примерах. Для каждого вспомогательного метода будет проверено
# несколько значений римских цифр. Современные римские цифры пишутся путем выражения каждой цифры отдельно, начиная с
# самой левой цифры и пропуская любую цифру со значением нуля. В римских цифрах 1990 отображается: 1000=M, 900=CM,
# 90=XC; в результате MCMXC. 2008 записывается как 2000=MM, 8=VIII; или MMVIII. 1666 использует каждый римский символ
# в порядке убывания: MDCLXVI.

class RomanNumerals:
    @staticmethod
    def to_roman(n):  # работает
        """Функция переводит число в римское
        Принцип работы: Получаем число, его преобразуем в строку и переворачиваем, далее идем по строке и отталкиваясь
        от индекса в строке создаем соответсвенный словарь из римских цифр. Первая цифра в строке это единицы, потом
        десятки, сотни и тысяча. Для каждого измерения применяется 3 римские цифры"""
        n = str(n)[::-1]
        st = ''
        roman_lst = ['', 'I', 'V', 'X', 'L', 'C', 'D', 'M']
        index = 0
        for ch in n if len(n) < 4 else n[:3]:
            index += 2
            if int(ch):
                roman_dict = \
                    {0: '*',
                     1: f'{roman_lst[index - 1]}',  # I
                     2: f'{roman_lst[index - 1] * 2}',  # II
                     3: f'{roman_lst[index - 1] * 3}',  # III
                     4: f'{roman_lst[index - 1] + roman_lst[index]}',  # IV
                     5: f'{roman_lst[index]}',  # V
                     6: f'{roman_lst[index] + roman_lst[index - 1]}',  # VI
                     7: f'{roman_lst[index] + roman_lst[index - 1] * 2}',  # VII
                     8: f'{roman_lst[index] + roman_lst[index - 1] * 3}',  # VIII
                     9: f'{roman_lst[index - 1] + roman_lst[index + 1]}'}  # IX
                st = roman_dict[int(ch)] + st  # добавляем в строку соответствующий цифре римскую
        st = ('' if len(n) < 4 else 'M' * int(n[:2:-1])) + st  # манипуляция с тысячами
        return st  # , 'все получилось'

    @staticmethod
    def from_roman(st):  # работает
        """Функуия римское число переводи в обычное"""
        roman_lst = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        """ Высчитываем тысячи, и заодно сокращаем строку до 3 знаков"""
        number = st.count('M') - st.count('CM')
        st = st[number:]
        number = number * 1000  # Переменная в которую результируется перевод
        """ переводим каждую римскую цифру в соответствующие значение"""
        lst_number = list(map(lambda i: roman_lst.get(i), st))
        lst_number.append(0)  # нужно что бы 6 не привратолось в 4
        """считаем итоговую цифру 9 IX - 10-1"""
        for i in range(len(lst_number)):
            number += lst_number[i] - lst_number[i - 1] * 2 if lst_number[i] > lst_number[i - 1] else lst_number[i]
        return number

"""Тело программы"""
number = 777  # 'MCMXC 1990'
s = RomanNumerals.to_roman(number)
print(s)
print(RomanNumerals.from_roman(s))
