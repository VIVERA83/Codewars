"""Image host filename generator 6kyu"""

# You are developing an image hosting website. You have to create a __function for generating random and
# unique image filenames. Create a __function for generating a random 6 character string which will be used to access
# the photo URL.To make sure the name is not already in use, you are given access to an PhotoManager object. You can call
# it like so to make sure the name is unique

# Вы разрабатываете сайт для размещения изображений. Вы должны создать функцию для генерации случайных и уникальных имен
# файлов изображений. Создайте функцию для генерации случайной 6-символьной строки, которая будет использоваться для
# доступа к URL-адресу фотографии. Чтобы убедиться, что имя еще не используется, Вам предоставляется доступ к объекту
# PhotoManager. Вы можете назвать его так, чтобы убедиться, что имя уникально

from random import randint

def generateName():
    return ''.join([chr(randint(49, 122)) for i in range(6)])


# чужой код
# нужно запомнить данную библиотеку
# import uuid
# def generateName():
#     return str(uuid.uuid4())[:6]



