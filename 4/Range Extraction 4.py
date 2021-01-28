lst = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
lst = [-3,-2,-1,2,10,15,16,18,19,20]
def solution(args):
    i = 0
    while i < len(args):
        j = i
        while j+1 < len(args) and args[j]+1 == args[j+1]:
            j += 1
        if j - i > 1:
            args[i] = str(args[i])+'-'+str(args[j])
            del args[i+1:j+1]
        i += 1
    return ','.join(map(str,args))

# мой один из лучших
# чужой


def solution(args):
     r = ""
     while args:       # обрати внимание, пока список не пустой
         i = 0
         while i < len(args)-1 and args[i+1] == args[i] + 1:
             i += 1
         if r:
             r += ","
         r += str(args[0])
         if i:
             r += ("-" if i > 1 else ",") + str(args[i])  # оказывается так можно тоже
         args = args[i+1:] # здесь он сокращает список с начала до column
     return r







st = solution(lst)
# st = st+'1'
#print(type(st), st, sep = '')
print(st)
print(("".join(map(str, st))))




#Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
#Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')