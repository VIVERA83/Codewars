# Get the Middle Character

def get_middle(s):
    return s[len(s) // 2:len(s) // 2+1] if len(s) % 2 else s[len(s) // 2-1:len(s) // 2+1]

# Чужой код
# return s[(len(s)-1)/2:len(s)/2+1]
#  пример  (5-1)//2 = 2  и 5//2+1 = 3  testing = t
#  пример  (4-1)//2 = 1  и 4//2+1 = 3  test = es
st = 'A'
print(get_middle(st))


# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"