
lista = [[],[],[]]

for c in range(0,3):
    num = int(input(f'Digite um valor para posição [0, {c}]: '))
    lista[0].append(num)

for c in range(0,3):
    num = int(input(f'Digite um valor para posição [1, {c}]: '))
    lista[1].append(num)

for c in range(0,3):
    num = int(input(f'Digite um valor para posição [2, {c}]: '))
    lista[2].append(num)


for linha in lista:
    for c in linha:
        print(f'[ {c:^5} ]', end='')
    print('')

