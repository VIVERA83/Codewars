"""Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this
way until a single-digit number is produced. This is only applicable to the natural numbers
Учитывая n, возьмем сумму цифр n.если это значение имеет более одной цифры, продолжайте уменьшать таким образом
, пока не будет получено одноразрядное число. Это применимо только к натуральным числам
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

def digital_root(n):
    if n>9:
        d=0
        while n>0:
            d, n = d + n % 10, n//10
        n = digital_root(d)
    return n
# у меня оказался не саймый плохой ответ

#чужой код
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# код генерации тестов на сайте
# k = 1 + ((n - 1) % 9) if n > 0 else 0
# переменная = действоие(результат) условие иначе ответ при иначе

print(digital_root(125))
