"""Function Addition 5 kyu"""


# I often find that I end up needing to write a function to return multiple values, in this case I would often split it
# up into two different functions but then I have to spend time thinking of a new function name! Wouldn't it be great
# if I could use same name for a function again and again...
# In this kata your task is to make a decorator, FuncAdd which will allow function names to be reused and when called
# all functions with that name will be called (in order) and the results returned as a tuple.
# foo() --> ('Hello', 'World')
# As well as this you will have to implement two more things, a way of deleting a particular function, and a way of
# deleting all stored functions. The delete method must work as follows:
# FuncAdd.delete(foo) # Delete all foo() functions only
# foo() # Should raise NameError
# And the clear method must work like this:
# И метод clear должен работать так
# foo() # Should raise NameError

# Я часто обнаруживаю, что мне нужно написать функцию для возврата нескольких значений, в этом случае я часто разделяю
# ее на две разные функции, но тогда мне приходится тратить время на обдумывание нового имени функции! Не было бы
# здорово, если бы я мог использовать одно и то же имя для функции снова и снова...
# В этом ката ваша задача состоит в том, чтобы сделать декоратор, FuncAdd, который позволит повторно использовать имена
# функций, и при вызове все функции с этим именем будут вызваны (по порядку), а результаты вернутся в виде кортежа.
# Кроме того, вам придется реализовать еще две вещи: способ удаления конкретной функции и способ удаления всех
# сохраненных функций. Метод delete должен работать следующим образом:
# FuncAdd.delete(foo) # Удаляются все функции foo() Delete all foo()
# foo() # вернуть исключение NameError

class FuncAdd:
    __dict_fun = {}

    def __init__(self, function):
        """При каждом объявлении декоратора над функцией, в словарь __dict_fun заносим функцию и ее имя, имя в значение
        так как имена могут повторяться"""
        self.__function = function

        FuncAdd.__dict_fun.setdefault(function, function.__name__)

    def __call__(self, *args, **kwargs):
        """Метод запускается при вызове функции декоратора, self - декарированная функция """
        res = tuple(
            fun(*args, **kwargs) for fun, name in FuncAdd.__dict_fun.items() if self.__function.__name__ is name)
        if res:
            return res
        else:
            raise NameError

    def delete(self):
        """Метод удаляет все декорированные функции из словаря, функция которая передается на удаление передается
         в self"""
        lst_del = [fun for fun, name in FuncAdd.__dict_fun.items() if self.__function.__name__ is name]
        if lst_del:
            FuncAdd.__dict_fun = {fun: name for fun, name in FuncAdd.__dict_fun.items() if fun not in lst_del}
        else:
            raise NameError

    @staticmethod
    def clear():
        FuncAdd.__dict_fun.clear()


# Проверка
@FuncAdd
def add(a, b):
    return a + b


@FuncAdd
def spam():
    return 'Hello'


@FuncAdd
def add(a, b):
    return a * b


@FuncAdd
def spam():
    return 'World'


@FuncAdd
def ham():
    return 'Eggs'


print(add(2, b=5))
print(spam())
print(ham())
FuncAdd.delete(spam)

FuncAdd.clear()
