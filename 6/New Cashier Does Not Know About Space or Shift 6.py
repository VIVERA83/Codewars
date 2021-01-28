"""New Cashier Does Not Know About Space or Shift 6"""


# Some new cashiers started to work at your restaurant.
# They are good at taking orders, but they don't know how to capitalize words, or use a space bar!
# All the orders they create look something like this:

# "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
#
# The kitchen staff are threatening to quit, because of how difficult it is to read the orders.
# Their preference is to get the orders as a nice clean string with spaces and capitals like so:
# "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
# The kitchen staff expect the items to be in the same order as they appear in the menu.
# The menu items are fairly simple, there is no overlap in the names of the items:
# 1. Burger
# 2. Fries
# 3. Chicken
# 4. Pizza
# 5. Sandwich
# 6. Onionrings
# 7. Milkshake
# 8. Coke

# В вашем ресторане начали работать новые кассиры.
# Они хорошо принимают заказы, но они не знают, как заглавные буквы слов, или использовать пробел!
# Все заказы, которые они создают, выглядят примерно так:
# ""молочный коктейль пицца курица фри кола бургер пицца сэндвич молочный коктейль пицца"
# Кухонный персонал грозится уволиться из-за того, как трудно читать приказы.
# Они предпочитают получать заказы в виде красивой чистой строки с пробелами и заглавными буквами вот так:
# "Бургер Фри Курица Пицца Пицца Сэндвич С Пиццей Молочный Коктейль Молочный Коктейль Кока-Кола"
# Кухонный персонал ожидает, что продукты будут в том же порядке, как они появляются в меню.
# Пункты меню довольно просты, в названиях пунктов нет перекрытия:
# 1. Бутерброд
# 2. Картофель фри
# 3. Курица
# 4. Пицца
# 5. Сэндвич
# 6. Луковые кольца
# 7. Молочный коктейль
# 8. Кокс


def get_order(order):
    menu = ('Burger',
            'Fries',
            'Chicken',
            'Pizza',
            'Sandwich',
            'Onionrings',
            'Milkshake',
            'Coke')

    new_order = []
    for i in menu:
        for j in range(order.count(i.lower())):
            new_order.append(i)
    return ' '.join(new_order)


# после оптимизации
#  ссоздаем  меню, по которому будем идти и искать есть ли в входящей строке пункт из меню и сколько их, если есть то мы добавляем нужное количество в номый список
# затем список превращаем в строку и возращаем его
def get_order(order):
    menu = ('Burger',
            'Fries',
            'Chicken',
            'Pizza',
            'Sandwich',
            'Onionrings',
            'Milkshake',
            'Coke')

    return ' '.join([i for i in menu for j in range(order.count(i.lower()))])


#                      1............ второй вложенный и из него уже в начало


st1 = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"  # "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke")
st2 = "pizzachickenfriesburgercokemilkshakefriessandwich"  # "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke")'

print(get_order(st2))
