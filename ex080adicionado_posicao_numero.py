lista = []
numero = int(input('Digite um número: '))
lista.append(numero)
print('Adcionado ao final da lista')
for c in range(4):
    numero = int(input('Digite um número: '))
    if numero < lista[0]:
        lista.insert(0, numero)
        print('Adicionado na posição 0!')
    elif numero > lista[-1]:
        lista.append(numero)
        print('Adicionado ao final da lista!')

    else:
        for posicao, valor in enumerate(lista):
            if numero < valor:
                lista.insert(posicao, numero)
                print(f'Adicionado na posição {posicao}!')
                break

print(lista)
