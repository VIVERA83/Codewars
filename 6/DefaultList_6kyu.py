"""DefaultList 6kyu"""


# The collections module has defaultdict, which gives you a default value for trying to get the value of a key which
# does not exist in the dictionary instead of raising an error. Why not do this for a list? Your job is to create
# a class (or a __function which returns an object) called DefaultList. The class will have two parameters to be given:
# a list, and a default value. The list will obviously be the list that corresponds to that object. The default value
# will be returned any time an index of the list is called in the code that would normally raise an error
# (i.e. i > len(list) - 1 or i < -len(list)). This class must also support the regular list functions extend, append,
# insert, remove, and pop. Because slicing a list never raises an error (slicing a list between two indexes that are
# not a part of the list returns [], slicing will not be tested for.

# Модуль collections имеет defaultdict, который дает вам значение по умолчанию для попытки получить значение ключа,
# которого нет в словаре, вместо того чтобы вызывать ошибку. Почему бы не сделать это для списка? Ваша задача-создать
# класс (или функцию, которая возвращает объект), называемый списком по умолчанию. Класс будет иметь два параметра:
# список и значение по умолчанию. Список, очевидно, будет тем списком, который соответствует этому объекту. Значение по
# умолчанию будет возвращено каждый раз, когда индекс списка вызывается в коде, который обычно вызывает ошибку
# (например, i > len(list) - 1 или i < -len(list)). Этот класс также должен поддерживать обычные функции списка extend,
# append, insert, remove и pop.  Поскольку нарезка списка никогда не вызывает ошибки (нарезка списка между двумя
# индексами, которые не являются частью списка, возвращает [], нарезка не будет проверяться.

class DefaultList(list):
    def __init__(self, array: list, default_value):
        list.__init__(self, array)
        self.default_value = default_value

    def __getitem__(self, key):
        if key >= len(self) or abs(key) > len(self):
            return self.default_value
        else:
            return list.__getitem__(self, key)

    def __setitem__(self, key, value):
        if key >= len(self):
            list.append(self,value)
        else:
            list.__setitem__(self, key, value)



g = DefaultList(['hello', 'abcd', '123', 123, True, False], 'default_value')
lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')

# Маленький тест на выявления возможных ошибок
print(lst[-1])
print(lst[333000])
lst.extend([3, 23, 'hello', 'lists', 'word', 344])
lst[100] = 'lists'
print(lst[9])
g.append(lst)
lst.append(233344455)
print(lst[12])
print(lst[100])
lst.remove(2)
lst.remove(1)
lst.remove(3)
lst.insert(-3, 34.34)
print(lst[8])
print(lst[10])
print(lst)
print(g)

