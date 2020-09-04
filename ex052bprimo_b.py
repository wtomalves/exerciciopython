primo = int(input("DIGITE UM NÚMERO:"))
vezes = 0
contar_divisiveis = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        vezes = vezes + 1
        contar_divisiveis = contar_divisiveis + 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print(' ')
if vezes == 2:
    print('\033[mO número {} é Primo, pois somente foi divisivel por 1 e por ele mesmo!'.format(primo))
else:
    print('\033[mO número {} "NÃO" é Primo, pois foi divisível por {} números!'.format(primo,  contar_divisiveis))


#solução do professor Guanabara com algumas modificações minhas
