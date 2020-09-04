from time import sleep

def numeros(*num):
    maior = 0
    sleep(1)
    print('Analizados os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if valor > maior:
            maior = valor
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(1)
    print(f'O Maior valor informado foi {maior}.' )






numeros(2, 9, 4, 5, 7, 1)
numeros(4, 7, 0)
numeros(1, 2)
numeros(6)
numeros(0)
