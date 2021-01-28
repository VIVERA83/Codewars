"""Snail Sort 4"""
# Given an n x n array, return the array elements arranged from outermost elements to the middle element,
# traveling clockwise.

# Учитывая массив n x n, верните элементы массива, расположенные от самых внешних элементов к среднему элементу,
# перемещаясь по часовой стрелке


#        [1,2,3,6,9,8,7,4,5]

# def snail(array):
#     new_array = []
#     len_x = len(array)
#     len_y = len(array[0])
#     print(f'длинна по х: {len_x} длинна по у: {len_y}')
#
#     begin_x = 0
#     end_x = len(array) -1
#     begin_y = 0
#     end_y = len(array[0])
#     flag = True  # для реверса
#
#     print(array[1][1])
#
#     column = 0
#     print(end_x,end_y)
#     while column < 3:
#         for x in range(begin_x if flag else end_x, end_x if flag else begin_x-1, 1 if flag else -1):
#             print(f'y {begin_y if flag else end_y} x {x}')
#             new_array.append(array[begin_y if flag else end_y][x])
#         print(column,new_array)
#         if flag:
#              begin_y += 1
#         for y in range(begin_y if flag else end_y-1, end_y if flag else begin_y+1, 1 if flag else -1):
#             print(end_x, y)
#             new_array.append(array[y][end_x])
#
#         print(column,new_array)
#
#         column += 1
#         if flag:
#             end_x -= 1
#             end_y -= 1
#
#         print(f'end_x {end_x} end_y {end_y} FLAG={flag}')
#         flag = not flag
#
#     return new_array
# array = [[ 1,  2,  3,  4, 5],
#          [14, 15, 16, 17, 6],
#          [13, 20, 19, 18, 7],
#          [12, 11, 10,  9, 8]]
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
# array = [[1, 2, 3],
#           [10, 11, 4],
#           [9, 12, 5],
#           [8, 7, 6]]

def snail(array): # рабочая версия
    """Функция сортирует двухмерный список по спирали с лева на право, по кругу в внутрь
   [[1,2,3], и выводит его в одномерный список [1,2,3,4,5,6,7,8,9]
   [8,9,4],
   [7,6,5]]
    """
    n = len(array[0])  # ширина списка (после полукруга будет уменьшаться на -1)
    array = [j for i in array for j in i]  # список преобразуем в одномерный для простоты работы
    new_array = []
    flag = True  # нужен для реверсивного движения по списку
    while array:
        step = 0  # Нужен для кореектировки при удалении элемента из старого массива
        # везде если flag = true идем от начала , при False в обратном порядке
        # первый полукруг 12345, второй 678
        for i in range(0 if flag else len(array) - 1, n if flag else len(array) - n - 1, 1 if flag else -1):
            new_array.append(array.pop(i - step))
            if flag:
                step += 1
        step = 0
        for i in range(0 if flag else len(array), len(array) if flag else 0, n if flag else -n):
            new_array.append(array.pop(i - 1 - step + n if flag else i - n))
            step += 1
        n -= 1
        flag = not flag
    return new_array

print(snail(array))

# чужой код
def snail(snail_map):
    result = []
    while snail_map: # вот идея пока массив не пустой
        result += snail_map.pop(0) # получается так он берет певую ячейку списка
        print(snail_map)
        print(result)
        snail_map = list(zip(*snail_map))[::-1] # далее спомощью зипа разбивает оставшийся масив на одинаковые кусочки берет  последний с последним элементом  [::-1],таким образом пересоздает список очень круто
        print('вот что дальше',snail_map)
    return result

snail = lambda a: list(a[0]) + snail(zip(*a[1:])[::-1]) if a else []

def snail(map):
    res=[]
    while map:
        for i in map[0]:
            res.append(i)
        map=map[1:]
        if not map:break
        for i in map:
            res.append(i[-1])
        map=[i[:-1] for i in map]
        if not map:break
        for i in map[-1][::-1]:
            res.append(i)
        map=map[:-1]
        if not map:break
        for i in map[::-1]:
            res.append(i[0])
        map=[i[1:] for i in map]
    return res
print(snail(array))