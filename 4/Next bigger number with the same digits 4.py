"""Next bigger number with the same digits 4"""

# Create a __function that takes a positive integer and returns the next bigger number
# that can be formed by rearranging its digits. For example:
#
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):
#
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1
# nextBigger(num: 9)   // returns nil
# nextBigger(num: 111) // returns nil
# nextBigger(num: 531) // returns nil

# Создайте функцию, которая принимает положительное целое число и возвращает следующее большее число,
# которое может быть сформировано путем перестановки его цифр.


def next_bigger(n):
    print(n)
    st = str(n)
    l = len(st)
    st = list(st)

    if all([True if st[i] >= st[i+1] else False for i in range(l-1)]): # проверка на то что из приведенного числа можно создать большее число
        return -1

    for i in range(l-1, 0, -1):
        temp = st[i:]
        temp.sort()
        print(i,''.join(st[:i]), temp)
        print(st[i-1], st[i])
        if st[i-1] < st[i]:
            for j in range(len(temp)):
                if st[i - 1] < temp[j]:
                    st[i - 1], temp[j] = temp[j], st[i - 1]
                    st = st[:i]+temp
                    return int(''.join(st))
            print(st, temp)
            st[i-1], temp[0] =temp[0] ,st[i-1]
            print('q1',st,temp)
            temp.sort()
            st[:i] += temp
            return int(''.join(st[:l]))

def next_bigger(n):
    st = str(n)
    l = len(st)
    st = list(st)
    # Проверка на 9 ==> -1 # 111 ==> -1 # 531 ==> -1
    if all([True if st[i] >= st[i+1] else False for i in range(l-1)]):
        return -1

    for i in range(l-1, 0, -1):# идем по числу с лева на права
        temp = st[i:] # создаем копию числа с лева на право
        temp.sort() # сортируем, что бы выявить самые меленькие цифры из просмотренных а так же это готовая минимальное число при склеевании правой и левой строны
        if st[i-1] < st[i]: # если левая цифра меньше, миняем их местами если еконечно
            for j in range(len(temp)): # нет более мелких чисел которые тоже меньше текущего
                if st[i - 1] < temp[j]: # сдесь мы проверяем есть ли среди правых чисел еще более мелкие цифры
                    st[i - 1], temp[j] = temp[j], st[i - 1]
                    st = st[:i]+temp
                    return int(''.join(st))
            st[i-1], temp[0] =temp[0] ,st[i-1] # если нет то меняем найденый и возращаем получившееся число
            temp.sort()
            st[:i] += temp
            return int(''.join(st[:l]))



# 59884848 459853
# 59884848 483559
#          493558

print(next_bigger(175431))
    #  59884848459853
    # 1234567890
# 1234567908
# 68129 61928
    # Test.assert_equals(next_bigger(2017), 2071)
    # Test.assert_equals(next_bigger(414), 441)
    # Test.assert_equals(next_bigger(144), 414)