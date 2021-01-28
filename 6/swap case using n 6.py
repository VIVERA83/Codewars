

st = 'the quick broWn fox leapt over the fence'
st1 ='the lord of the rings'
n = 9
n1 = 4
def changeWord(st, n):
    binst = str(bin(n)[2:])
    count = len(binst)
    print(binst,count)
    i = 0
    newst = ''
    for ch in st:
        if i > count-1:
            i = 0
        if binst[i] == '1':
            if ch.isupper():
                newst += ch.lower()
            else:
                newst += ch.upper()
        else:
            newst += ch
        print(ch,binst[i])
        if ch.isalpha():
            i += 1
    return newst

# текст для codewars
def changeWord(st, n):
    binst = str(bin(n)[2:])
    count = len(binst)
    i = 0
    newst = ''
    for ch in st:
        if i > count-1:
            i = 0
        if binst[i] == '1':
            #if ch.isupper():
            #   newst += ch.lower()
            #else:
            newst += ch.swapcase() #    newst += ch.upper()     Добавил новый метод строки.
        else:
            newst += ch
        if ch.isalpha():
            i += 1
    return newst

print(changeWord(st,n))
# чужой код:
# from itertools import cycle
# def swap(s,n):
#     b = cycle(bin(n)[2:])
#     print(b)
#     return "".join(c.swapcase() if c.isalpha() and next(b) == '1' else c for c in s)
#
# print(swap(st,n))

