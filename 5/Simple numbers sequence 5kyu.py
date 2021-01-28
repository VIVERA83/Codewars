def missing(s):

   # print(s)
    n = len(s)//2
   # print('длинна строки:',n)
    step = -1
    chek = -1
    p=0
    for i in range(1,n+1):
        p=p+1
        a = int(s[:i])
        b = int(s[i:i+i])
        c = (a + b) // 2
        #print(a,b,c, a==c, a!=b, a==0)
        if ((a == c) and (a != b) or (a == 0)) or (a+1 ==c):
            step = i
        elif (a > c) or (a == b):
            b = int(s[i:i+i+1])
            c = (a + b) // 2
            if a+1 == c:
                step = i

    n = len(s)
    move = 0
    flag = True
    chek = -1
   # print(step)
    while move + step != n:
        p=p+1
        a = int(s[move:move + step])
        b = int(s[move + step:move + 2 * step])
        c = (a + b) // 2
       # print(a,b,c, chek)
        if a > b > c:
            step += 1
        if b > c+1 > a:
            return -1, p
        if a > c > b:
            b = int(s[move + step:move + 2 * step+1])
            c = (a + b) // 2
            move += step
            step +=1
            flag = False
        if b > c > a:
            if (chek == -1) and ( b==c+1):
                chek = c
            else:
               # print('Вылет 1')
                return -1, p

        if flag:
            move += step
        flag = True
    return chek, p

# чужой код
def missing(seq):
    i=0
    for digits in range(1, len(seq) // 2 + 1):
        i=i+1
        my_seq = last = seq[:digits]
        n = int(my_seq)
     
        missing = None

        while len(my_seq) < len(seq):
            n += 1
            my_seq += str(n)

            if not seq.startswith(my_seq):
                if missing == None:
                    missing = n
                    my_seq = last
                else:
                    break
            else:
                last = my_seq

        if my_seq == seq and missing:
            return missing, i

    return -1 , i

print(missing('99299399499599699799899910021003'))  #-1
print(missing('464903464905464906464907464908464909464910464911464912464913464914464915')) # 464904
print('****')
print('TEST-1')
print(missing("123567")) # = 4
print('TEST-2')
print(missing("899091939495")) #= 92
print('TEST-3')
print(missing("9899101102")) # = 100
print('TEST-4')
print(missing("599600601602"))  #= -1 -- no number missing
print('TEST-5')
print(missing("8990919395"))  # = -1 -- error in sequence. Both 92 and 94 missing.
print('TEST-6')
print(missing('900001900002900004900005900006')) #90003
print('TEST-7')
print(missing("99991000110002"))    #10000
print('TEST-8')
print(missing('99899990999199929993999599979998999910000')) #-1