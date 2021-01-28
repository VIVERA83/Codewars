# Sudoku Solution Validator 4
b = \
    [[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]] # True


k = [1, 3, 2, 5, 7, 9, 4, 6, 8,
     4, 9, 8, 2, 6, 0, 3, 7, 5,
     7, 0, 6, 3, 8, 0, 2, 1, 9,
     6, 4, 3, 1, 5, 0, 7, 9, 2,
     5, 2, 1, 7, 9, 0, 8, 4, 6,
     9, 8, 0, 4, 2, 6, 5, 3, 1,
     2, 1, 4, 9, 3, 5, 6, 8, 7,
     3, 6, 0, 8, 1, 7, 9, 2, 4,
     8, 7, 0, 6, 4, 2, 1, 3, 5]

l = [1, 3, 2, 5, 7, 9, 4, 6, 8,
     4, 9, 8, 2, 6, 1, 3, 7, 5,
     7, 5, 6, 3, 8, 4, 2, 1, 9,
     6, 4, 3, 1, 5, 8, 7, 9, 2,
     5, 2, 1, 7, 9, 3, 8, 4, 6,
     9, 8, 7, 4, 2, 6, 5, 3, 1,
     2, 1, 4, 9, 3, 5, 6, 8, 7,
     3, 6, 5, 8, 1, 7, 9, 2, 4,
     8, 7, 9, 6, 4, 2, 1, 3, 5]

def valid_solution(board):
    N = 9;  n = 3
    setA = set()
    for i in board:
        if (0 in set(i)) or (len(set(i))<0):
            return False
    for j in range (N):
        setA.clear();
        for i in range (N):
            setA.add(board[i][j])
            print(f' i={i}   j={j}   {board[i][j]}')
        print(f'setA={setA}, {len(setA)}')

    lst =[] #board

    for i in board:
        for j in i:
            lst.append(j)
    #print(array)
    for y in range(n) :
        for x in range(n):
            setA = set()
            for i in range(n):
                index = (y * N * n) + (x * n) + (i * N)
                setA.update(lst[index:index+n])
                print(lst[index:index+n], sum(lst[index:index+n]))
            print(f'setA={setA} index={index} срез = {lst[index:index+n]} ')
            if (0 in setA) or (len(setA) < N):
                return False
    return True




def valid_solution(board):
    N = 9;  n = 3
    setA = set()
    lst = []
    for i in board:
        if (0 in set(i)) or (len(set(i)) < N):
            return False
    for j in range(N):
        setA.clear()
        for i in range(N):
            setA.add(board[i][j])
        if len(setA) < N:
            return False

#    array = [    zip(*board)]
    for i in board:
        for j in i:
            lst.append(j)
    for y in range(n):
        for x in range(n):
            setA = set()
            for i in range(n):
                index = (y * N * n) + (x * n) + (i * N)
                setA.update(lst[index:index+n])
                print(lst[index:index+n], sum(lst[index:index+n]))
            print(f'setA={setA} index={index} срез = {lst[index:index+n]} ')
            if len(setA) < N:
                return False
    return True
# b[0].sort()

# print(b[0])
#print(*b, sep='\n')
print(valid_solution(b))

