"""Product of consecutive Fib numbers 5"""
from functools import reduce

# The Fibonacci numbers are the numbers in the following integer sequence (Fn):
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
# such as
# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
# F(n) * F(n+1) = prod.
# Your __function productFib takes an integer (prod) and returns an array:
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
#
# Числа Фибоначчи - это числа в следующей целочисленной последовательности (Fn):
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
# такие как:
# F(n) = F(n-1) + F(n-2) с F(0) = 0 и F (1) = 1.
# Учитывая число, скажем prod (для продукта), мы ищем два числа Фибоначчи F (n) и F (n+1).
# F (n) * F (n+1) = prod.
# Ваша функция product Fib принимает целое число (prod) и возвращает массив:
# [F (n), F (n+1), true] или {F (n), F (n+1), 1} или (F( n), F (n+1), True)
# Если вы не найдете двух последовательных F (m), проверяющих F (m) * F (m+1) = prod, вы вернетесь


"""
productFib(714) # should return (21, 34, true),
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
productFib(800) # should return (34, 55, false),
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
productFib(714) # should return [21, 34, true],
productFib(800) # should return [34, 55, false],
productFib(714) # should return {21, 34, 1},
productFib(800) # should return {34, 55, 0},
productFib(714) # should return {21, 34, true},
productFib(800) # should return {34, 55, false}, 
"""
from time import time

def productFib(n): # работает
    def fib(n):
        num = [0,1]
        flag = False
        for i in range(n):
            num[flag] = num[0]+num[1]
            print(num[flag])
            flag = not flag
            yield num[not flag]

    it = fib(n)
    flag = False
    num = [0,1]
    for j in range(n):
        num[flag] = next(it)
        print(j,num[flag])
        if num[0]*num[1] == n:              # if reduce(lambda x=1, y=1: x*y,num) == n:
            num.sort()
            num.append(True)
            return num
        elif num[0]*num[1] > n:
            num.sort()
            num.append(False)
            return num
        flag = not flag
    return [0, 1, True]

# ЧУЖОЙ КОД
def productFib(prod): # все гениальное просто
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]

n = 800
print(productFib(n))

