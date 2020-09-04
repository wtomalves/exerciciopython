lista = []
cont = 0
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero == 5:
        cont += 1

    continuar = str(input('Continuar [S/N]: ')).strip().upper()
    if continuar == 'N':
        break


lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números!')
print(f'Os numeros em ordem descrecente são: {(lista)}')
if 5 in lista:
    print(f'O valor 5 foi digitado {cont} vez(es)!')
else:
    print('O valor 5 não foi encontrado na lista!')

