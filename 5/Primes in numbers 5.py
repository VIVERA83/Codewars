"""Primes in numbers 5"""


#
# Given a positive number n > 1 find the prime factor decomposition of n.
# The result will be a string with the following form : "(p1**n1)(p2**n2)...(pk**nk)"
# where a ** b means a to the power of b
# with the new_value_cell(column) in increasing order and n(column) empty if n(column) is 1.
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

# При положительном числе n > 1 Найдите разложение простого множителя n.
# Результатом будет строка следующего вида : "(p1**n1)(p2**n2)...(pk**nk)"
# где a ** b средства aк власти b
# # с new_value_cell (column) в порядке возрастания и N (column) пустым, если n (column) равно 1.
# # Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


def primeFactors(n):
    i = 2
    st_dict = {}  # dictionary of Prime factors список простых множителей
    while n > 1:  # The decomposition of a number into factors разложение числа на множители и заполнение словаря
        if not n % i:  # если число делится без остатка
            st_dict.setdefault(i, 0)  # если такого множителя нет добавляем его с значением 0
            st_dict[i] += 1  # добавляем степень
        n //= i if not n % i else 1
        i += 1 if n % i else 0
        # Превращаем словарь в строку (2**5)(5)(7**2)(11)
    return ''.join(map(lambda x: f'({x[0]}**{x[1]})' if x[1] > 1 else f'({x[0]})', st_dict.items()))


n = 16
print(primeFactors(n))


# чужой
def primeFactors(n):
    p = 2
    factors = dict()
    while n >= p:
        if n % p == 0:
            if str(p) in factors:
                factors[str(p)] += 1
            else:
                factors[str(p)] = 1
            n = n // p
        else:
            p += 1
    result = ''
    for factor, power in factors.items():
        result += f'({factor}**{power})' if power != 1 else f'({factor})'  # у меня круче
    return result
