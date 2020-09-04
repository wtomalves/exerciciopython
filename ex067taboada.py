taboada = int(input('Qual taboada você quer ver? '))
contador = 0
continuar = ''
while True:
    if taboada < 0:
        print('Não imprimimos taboada com números negativos!')
        break
    if contador != 10:
        contador += 1
        print(f'{taboada} x {contador} = {taboada * contador}')
    if contador == 10:
        contador = 0
        if continuar != 0:
            continuar = int(input('Digite "0" para sair ou outro número para imprimir a taboada: '))
        taboada = 0
        taboada = continuar
    if continuar == 0:
        break








print('Fim')









#print(f'{taboada} x {contador} = {taboada * contador}')
