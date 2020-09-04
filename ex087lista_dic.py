'''Exercício com mais três funcionalidades utilizando coluna específica '''
lista = [[],[],[]]

soma = 0
soma_terceira_coluna = 0
maior = 0
for c in range(0,3):
    num = int(input(f'Digite um valor para posição [0, {c}]: '))
    lista[0].append(num)
    if num % 2 == 0:
        soma = soma + num

for c in range(0,3):
    num = int(input(f'Digite um valor para posição [1, {c}]: '))
    lista[1].append(num)
    if num % 2 == 0:
        soma  = soma + num

for c in range(0,3):
    num = int(input(f'Digite um valor para posição [2, {c}]: '))
    lista[2].append(num)
    if num % 2 == 0:
        soma  = soma + num


print('=' * 50)
for linha in lista:
    for c in linha:
        print(f'[ {c:^5} ]', end='')
    print('')

print('=' * 50)


print(f'A soma dos valores pares é {soma}!')


for c in lista:
    soma_terceira_coluna += c[2]

print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}!')

for c in range(1):
    lista[1].sort()

print(f'O maior número da segunda linha é {lista[1][-1]}!')



