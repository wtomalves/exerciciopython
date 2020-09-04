lista = []
pares = []
impares = []
while True:
    numeros = int(input('Digite um número: '))
    lista.append(numeros)

    if numeros % 2 == 0:
        pares.append(numeros)


    if numeros % 2 != 0:
        impares.append(numeros)

    continuar = str(input('Quer continuar [S/N]:')).strip()
    if continuar in 'Nn':
        break

pares.sort()
impares.sort()
print(f'A lista completa é: {lista}')
print(f'Números pares: {pares}')
print(f'Números impares: {impares}')

