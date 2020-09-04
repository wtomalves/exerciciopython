print('Eu consegui chegar até aqui com a ajuda e força de Deus!')
from random import randint


def sorteio():
    num = []
    for c in range(1, 6):
        num.append(randint(0, 10))
    return num


def matematica(*num):
    soma = 0
    numeros = []
    print(f'Sorteando 5 valores da lista:', end=' ')
    for sorteados in num:
        for individual in sorteados:
            print(f'{individual}', end=' ')
            if individual % 2 == 0:
                soma += individual
        print('Pronto!')
    print(f'Somando os valores pares temos a soma de {soma}')

matematica(sorteio())








