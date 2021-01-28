"""Connect 4"""
# The game consists of a grid (7 columns and 6 rows) and two players that take turns to drop their discs.
# The pieces fall straight down, occupying the next available space within the column. The objective of the game is
# to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.
# Your task is to create a Class called Connect4 that has a method called play which takes one argument for the column
# where the player is going to place their disc.
# If a player successfully has 4 discs horizontally, vertically or diagonally then you should return "Player n wins!”
# where n is the current player either 1 or 2.
# If a player attempts to place a disc in a column that is full then you should return ”Column full!” and the next move
# must be taken by the same player.
# If the game has been won by a player, any following moves should return ”Game has finished!”.
# Any other move should return ”Player n has a turn” where n is the current player either 1 or 2.
# Player 1 starts the game every time and alternates with player 2.
# The columns are numbered 0-6 left to right.

# 1 сделать котроль правельности вывода от пользователя
# 2 проверка на возможность бросить в выбранный столбец диска
# 3 проверка на победу
# 4 визуализация в консоль с использование цвета.
# Пусть поле будет словарем

gamefield = {number: [0 for _ in range(6)] for number in range(6)}  # инициализация пустого поля 7х6 через словарь
[print(value) for value in gamefield.values()]  # вывод поля на экран


# 0 - свободно

def checkColumn(column: list) -> bool:
    """Проверка выбранного столбца на свободное место, если свободно возвращается True, иначе False"""
    return not any(column)


print(checkColumn(gamefield[1]))
