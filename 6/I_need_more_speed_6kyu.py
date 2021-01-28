"""
Remove this comment otherwise your code cannot pass the anti-cheat tests!

You are not allowed to use the following:
    - python 2
    - slice notations
    - defining an empty list: []. Use "x=list()" instead if you need it
    - list comprehensions
    - the spread operator inside square brackets
    - "tuple" and "reversed" builtins have been deactivated

The "list" builtin has been replaced with another implementation with the following specifications:
    - list.reverse is forbidden
    - list.__reversed__ is forbidden
    - slicing is forbidden
All other usual methods of the list class are still present.
"""


# Write a __function that will take in any array and reverse it.
# Sounds simple doesn't it?
# NOTES:
# Array should be reversed in place! (no need to return it)
# Usual builtins have been deactivated. Don't count on them.
# You'll have to do it fast enough, so think about performances

# ver 2.0 не прошли тест по скорости , вероятно из- за функции инсерт
def reverse(seq: list) -> None:
    for i in range(len(seq)):
        seq.insert(i, seq.pop())
    pass


# ver 1.0 как и предпологалось вставка очень медленный процесс
def reverse(seq: list) -> None:
    temp_list = list()
    for index in range(len(seq)):
        temp_list.append(seq.pop())
    for value in temp_list:
        seq.append(value)
    pass


seq = [1, 2, 3, 4, 5, 6, 7]
# reverse(seq)
print(len(seq) // 2)
for i in range(len(seq) >> 1):
    print(i, len(seq) >> 1, -i - 1, -i)
    seq[i], seq[-i - 1] = seq[-i - 1], seq[i]
print(seq)

# забавно в задание вроде сказано пользоваться скобками нельзя, аот оно  трудность перевода
# def reverse(seq):
#     for i in range(len(seq)>>1):
#         seq[i],seq[-i-1] = seq[-i-1],seq[i]

# def reverse(seq):
#     for i in range(len(seq)>>1):
#         seq[i],seq[-i-1] = seq[-i-1],seq[i]
