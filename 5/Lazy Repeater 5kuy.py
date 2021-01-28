"""Lazy Repeater 5 kuy"""


# The makeLooper() __function (make_looper in Python) takes a string (of non-zero length) as an argument. It returns a
# __function. The __function it returns will return successive characters of the string on successive invocations.
# It will start back at the beginning of the string once it reaches the end.
# For example:
# abc = make_looper('abc')
# abc() # should return 'a' on this first call
# abc() # should return 'b' on this second call
# abc() # should return 'c' on this third call
# abc() # should return 'a' again on this fourth call
#
# Функция makeLooper () (make_looper в Python) принимает в качестве аргумента строку (ненулевой длины). Он возвращает
# функцию. Функция, которую она возвращает, будет возвращать последовательные символы строки при последовательных
# вызовах. Он будет начинаться с начала строки, как только она достигнет конца.
# Например:
# АВС = make_looper('Азбука')
# Азбука() # должна вернуть 'а' на этом первый звонок
# Азбука() # должна возвращать 'Б' на этот второй вызов
# Азбука() # должны вернуться в этот третий звонок
# Азбука() # должна вернуть 'а' снова на четвертый звонок

def make_looper(string):
    i = len(string) + 1

    def wrapper():
        nonlocal i
        i += -1 if i else len(string) - 1
        return string[-i]

    return wrapper

# abc = make_looper("При")
# print(abc())
# print(abc())
# print(abc())
# print(abc())
# print(abc())
# print(abc())
# print(abc())
# print(abc())


