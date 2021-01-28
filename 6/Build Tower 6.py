

def tower_builder(n_floors):
    return [('*' + '*' * i * 2).center((n_floors - 1) * 2 + 1) for i in range(n_floors)]

    # for column in range(n_floors):
    #    print(('*'+'*'*column*2).center((n_floors-1)*2+1))

# у меня одно из лучших решений



# чужой код
tower_builder=lambda n:[str.center('*'*i,n*2-1)for i in range(1,n*2,2)]
# return ['{}{}{}'.format(' '*ind,'*'*((2*n_floors-1)-ind*2),' '*ind) for ind in range(n_floors)][::-1]