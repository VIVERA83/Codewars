"""Who has the most money?"""

# Как видите, у каждого ученика есть пятерки, десятки и двадцатки. Ваша задача-вернуть имя студента с наибольшим
# количеством денег. Если у каждого ученика есть одинаковая сумма, то верните "все".
#
# Записи:
# # У каждого ученика будет свое уникальное имя
# Всегда будет явный победитель: либо у одного человека больше всего, либо у всех одинаковое количество
# Если есть только один студент, то у этого студента больше всего денег

class Student:
    def __init__(self, name: str, fives: int, tens: int, twenties: int):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    money_students = [sum([student.fives * 5, student.tens * 10, student.twenties * 20]) for student in students]
    max_money = max(money_students)
    count = 0
    for ind, money in enumerate(money_students):
        if max_money == money:
            index = ind
            count += 1
    return students[index].name if count == 1 else 'all'


# Чужой код
# money = lambda student: 5*student.fives + 10*student.tens + 20*student.twenties
#
# def most_money(students):
#     if len(students) == 1: return students[0].name
#     D = {money(student):student.name for student in students}
#     return "all" if len(D) == 1 else D[max(D)]