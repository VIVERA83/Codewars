"""Game - Electrons around the cores 5"""

# Have you heard of the game "electrons around the cores"? I'm not allowed to give you the complete rules of the game,
# just so much:
# the game is played with 4 to 6 dice, so you get an array of 4 to 6 numbers, each 1-6
# the name of the game is important
# you have to return the correct number five times in a row and your solution is considered to be correct
# If you just press "submit", you'll get an array and the expected value!
# Here are some input/output pairs for you to wrap your mind around:
# [ 1, 2, 3, 4, 5 ] -> 6
# [ 2, 2, 3, 3 ] -> 4
# [ 6, 6, 4, 4, 1, 3 ] -> 2
# [ 3, 5, 3, 5, 4, 2 ] -> 12
"""
And yes, it is a shameless copy of a famous game.
Вы слышали об игре "электроны вокруг ядер"? Я не имею права давать вам полные правила игры, просто так много:
игра ведется с 4 до 6 кубиков, так что вы получаете массив из 4 до 6 чисел, каждое 1-6
название игры очень важно
вы должны вернуть правильное число пять раз подряд и ваше решение будет считаться правильным
Если вы просто нажмете "отправить", то получите массив и ожидаемое значение!
Вот несколько пар ввода-вывода, которые вы можете обернуть вокруг себя:
И да, это бесстыдная копия известной игры."""


def electrons_around_the_cores(dice):
    dice = [i for i in dice if i % 2]
    return sum(dice)-len(dice)

#вообщем можно было так, так как мы вычетаем длинну списка можно было сразу из каждого элемента вычитать по 1

def electrons_around_the_cores(dice):
    return sum([i-1 for i in dice if i % 2])



#чужой код
def electrons_around_the_cores(dice):
    print(dice.count(5))
    return dice.count(5) * 4 + dice.count(3) * 2  #

def electrons_around_the_cores(dice):
    # Just so you can try some numbers
    return sum([n-1 for n in dice if n==3 or n==5 ])

def electrons_around_the_cores(dice):
    x = (dice.count(3))*2  # count в списке выводит количество элементов в списке, ЗАПОМНИ, если нет выводит 0
    y = (dice.count(5))*4
    return x+y
electrons_around_the_cores=lambda A:sum(~-x*(x%2)for x in A) # ~ не

l = [1, 2, 3, 4, 5]  # 6
l = [ 6, 6, 4, 4, 1, 3 ]# 2
print(electrons_around_the_cores(l))
