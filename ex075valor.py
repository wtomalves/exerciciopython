valores = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input(''
         'Digite mais um número: ')), int(input('Digite o último número: '))

print(f'Você digitou os valores {valores}')
contar_9 = contar_3 = 0
par = impar = 0
for posicao, valor in enumerate(valores):
    if valor == 9:
        contar_9 += 1
        print(f'O valor {valor} está na posição {posicao}')

    if valor == 3:
        contar_3 += 1
        print(f'O valor {valor} está na posição {posicao}')

if contar_9 == 0:
    print('O valor 9 apareceu 0 vezes!')

if contar_3 == 0:
    print('O valor 3 apareceu 0 vezes!')

print('Os números pares são: ', end='')
for valor in valores:
    if valor % 2 == 0:
        print(f' {valor}', end=' ')


print('')
print('********************************************')