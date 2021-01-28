"""Battleship field validator 3kyu"""
# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has
# a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array.
# Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
# Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid
# containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field.
# 'The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version.
# In this kata we will use Soviet/Russian version of the game.
# Before the game begins, players set up the board and place the ships accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines
# (size 1). Any additional ships are not allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just single cell.
# The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
# This is all you need to solve this kata. If you're interested in more information about the game

# Напишите метод, который принимает поле для известной настольной игры "линкор" в качестве аргумента и возвращает true,
# если у него есть допустимое расположение кораблей, false в противном случае. Аргумент гарантированно будет
# представлять собой двумерный массив размером 10*10. Элементами в массиве являются числа: 0, если ячейка свободна, и 1,
# если занята кораблем. Линкор (также линкор или морской бой) - это игра в угадайку для двух игроков. У каждого игрока
# есть сетка 10х10, содержащая несколько "кораблей", и цель состоит в том, чтобы уничтожить силы противника,
# нацеливаясь на отдельные клетки на его поле. Корабль занимает одну или несколько ячеек в сетке. Размер и количество
# кораблей могут отличаться от версии к версии. В этом ката мы будем использовать советскую / русскую версию игры.
# Перед началом игры игроки устанавливают доску и расставляют корабли в соответствии со следующими правилами:
# Там должны быть один линкор (размер 4 ячейки), 2 крейсера (размер 3), 3 эсминца (размер 2) и 4 подводные лодки
# (размер 1). Любые дополнительные корабли не допускаются, равно как и пропавшие корабли.
# Каждый корабль должен быть прямой линией, за исключением подводных лодок, которые представляют собой только одну
# ячейку. Корабль не может пересекаться или соприкасаться с любым другим кораблем ни краем, ни углом.
# Это все, что вам нужно, чтобы решить эту Кату. Если вас интересует более подробная информация об игре,


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]  # True


battleField = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
               [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]  # False

