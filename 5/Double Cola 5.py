"""Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine;
there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles!
The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can,
drinks it and gets to the end of the queue as two Leonards, and so on.
For example, Penny drinks the third can of cola and the queue will look like this:
Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
Input:
The input data consist of an array which contains at least 1 name, and single integer n which may go as high as
the biggest number your language of choice supports (if there's such limit, of course).

who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
"""

def who_is_next(names, r):
    number = len(names)
    prog, mysum, i = 1, 0, 0
    while r > mysum + prog * number:
        mysum += prog * number
        prog *= 2
    while (r - mysum) > i * prog:
        i += 1
    return names[i-1]

# чужой код
#def who_is_next(names, r):
#    while r > len(names):
#        r = (r - len(names) + 1) // 2
#    return names[r-1]

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
#names =['Batou', 'Sheldon', 'Togusa', 'Saito', 'Yano', 'Proto', 'Daisuke Aramaki', 'Motoko Kusanagi']# 8 269 Sheldon
print(who_is_next(names, 2))
#test.assert_equals(who_is_next(names, 1), "Sheldon")
#test.assert_equals(who_is_next(names, 52), "Penny")
#test.assert_equals(who_is_next(names, 7230702951), "Leonard")
# 11 43 ['Howard', 'Penny', 'Daisuke Aramaki', 'Azuma', 'Proto', 'Motoko Kusanagi', 'Rajesh', 'Saito', 'Togusa', 'Yano', 'Leonard'] saito
"""
моя прошла тест
def who_is_next(names, r):
    number = len(names)
    prog = 1
    mysum = 0
    while r > mysum + prog * number:
        mysum += prog * number
        prog *= 2
    print(f'r= {r} mysum= {mysum}  prog= {prog}')
    ostatok = r - mysum
    print(f'ostatok= {ostatok}')
    column = 0
    while ostatok > (column) * prog:
        column += 1
    print(f'column= {column} (column+1)*prog={(column)*prog},')

    indeks = ostatok % prog
    print(indeks)
    return names[column-1]
"""
