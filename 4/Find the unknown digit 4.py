"""Find the unknown digit 4"""

# The professor will give you a simple math expression, of the form
# [number][op][number]=[number]
# He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-),
# and multiplication (*), so those are the only ones that will appear. Each number will be in the
# range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s.
# If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator, '
# and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the '
# other given digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would
# not be a valid number. Given an expression, figure out the value of the rune represented by the question mark.
# If more than one digit works, give the lowest one. If no digit works, well, that's bad news for the professor - '
# 'it means that he's got some of his runes wrong. output -1 in that case. Complete the method to solve the expression to
# find the value of the unknown rune. The method takes a string as a paramater repressenting the expression and will
# return an int value representing the unknown rune or -1 if no such rune exists.
#
# Профессор даст вам простое математическое выражение вида
# [число][ФП][количество]=[количество]
# Он превратил все известные ему руны в цифры. Единственные известные ему операторы-это сложение (+),вычитание ( - ) и
# умножение ( * ), так что это единственные, которые появятся. Каждое число будет находиться в диапазоне от -1000000 до
# 1000000 и будет состоять только из цифр 0-9, возможно, ведущих -, а может быть, и нескольких ?с. если они есть ?s в
# выражении они представляют собой цифровую руну, которую профессор не знает (никогда оператор и никогда ведущий -).
# Все это ?s в выражении будет представлять ту же цифру (0-9), и это не будет одна из других заданных цифр в выражении.
# Ни одно число не будет начинаться с 0, если само число не равно 0, поэтому 00 не будет допустимым числом. Учитывая
# выражение, определите значение руны, представленной вопросительным знаком. Если работает более одной цифры, Назовите
# самую низкую. Если ни одна цифра не сработает, что ж, это плохая новость для профессора - это значит, что он ошибся в
# некоторых своих рунах. в этом случае выведите значение -1. Завершите метод решения выражения, чтобы найти значение
# неизвестной руны. Метод принимает строку в качестве параметра, репрессирующего выражение, и возвращает значение int,
# представляющее неизвестную руну, или -1, если такой руны не существует.

" для кодеварс"

def solve_runes(runes):
    #  """ Получаем руну.
    #  1. Разбиваем руну на 4 компонента числа x, y, z(список number) и математический знак(sign)
    # 2. Создаем список цифр(array), который будем перебирать, с учетом:
    #     a. 0 не может быть первым символом если подстрока более 1 символа
    #     b.Учитываем, что “–“ может быть первым символом в подстроке Сортируем список(array), что бы начать обход с
    #   минимального значения
    #  3. Обходим список цифр(array) и подставляем в место ‘?’ цифру из списка, в новый список(xyz).Далее сравниваем значение
    #     выражения x sign y с z и если верное выходим из функции возвращаем текущий элемент списка(array)"""

    print('исходная строка', runes)

    for i in ['+', '*', '-']:
        if i in runes:
            sign = runes[runes.find(i)]
            break
    number = [runes[:runes.find(sign, 1)],  # a
              runes[runes.find(sign, 1) + 1:runes.find('=')],  # b
              runes[runes.find('=') + 1:]]  # c

    allnumbers = {i for i in range(10)}
    runesnumbers = {int(i) for i in runes if i.isdigit()}
    if any(True if (i[0] == '-' and i[1] == '?') or
                   (i[0] == '?' and len(i) > 1) else False for i in number):
        runesnumbers.add(0)

    number = [i[::-1] for i in number]
    lst = sorted(list(allnumbers - runesnumbers))

    for i in lst:
        xyz = [0, 0, 0]
        index = 0
        for item in number:
            for j in range(len(item)):
                if item[j] != '-':
                    xyz[index] += int(item[j]) * pow(10, j) if item[j] != '?' else i * pow(10, j)
                else:
                    xyz[index] *= -1
            index += 1
        if eval(f'{xyz[0]}{sign}{xyz[1]}') == xyz[2]:
            return i

    return -1

# чужой код
def solve_runes(runes):
    # Sorted set subtraction returns a list of elements in the first set that weren't in the second
    for i in sorted(set('0123456789')-set(runes)):
        # Prepare string for eval
        eval_string = runes.replace('?', str(i)).replace('=','==')
        # Python 3 gives an error if an int starts with 0.
        # We use it for our advantage. Also check that result is not 00
        try:
            if eval(eval_string) and eval_string[-4:] != '==00':
                return int(i)
        except:
            continue
    return -1

import re

def solve_runes(runes):
    for d in sorted(set("0123456789") - set(runes)):
        toTest = runes.replace("?",d)
        if re.search(r'([^\d]|\b)0\d+', toTest): continue
        l,r = toTest.split("=")
        if eval(l) == eval(r): return int(d)
    return -1

# runa = '??605*-63=-73???5'  # 1
# runa = '?*123?45=?' # 0
# runa = '?*11=??'  # 2
runa = '??*1=??'  # 2
# runa = '1+1=?' #2
# runa = '-19-45=50?' #-1
# runa = '-5?*-1=5?'  # 0
# runa = '-2361+-?2122=-?4483' #5
# runa= '??*??=302?'
print(solve_runes(runa))
