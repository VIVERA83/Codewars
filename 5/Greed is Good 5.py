"""Greed is Good 5"""


# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw
# according to these rules. You will always be given an array with five six-sided dice values.
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
# (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
# Example scoring
#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
# In some languages, it is possible to mutate the input to the __function. This is something that you should never do.
# If you mutate the input, you will not be able to pass all the tests.

# Жадность-это игра в кости, в которую играют пятью шестигранными кубиками. Ваша миссия, Если вы решите принять его,
# состоит в том, чтобы забить бросок в соответствии с этими правилами.
# Вам всегда будет дан массив с пятью шестигранными значениями кубиков.
#
#  Three 1's => 1000 points 3
#  Three 6's =>  600 points 3
#  Three 5's =>  500 points 3
#  Three 4's =>  400 points 3
#  Three 3's =>  300 points 3
#  Three 2's =>  200 points 3
#  One   1   =>  100 points 1
#  One   5   =>   50 point  1
# Один кубик может быть подсчитан только один раз в каждом рулоне. Например, данная "5" может считаться только частью a
# триплет (вносящий вклад в 500 очков) или как один 50 очков, но не оба в одном броске.
# # Пример подсчета очков
# #  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
# В некоторых языках можно изменить входные данные для функции. Это то, что вы никогда не должны делать.
# Если вы мутируете входные данные, вы не сможете пройти все тесты.

def score(dice):
    win_dict = {'111': 1000, '666': 600, '555': 500, '444': 400, '333': 300, '222': 200, '1': 100, '5': 50}
    win = 0
    dice = ''.join(map(str, sorted(dice))) # создали строку, отсортированную
    for i in win_dict:                     # идем пословарю и ищим совпадения в строке
        win += win_dict.get(i) * dice.count(i) # Если находи мы их добавляем в общию копилку
        dice = dice.replace(i, '', dice.count(i)) # убираем выбранную компбинацию из строки что бы повторно не вызвать
    return win


lst = [2, 3, 4, 6, 2]  # 0
lst = [4, 4, 4, 3, 3]  # 400
lst = [1, 1, 1, 1, 1]  # 1100
print(score(lst))

# чужой код
"""В целом мой код очень не плох, короткий относительно и понятный, маштабируется под любой массив"""