class CheckField:

    def __init__(self, battlefield: list):
        self.N = len(battlefield)
        self.length_field = self.N * self.N
        # Перевожу двухмерный список в одномерный, мне так проще работать
        self.battlefield = [value for line in battlefield for value in line]
        # Список в котором будут отмечаться посещенные ячейки, нужен для того что бы 2 раза не заходить в одну ячейку
        self.visit = [False]*self.length_field
        # Список найденных кораблей, нужен для проверки соответствия условиям
        self.ships = {1: 0,
                      2: 0,
                      3: 0,
                      4: 0}
        # Словарь, нужен для рекурсивного определения корабля, и определения на соприкосновение с другим кораблем
        self.dict_errors = {'bottom': False,
                            'right': False,
                            'down': False}

    def check(self) -> bool:
        """Метод, в котором производится обход всего списка “battlefield” на наличие кораблей (1), как только находим
        корабль запускаем, метод ” identification_ship ” который определяет количество палуб и есть ли нарушения
        расположения корабля на поле, если нарушений нет то в конце производим проверку на кол-во кораблей по их типу,
        если все нормально возвращаем True, иначе False
        Method in which the entire “battlefield " list is crawled for the presence of ships (1), as soon as we find
        ship launch, method "identification_ship" which determines the number of decks and whether there are violations
        the location of the ship on the field, if there are no violations, then at the end we check for the number of
        ships by their type, if everything is fine, we return True, otherwise False"""

        for index, value in enumerate(self.battlefield):
            # Если мы еще не посещали ячейку и ее значение 1, запускаем определение корабля
            # и правильность его расположения на поле "battlefield"
            if not self.visit[index] and value and not self.identification_ship(index):
                return False
            # заносим информацию о том что посетили ячейку, что бы дважды не заходить в нее
            self.visit[index] = True
            # Проверка на правильное количество кораблей на поле, если все нормально возвращаем TRUE
        return all([key+value == 5 for key, value in self.ships.items()])

    def getDictErrors(self, index):
        """Метод обновляет значения словаря "dict_errors" из трех элементов типа bool. Ключ "bottom"  - True, означает
        что корабли расположены слишком близко и нарушают правела размещения. Ключ "right" - True, означает что корабль
        расположен горизонтально и метод "identification_ship" продолжит считать палубы в ->. ключ "down" - True,
        означает, что корабль расположен вертикально и метод "identification_ship" продолжит считать палубы вниз,
        если ключи "right" и "down" оба равны True то это означает неправильную расстановку кораблей
        The method updates the values of the dictionary "dict_errors" from three elements of the bool type. The "bottom"
        key is True, meaning that the ships are located too close and violate the rules of placement.
        The key "right" - True, means that the ship positioned horizontally and the "identification_ship" method will
        continue to count decks in ->. the "down" key is True, means that the ship is positioned vertically and the
        "identification_ship" method will continue to count the decks down, if the keys "right" and "down" are both
        True, then this means that the ships are placed incorrectly"""

        # Обнуляем значение словаря
        for i in self.dict_errors:
            self.dict_errors[i] = False

        # Eсли index >= длине поля
        if index >= self.N * self.N:
            self.dict_errors['bottom'] = True
        else:
            # Проверка на то что ПРАВАЯ ячейка входит в поле и если она = 1 вносим True
            if all([index + 1 < self.N * self.N, (index + 1) // self.N == index // self.N]):
                self.dict_errors['right'] = bool(self.battlefield[index + 1])

            # Проверка на то что НИЖНЯЯ ячейка входит в поле и если она = 1 вносим True
            if all([index + self.N < self.N * self.N, (index + self.N) // self.N > index // self.N]):
                self.dict_errors['down'] = bool(self.battlefield[index + self.N])

            # Проверка на то что НИЖНЯЯ ЛЕВАЯ ячейка входит в поле и если она = 1 вносим True
            # (означает неправильную расстановку кораблей)
            if all([index + self.N - 1 < self.N*self.N, (index + self.N - 1) // self.N > index//self.N]):
                self.dict_errors['bottom'] = bool(self.battlefield[index + self.N - 1])

            # Проверка на то что НИЖНЯЯ ПАРВАЯ ячейка входит в поле и если она = 1 вносим True
            # (означает неправильную расстановку кораблей)
            if all([index + self.N + 1 < self.N*self.N, (index + self.N + 1) // self.N == index//self.N+1]):
            # если 'bottom' уже True, мы ее не перезаписываем
                if not self.dict_errors['bottom']:
                    self.dict_errors['bottom'] = bool(self.battlefield[index + self.N + 1])


    def identification_ship(self, index:int, count_right=0, count_down=0):
        """Метод определяет длину корабля, и вносит его в словарь ships, если обнаружена ошибка то возвращает False
        The method determines the length of the ship, and enters it in the ships dictionary, if an error is detected
        it returns False"""

        # обновляем словарь "dict_errors"
        self.getDictErrors(index)
        if self.dict_errors['bottom']:
            return False
        else:
            # заносим информацию о том что посетили ячейку, что бы дважды не заходить в нее
            self.visit[index] = True
            # если "right" - то идем по рекурсии в право, пока right не False
            if self.dict_errors['right']:
                self.identification_ship(index + 1, count_right + 1, 0)
            # если "down" - то идем по рекурсии в вниз
            elif self.dict_errors['down']:
                self.identification_ship(index + self.N, 0, count_down+1)
            # После того как рекурсия закончится и количество палуб меньше 5, увеличиваем значения ключа на 1
            # один из count_right или count_down по результатам всегда будет равен 0
            elif count_right+count_down+1 < 5:
                self.ships[count_right+count_down+1] += 1
            # если палуб больше 5, значит неправильная расстановка
            else:
                return False
        return True

def validate_battlefield(field):
    return CheckField(field).check()

print(f' результат {validate_battlefield(battleField)}')

# v v v - check (ok) Проверенные клетки, все хорошо
# v 1 ? - 1 - клетка в которой найдена палуба    right -
# ? ? ? - bottom, down, bottom  -
#